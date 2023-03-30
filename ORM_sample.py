
from sqlalchemy import create_engine
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Numeric, Integer, Date, Text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import select

from datetime import date

class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = "employees" # name of table in SQL database

    employeeNumber: Mapped[int] = mapped_column(primary_key = True)      
    lastName: Mapped[str] = mapped_column(String(50))
    firstName: Mapped[str] = mapped_column(String(50))
    extension: Mapped[str] = mapped_column(String(10))
    email: Mapped[str] = mapped_column(String(100))
    officeCode: Mapped[str] = mapped_column(String(10))
    reportsTo: Mapped [int] = mapped_column(Integer) 
    jobTitle: Mapped[str] = mapped_column(String(50))
    customers: Mapped[List["Customer"]] = relationship(back_populates = "representative", 
                                                       cascade="all, delete-orphan")


    def __repr__(self):
        return f"Employee {self.employeeNumber} is named {self.firstName} {self.lastName}, contact him in {self.email}"


class Customer(Base):
    __tablename__ = "customers"

    customerNumber: Mapped[int] = mapped_column(primary_key = True)
    customerName: Mapped[str] = mapped_column(String(50)) 
    contactLastName: Mapped[str] = mapped_column(String(50)) 
    contactFirstName: Mapped[str] = mapped_column(String(50)) 
    phone: Mapped[str] = mapped_column(String(50))
    addressLine1: Mapped[str] = mapped_column(String(50)) 
    addressLine2: Mapped[str] = mapped_column(String(50))
    city: Mapped[str] = mapped_column(String(50))
    state: Mapped[str] = mapped_column(String(50))
    postalCode: Mapped[str] = mapped_column(String(15))
    country: Mapped[str] = mapped_column(String(50))    
    salesRepEmployeeNumber: Mapped[int] = mapped_column(ForeignKey(Employee.employeeNumber)) 
    creditLimit: Mapped[float] = mapped_column(Numeric(10,3)) 
    orders: Mapped[List["Order"]] = relationship(back_populates = "customer", cascade="all, delete-orphan")
    representative: Mapped["Employee"] = relationship(back_populates = "customers")

    def __repr__(self):
        return f"Customer {self.customerName} is owned by {self.contactFirstName} {self.contactLastName}"

class Order(Base):
    __tablename__ = "orders"

    orderNumber: Mapped[int] = mapped_column(primary_key = True)  
    orderDate: Mapped[date] = mapped_column(Date) 
    requiredDate: Mapped[date] = mapped_column(Date)  
    shippedDate: Mapped[date] = mapped_column(Date)  
    status: Mapped[str] = mapped_column(String(50))
    comments: Mapped[str] = mapped_column(Text)
    customerNumber: Mapped[int] = mapped_column(ForeignKey(Customer.customerNumber))
    customer: Mapped["Customer"] = relationship(back_populates = "orders")

    def __repr__(self):
        return f"Order {self.orderNumber} to customer {self.customerNumber}"

engine = create_engine("mysql+pymysql://root:Pinkbanjos5396!@localhost:3306/classicmodels", echo=True)


session = Session(engine)
#stmt = select(Customer).where(Customer.country.in_(["France"]))
#stmt = select(Customer)
#stmt = select(Employee)

stmt = select(Order).join(Order.customer).where(Customer.country == "France")

for user in session.scalars(stmt):
    print(user)


