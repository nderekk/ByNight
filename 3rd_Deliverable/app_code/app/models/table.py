from sqlalchemy import Column, Integer, Float, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from app.data.database import Base
import app.models
from enum import Enum

class TableType(str, Enum):
    VIP = "VIP"
    PASS = "Pass"
    BAR = "bar"

class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True)
    capacity = Column(Integer, nullable=False)
    table_type = Column(SQLAlchemyEnum(TableType), nullable=False)

    # Assuming a club owns tables
    club_id = Column(Integer, ForeignKey("clubs.id"), nullable=False)
    club = relationship("Club", back_populates="tables")

    reservations = relationship("Reservation", back_populates="table", cascade="all, delete-orphan")
    
    @classmethod
    def get_capacity_on_table_type(cls, table_type: str) -> int:
        if table_type == TableType.PASS.value:
            return 4
        elif table_type == TableType.VIP.value:
            return 10
        elif table_type == TableType.BAR.value:
            return 3
        else:
            print("TIN GAMISAME")
