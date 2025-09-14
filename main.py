from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from typing import List

from database import create_db_and_tables, get_session
from schema import Stock

app = FastAPI(title="Stock CRUD API")


# 👇 Add your frontend URL here
origins = [
    "http://localhost:3000",   # React dev server
    "http://127.0.0.1:3000",
    "https://stock-fronted.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Allowed origins
    allow_credentials=True,
    allow_methods=["*"],            # GET, POST, PUT, DELETE etc.
    allow_headers=["*"],            # Allow all headers
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# 🔹 Create a stock
@app.post("/stocks", response_model=Stock)
def stock(stock: Stock, session: Session = Depends(get_session)):
    session.add(stock)
    session.commit()
    session.refresh(stock)
    return stock


# 🔹 Get stocks with pagination
# @app.get("/stocks", response_model=List[Stock])
# def get_stocks(
#     skip: int = Query(0, ge=0),
#     limit: int = Query(10, ge=1),
#     trade_code: str | None = Query(None),
#     session: Session = Depends(get_session),
# ):
#     statement = select(Stock)
#     if trade_code:  # apply filter if provided
#         statement = statement.where(Stock.trade_code == trade_code)

#     statement = statement.offset(skip).limit(limit)
#     results = session.exec(statement).all()
#     return results


@app.get("/stocks", response_model=List[Stock])
def get_stocks(
    last_id: int | None = Query(None, ge=0),
    limit: int = Query(100, ge=1),
    trade_code: str | None = Query(None),
    session: Session = Depends(get_session),
):
    statement = select(Stock)

    if trade_code and trade_code != "all":  # <-- important
        statement = statement.where(Stock.trade_code == trade_code)

    if last_id:
        statement = statement.where(Stock.id > last_id)

    statement = statement.order_by(Stock.id).limit(limit)
    results = session.exec(statement).all()
    print('results',results)
    return results



@app.get("/stocks/trade-codes", response_model=list[str])
def get_trade_codes(session: Session = Depends(get_session)):
    # Distinct trade codes from DB
    results = session.exec(select(Stock.trade_code).distinct()).all()
    return results


# 🔹 Get stock by ID
@app.get("/stocks/{stock_id}", response_model=Stock)
def get_stock(stock_id: int, session: Session = Depends(get_session)):
    stock = session.get(Stock, stock_id)
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock


# 🔹 Update stock
@app.put("/stocks/{stock_id}", response_model=Stock)
def update_stock(stock_id: int, updated_stock: Stock, session: Session = Depends(get_session)):
    stock = session.get(Stock, stock_id)
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")

    stock.date = updated_stock.date
    stock.trade_code = updated_stock.trade_code
    stock.high = updated_stock.high
    stock.low = updated_stock.low
    stock.open = updated_stock.open
    stock.close = updated_stock.close
    stock.volume = updated_stock.volume

    session.add(stock)
    session.commit()
    session.refresh(stock)
    return stock


# 🔹 Delete stock
@app.delete("/stocks/{stock_id}")
def delete_stock(stock_id: int, session: Session = Depends(get_session)):
    stock = session.get(Stock, stock_id)
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")

    session.delete(stock)
    session.commit()
    return {"ok": True}



