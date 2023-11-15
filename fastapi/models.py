from database import Base

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship


class TradingItem(Base):
    __tablename__ = "trading_data"

    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    amount = Column(Float)
    time = Column(Integer, default=14102023)
    userID = Column(Integer, nullable=True)

