from sqlalchemy import Column, String, Float, DateTime, CheckConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Prices(Base):
    __tablename__ = 'pycon_prices'
    __table_args__ = (UniqueConstraint('date', 'equity_id', 'mic', name='unique_date_equity_id_market'),)

    date = Column(DateTime, primary_key=True)
    equity_id = Column(String(32), primary_key=True)
    mic = Column(String(32), nullable=True)
    #market = Column(String(32), nullable=True)
    price = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)
