from sqlalchemy.orm import Session
import models
import schema


def post_item(db: Session, trading_data: schema.TradingData):
    if trading_data.userID is None:
        trading_data.userID = 1

    trading_item = models.TradingItem(id=trading_data.id,
                                      symbol=trading_data.symbol,
                                      amount=trading_data.amount,
                                      userID=trading_data.userID)

    db.add(trading_item)
    db.commit()
    db.refresh(trading_item)
    return trading_item


def read_item(db: Session, symbol: str):
    return db.query(models.TradingItem).filter(models.TradingItem.symbol == symbol).all()


