import enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr

Base = declarative_base()


class Resource(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)


class LeadType(enum.Enum):
    CAR = "car"
    HOUSE = ("house",)
    PAYROLL = "payroll"


class LeadStatus(enum.Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Lead(Resource):
    __tablename__ = "lead"
    type = Column(Enum(LeadType, default=LeadType.CAR, nullable=False))
    status = Column(Enum(LeadStatus, default=LeadStatus.NEW, nullable=False))
    name = Column(String())
    telephone = Column(String())
    email = Column(String())
    rfc = Column(String())
    address = Column(String())


class LeadAware(Base):
    __abstract__ = True
    @declared_attr
    def lead_id(self):
        return Column(Integer, ForeignKey("lead.id"))
    
class LeadAuto(Resource, LeadAware):
    __tablename__ = "lead_auto"
    model = Column(String())
    price = Column(Float())


class LeadHouse(Resource, LeadAware):
    __tablename__ = "lead_house"
    address = Column(String())
    price = Column(Float())


class LeadPayroll(Resource, LeadAware):
    __tablename__ = "lead_payroll"
    company = Column(String())
    admission_at = Column(DateTime())
