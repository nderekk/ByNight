from typing import Dict, Type, Any

class Container:
  _instances: Dict[Type, Any] = {}
  _factories: Dict[Type, callable] = {}
  
  @classmethod
  def register(cls, interface: Type, implementation: Type):
    cls._factories[interface] = implementation
    
  @classmethod
  def resolve(cls, interface: Type) -> Any:
    if interface not in cls._instances:
      if interface not in cls._factories:
        raise ValueError(f"No implementation registered for {interface}")
      cls._instances[interface] = cls._factories[interface]()
    return cls._instances[interface]
  
  @classmethod
  def add_existing_instance(cls, interface: Type, existing_obj: Type):
    if interface not in cls._instances:
      cls._instances[interface] = existing_obj
      
  @classmethod
  def is_initialized(cls, interface: Type):
    if interface not in cls._instances:
      return False
    return True