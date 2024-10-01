from sqlalchemy import Column, String, Integer, Float
from app.db.dbconnect import Base


class InventorySchema(Base):
    __tablename__ = "Inventory"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_number = Column(String, nullable=False)
    material = Column(String, nullable=False)
    form = Column(String, nullable=False)
    choice = Column(String, nullable=False)
    grade = Column(String, nullable=False)
    finish = Column(String, nullable=False)
    surface = Column(String, nullable=True)
    quantity = Column(Integer, nullable=True)
    weight = Column(Float, nullable=False)
    length = Column(Float, nullable=True)
    width = Column(Float, nullable=True)
    height = Column(Float, nullable=True)
    thickness = Column(Float, nullable=True)
    outer_diameter = Column(Float, nullable=True)
    wall_thickness = Column(Float, nullable=True)
    web_thickness = Column(Float, nullable=True)
    flange_thickness = Column(Float, nullable=True)
    certificates = Column(String, nullable=True)
    location = Column(String, nullable=False)


class PreferenceSchema(Base):
    __tablename__ = "Preference"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    material = Column(String, nullable=False)
    form = Column(String, nullable=False)
    grade = Column(String, nullable=True)
    choice = Column(String, nullable=True)
    min_width = Column(Float, nullable=True)
    max_width = Column(Float, nullable=True)
    min_thickness = Column(Float, nullable=True)
    max_thickness = Column(Float, nullable=True)
