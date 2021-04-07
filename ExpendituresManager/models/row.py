from sqlalchemy import Column, Integer, Date, String, Float


def create_models(base, tablename):
    Base = base

    class Row(Base):
        __tablename__ = tablename

        expenditure_id = Column(Integer, primary_key=True, autoincrement=True)
        date = Column(Date)
        shop = Column(String)
        description = Column(String)
        event = Column(String)
        cost = Column(Float)
        expenditure_type = Column(String)

        def __init__(self, **kwargs):
            self.date = kwargs.get("date")
            self.shop = kwargs.get("shop")
            self.description = kwargs.get("description")
            self.event = kwargs.get("event")
            self.cost = kwargs.get("cost")
            self.expenditure_type = kwargs.get("expenditure_type")
    return Row
