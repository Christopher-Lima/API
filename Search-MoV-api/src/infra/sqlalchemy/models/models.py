import datetime
from sqlalchemy import Column, Boolean, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import SQLALCHEMY_DATABASE_URL, Base


################################

## Hack UUID
from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects.postgresql import UUID
import uuid

### URL: https://gist.github.com/gmolveau/7caeeefe637679005a7bb9ae1b5e421e?permalink_comment_id=3988721

class GUID(TypeDecorator):
    """Platform-independent GUID type.
    Uses PostgreSQL's UUID type, otherwise uses
    CHAR(32), storing as stringified hex values.
    """
    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return "%.32x" % uuid.UUID(value).int
            else:
                # hexstring
                return "%.32x" % value.int

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            if not isinstance(value, uuid.UUID):
                value = uuid.UUID(value)
            return value

################################

## Modelo de Usuário
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    uuid = Column(String, GUID(), default=lambda: str(uuid.uuid4()), unique=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(90))
    age = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    gender = Column(String(1), nullable=False)
    cpf_cnpj = Column(String(14), unique=True)
    phone = Column(String(11))
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(16), nullable=False)
    
   ## Relacionamentos
    house = relationship("House", back_populates="owner")
    announcement = relationship("Announcement", back_populates="owner")
    evaluation = relationship("Evaluation", back_populates="owner")
    
## Modelo de Imóvel
class House(Base):
    __tablename__ = 'houses'
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    uuid = Column(String, GUID(), default=lambda: str(uuid.uuid4()), unique=True)
    type = Column(String(20))
    size = Column(String(10))
    bedroom = Column(Integer, nullable=False)
    restroom = Column(Integer, nullable=False)
    furniture = Column(Boolean, default=False)
    cep = Column(String(8), nullable=False)
    state = Column(String(20))
    city = Column(String(20))
    district = Column(String(20))
    number = Column(String(8))
    reference = Column(String(100))    
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    #Relacionamentos
    owner = relationship("User", back_populates="house")
    announcement = relationship("Announcement", back_populates="house", uselist=False)

## Modelo de Anúncio    
class Announcement(Base):
    __tablename__ = 'announcements'
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    uuid = Column(String, GUID(), default=lambda: str(uuid.uuid4()), nullable=False, unique=True)
    name = Column(String(60))
    type = Column(String)
    rent_period = Column(String(20))
    available = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    house_id = Column(Integer, ForeignKey("houses.id"), nullable=False)

    ## Relacionamentos
    owner = relationship("User", back_populates="announcement")
    evaluation = relationship("Evaluation", back_populates="announcement")
    house = relationship("House", back_populates="announcement")

## Modelo para avaliações    
class Evaluation(Base):
    __tablename__ = 'evaluations'
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    uuid = Column(String, GUID(), default=lambda: str(uuid.uuid4()), nullable=False, unique=True)
    comment = Column(String(500))
    rating = Column(Float)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    announcement_id = Column(Integer, ForeignKey("announcements.id"), nullable=False)
    
    ## Relacionamentos
    owner = relationship("User", back_populates="evaluation")    
    announcement = relationship("Announcement", back_populates="evaluation")