from typing import Dict, List, Type, Optional, Any
from dataclasses import dataclass
from PySide6.QtWidgets import QWidget

@dataclass
class PageMeta:
  name: str
  view_class: Type[QWidget]
  controller_class: Type
  requires_auth: bool = False
  roles: List[str] = ['customer', 'manager']
  category: str = 'main'  # For grouping/organization
  icon: Optional[str] = None  # For menu displays
  order: int = 0  # Display order
  
class PageRegistry:
  _pages: Dict[str, PageMeta] = {}
  _initialized = False
  
  @classmethod
  def register_page(
    cls,
    name: str,
    view_class: Type[QWidget],
    controller_class: Type,
    **kwargs
  ):
    """Register a new page with the application"""
    if name in cls._pages:
      raise ValueError(f"Page '{name}' is already registered")
        
    cls._pages[name] = PageMeta(
      name=name,
      view_class=view_class,
      controller_class=controller_class,
      **kwargs
    )
    
  @classmethod
  def get_page_meta(cls, name: str) -> PageMeta:
    """Get metadata for a specific page"""
    return cls._pages.get(name)
  
  @classmethod
  def get_all_pages(cls) -> List[PageMeta]:
    """Get all registered pages in registration order"""
    return sorted(
      list(cls._pages.values()),
      key=lambda x: x.order
    )
    
  @classmethod
  def get_available_pages(cls, user_roles: List[str] = None) -> List[PageMeta]:
    """Get pages accessible to current user"""
    available = []
    for page in cls.get_all_pages():
      if not page.requires_auth or not user_roles:
        available.append(page)
      elif page.roles and any(role in user_roles for role in page.roles):
        available.append(page)
      return available

  @classmethod
  def initialize_pages(cls, container: 'Container') -> Dict[str, QWidget]:
    """Instantiate all registered pages"""
    if cls._initialized:
      raise RuntimeError("Pages already initialized")
        
    instances = {}
    for name, meta in cls._pages.items():
      # Resolve dependencies from DI container
      controller = container.resolve(meta.controller_class)
      view = container.resolve(meta.view_class)
      controller.view = view
      instances[name] = view
            
    cls._initialized = True
    return instances