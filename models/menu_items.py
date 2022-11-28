from Cafe_Project.core.db_manager import Base, session, engine
from sqlalchemy import Column, Integer, String, Date, Float


class MenuItems(Base):
    __tablename__ = 'menu_items'
    id = Column('menu_id', Integer, primary_key=True)
    name = Column(String(30))
    price = Column(Float)
    category = Column(String(30))
    imgpath = Column(String)


# Base.metadata.create_all(engine)
# session.commit()
