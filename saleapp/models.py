from sqlalchemy import Column, Integer, String, Boolean, Enum,Float, ForeignKey
from sqlalchemy.orm import relationship
from saleapp import db
from flask_login import UserMixin
from enum import Enum as UserEnum



class SaleBase(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class Category(SaleBase):
    __tablename__ = 'category'

    products = relationship('Product',
                            backref='category', lazy=True)

class InfoSach(SaleBase):

    totalPage = Column(Integer, nullable=False)
    director = Column(String(100), nullable=False)
    edition = Column(String(200), nullable=False)
    dateofissure = Column(String(250), nullable=False)


class Product(SaleBase):
    __tablename__ = 'product'

    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id),
                         nullable=False)

class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100))
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100))
    active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.USER)


    def __str__(self):
        return self.name


if __name__ == '__main__':
    db.create_all()