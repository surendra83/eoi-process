from sqlalchemy import Column, Date, Integer, String

from database.base import Base


class UldSubgroups(Base):
    __tablename__ = "ULD_SUBGROUPS"

    TS_ID = Column(Integer, primary_key=True)
    TS_LINK_TO_SOLD_CASE = Column(Integer)
    TS_ISSUEID = Column(String)
    TS_SUBGROUP_NAME = Column(String)
    TS_SUBGROUP_NUMBER = Column(String)
    TS_TERMINATION_DATE = Column(Date)
    TS_EFFECTIVE_DATE = Column(Date)
    TS_NAME_CON1 = Column(String)
    TS_TYPE_CON1 = Column(String)
    TS_EMAIL_CON1 = Column(String)
    TS_ADDRESS_CON1 = Column(String)
    TS_NAME_CON2 = Column(String)
    TS_TYPE_CON2 = Column(String)
    TS_EMAIL_CON2 = Column(String)
    TS_ADDRESS_CON2 = Column(String)
    TS_COMMENTS_SUBGROUP = Column(String)
    TS_LASTMODIFIER = Column(String)