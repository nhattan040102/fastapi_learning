from typing import Optional
from pydantic import BaseModel


class TradingData(BaseModel):
    id: int
    symbol: str
    amount: float
    time: int = 14102023
    userID: int = None

    class Config:
        orm_mode=True


class TradingParams(BaseModel):
    symbol: str

