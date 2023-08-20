from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class LinkedHardware(Base):
    __tablename__ = "linked_hardware"
    id = Column(Integer, primary_key=True)
    motor_id = Column(Integer)
    sensor_id = Column(Integer)
    relationship = Column(String)

DATABASE_URL = "sqlite:///linked_hardware.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

class LinkedDatabase:
    def __init__(self):
        self.session = SessionLocal()

    def link_hardware(self, motor_id, sensor_id, relationship):
        link = LinkedHardware(motor_id=motor_id, sensor_id=sensor_id, relationship=relationship)
        self.session.add(link)
        self.session.commit()

    def unlink_hardware(self, link_id):
        link = self.session.query(LinkedHardware).filter(LinkedHardware.id == link_id).first()
        self.session.delete(link)
        self.session.commit()

    def get_all_links(self):
        return self.session.query(LinkedHardware).all()

