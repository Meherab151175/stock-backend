from sqlmodel import SQLModel, Field
from datetime import date


class Stock(SQLModel, table=True):
    __tablename__ = "stocks"
    id: int | None = Field(default=None, primary_key=True)
    date: date
    trade_code: str
    high: float
    low: float
    open: float
    close: float
    volume: int
