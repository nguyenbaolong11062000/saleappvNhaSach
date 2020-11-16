from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from saleapp import db
from flask_login import UserMixin


class SaleBase(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class Category(SaleBase):
    __tablename__ = 'category'

    products = relationship('Product',
                            backref='category', lazy=True)


class Product(SaleBase):
    __tablename__ = 'product'

    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id),
                         nullable=False)

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)

    def __str__(self):
        return self.name

class InfoUser(SaleBase):
    __tablename__ = 'infouser'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
    password = Column(String(100), nullable=False)
    def __str__(self):
        return self.name

if __name__ == '__main__':
    db.create_all()