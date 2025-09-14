from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import json
from pydantic import BaseModel
from datetime import date
from pathlib import Path
from uuid import UUID, uuid4

# Path to JSON file
DATA_FILE = Path(__file__).parent / "stock_market_data.json"

app = FastAPI(title="Stock CRUD API (JSON + UUID)")

# Frontend URLs
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://stock-fronted.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model
class Stock(BaseModel):
    id: UUID
    date: date
    trade_code: str
    high: float
    low: float
    open: float
    close: float
    volume: int

# 🔹 Helper functions
def parse_number(value: str) -> float:
    """Convert string with commas to float"""
    if isinstance(value, (int, float)):
        return float(value)
    return float(str(value).replace(",", ""))

def parse_int(value: str) -> int:
    """Convert string with commas to int"""
    if isinstance(value, int):
        return value
    return int(str(value).replace(",", ""))

def preprocess_stock(item: dict) -> Stock:
    """Convert raw JSON item to Stock with UUID"""
    stock_id = UUID(item["id"]) if "id" in item else uuid4()
    return Stock(
        id=stock_id,
        date=item["date"],
        trade_code=item["trade_code"],
        high=parse_number(item["high"]),
        low=parse_number(item["low"]),
        open=parse_number(item["open"]),
        close=parse_number(item["close"]),
        volume=parse_int(item.get("volume", 0))
    )

def load_data() -> List[Stock]:
    """Load stocks from JSON file safely"""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
    return [preprocess_stock(item) for item in raw_data]

def save_data(data: List[Stock]):
    """Save list of Stock objects to JSON"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([s.dict() for s in data], f, indent=2, default=str)

# 🔹 Endpoints
@app.get("/stocks", response_model=List[Stock])
def get_stocks(
    trade_code: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1)
):
    stocks = load_data()
    if trade_code and trade_code.lower() != "all":
        stocks = [s for s in stocks if s.trade_code == trade_code]
    return stocks[skip: skip + limit]

@app.get("/stocks/trade-codes", response_model=List[str])
def get_trade_codes():
    stocks = load_data()
    return list(sorted({s.trade_code for s in stocks}))

@app.get("/stocks/{stock_id}", response_model=Stock)
def get_stock(stock_id: UUID):
    stocks = load_data()
    for stock in stocks:
        if stock.id == stock_id:
            return stock
    raise HTTPException(status_code=404, detail="Stock not found")

@app.post("/stocks", response_model=Stock)
def create_stock(stock: Stock):
    stocks = load_data()
    if any(s.id == stock.id for s in stocks):
        raise HTTPException(status_code=400, detail="Stock with this ID already exists")
    if not stock.id:
        stock.id = uuid4()
    stocks.append(stock)
    save_data(stocks)
    return stock

@app.put("/stocks/{stock_id}", response_model=Stock)
def update_stock(stock_id: UUID, updated_stock: Stock):
    stocks = load_data()
    for i, s in enumerate(stocks):
        if s.id == stock_id:
            updated_stock.id = stock_id
            stocks[i] = updated_stock
            save_data(stocks)
            return updated_stock
    raise HTTPException(status_code=404, detail="Stock not found")

@app.delete("/stocks/{stock_id}")
def delete_stock(stock_id: UUID):
    stocks = load_data()
    new_stocks = [s for s in stocks if s.id != stock_id]
    if len(new_stocks) == len(stocks):
        raise HTTPException(status_code=404, detail="Stock not found")
    save_data(new_stocks)
    return {"ok": True}
