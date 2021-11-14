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
    AUTO = "AUTO"
    HOUSE = "HOUSE"
    PAYROLL = "PAYROLL"


class LeadStatus(enum.Enum):
    NEW = "NEW"
    APROVE = "APROVE"
    REJECTED = "REJECTED"


class Lead(Resource):
    __tablename__ = "lead"
    type = Column(Enum(LeadType, default=LeadType.AUTO, nullable=False))
    status = Column(Enum(LeadStatus, default=LeadStatus.NEW, nullable=False))
    name = Column(String())
    telephone = Column(String())
    email = Column(String())
    rfc = Column(String())
    address = Column(String())
    auto = relationship("LeadAuto")
    
    def as_dict(self):
        return {
            "id": self.id,
            "type": self.type.value,
            "status": self.status.value,
            "name": self.name,
            "telephone": self.telephone,
            "email": self.email,
            "rfc": self.rfc,
            "address": self.address
        }


class LeadAware(Base):
    __abstract__ = True
    @declared_attr
    def lead_id(self):
        return Column(Integer, ForeignKey("lead.id"))
    
class LeadAuto(Resource, LeadAware):
    __tablename__ = "lead_auto"
    model = Column(String())
    price = Column(Float())
    
    def as_dict(self):
        return {
            "id": self.id,
            "model": self.model,
            "price": self.price
        }


class LeadHouse(Resource, LeadAware):
    __tablename__ = "lead_house"
    address = Column(String())
    price = Column(Float())
    
    def as_dict(self):
        return {
            "id": self.id,
            "address": self.address,
            "price": self.price
        }


class LeadPayroll(Resource, LeadAware):
    __tablename__ = "lead_payroll"
    company = Column(String())
    admission_at = Column(DateTime())
    
    def as_dict(self):
        return {
            "id": self.id,
            "company": self.company,
            "admission_at": self.admission_at
        }
