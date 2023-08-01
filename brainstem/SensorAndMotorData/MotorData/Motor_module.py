from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class MotorType(Base):
    __tablename__ = 'motor_types'

    type_id = Column(Integer, primary_key=True)
    type_name = Column(String, unique=True)
    description = Column(Text)

class BrushType(Base):
    __tablename__ = 'brush_types'

    brush_id = Column(Integer, primary_key=True)
    brush_name = Column(String, unique=True)  # Brushed, Brushless
    description = Column(Text)

class Motor(Base):
    __tablename__ = 'motors'

    motor_id = Column(Integer, primary_key=True)
    type_id = Column(Integer, ForeignKey('motor_types.type_id'))
    brush_id = Column(Integer, ForeignKey('brush_types.brush_id'))
    
    motor_name = Column(String)
    rpm = Column(Integer)
    gear_reduction = Column(String)
    resistance = Column(Float)
    torque = Column(Float)
    voltage = Column(Float)
    current = Column(Float)
    encoder_ratio = Column(String)
    safe_temperature = Column(Float)
    warning_temperature = Column(Float)
    red_flag_temperature = Column(Float)
    description = Column(Text)

    motor_type = relationship("MotorType")
    brush_type = relationship("BrushType")

# Setting up the SQLite database
engine = create_engine('sqlite:///motors.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Demonstration: Adding a motor type, brush type, and motor to the database
motor_type = MotorType(type_name="DC", description="Direct Current Motor")
brush_type = BrushType(brush_name="Brushed", description="Motor with brushes")

motor = Motor(
    motor_name="Test Motor",
    rpm=5000,
    gear_reduction="1:10",
    resistance=0.5,
    torque=10.0,
    voltage=12.0,
    current=1.5,
    encoder_ratio="10:1",
    safe_temperature=60.0,
    warning_temperature=80.0,
    red_flag_temperature=100.0,
    description="Test motor for demonstration",
    motor_type=motor_type,
    brush_type=brush_type
)

session.add(motor)
session.commit()

