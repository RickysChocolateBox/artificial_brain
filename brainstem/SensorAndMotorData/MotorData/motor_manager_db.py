from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Setup
Base = declarative_base()

class Motor(Base):
    __tablename__ = "motors"
    id = Column(Integer, primary_key=True)
    motor_type = Column(String)
    brush_type = Column(String)
    motor_name = Column(String)
    rpm = Column(Integer)
    gear_reduction = Column(Float)
    resistance = Column(Float)
    torque = Column(Float)
    voltage = Column(Float)
    current = Column(Float)
    encoder_ratio = Column(Float)
    safe_temperature = Column(Float)
    warning_temperature = Column(Float)
    red_flag_temperature = Column(Float)
    description = Column(String)

DATABASE_URL = "sqlite:///motors.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

class MotorDatabase:
    def __init__(self):
        self.session = SessionLocal()

    def add_motor(self, motor_data):
        new_motor = Motor(**motor_data)
        self.session.add(new_motor)
        self.session.commit()

    def update_motor(self, motor_id, updated_data):
        motor = self.session.query(Motor).filter(Motor.id == motor_id).first()
        for key, value in updated_data.items():
            setattr(motor, key, value)
        self.session.commit()

    def delete_motor(self, motor_id):
        motor = self.session.query(Motor).filter(Motor.id == motor_id).first()
        self.session.delete(motor)
        self.session.commit()

    def get_all_motors(self):
        return self.session.query(Motor).all()

    def get_motor_by_index(self, index):
        return self.session.query(Motor).all()[index]

    def get_motor_by_id(self, motor_id):
        return self.session.query(Motor).filter(Motor.id == motor_id).first()
