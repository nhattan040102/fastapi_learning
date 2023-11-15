from typing import Union

from fastapi import FastAPI
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
import schema
import crud
from database import SessionLocal, postgres_engine

models.Base.metadata.create_all(bind=postgres_engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/trading_data")
def post_item(trading_data: schema.TradingData, db: Session = Depends(get_db)):
    try:
        item = crud.post_item(db, trading_data)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing the request: {str(e)}",
        )

    return {"Trading data has been uploaded successfully": item}




@app.get("/trading_data")
def read_item(symbol: str, db: Session = Depends(get_db)):
    item = crud.read_item(db, symbol)

    return {"data": item}



