from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SkeletalPart(Base):
    __tablename__ = "skeletal_parts"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('skeletal_parts.id'), nullable=True)
    shape_type = Column(String)
    measurements = Column(String)  # Serialized JSON
    orientation = Column(String)   # Serialized JSON
    object_file_path = Column(String)
    children = relationship('SkeletalPart', backref='parent')

class LinkagePoint(Base):
    __tablename__ = "linkage_points"
    id = Column(Integer, primary_key=True)
    skeletal_part_id = Column(Integer, ForeignKey('skeletal_parts.id'))
    name = Column(String)
    coordinates = Column(String)  # Serialized JSON
    orientation = Column(String)  # Serialized JSON

class SkeletalConfiguration(Base):
    __tablename__ = "skeletal_configurations"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    parts = Column(String)  # Serialized list of SkeletalPart IDs

class SkeletalDatabase:
    def __init__(self):
        DATABASE_URL = "sqlite:///skeletal.db"
        self.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(self.engine)
        self.SessionLocal = sessionmaker(bind=self.engine)
        self.session = self.SessionLocal()

    def add_skeletal_part(self, name, parent_id, shape_type, measurements, orientation, object_file_path):
        part = SkeletalPart(name=name, parent_id=parent_id, shape_type=shape_type,
                            measurements=measurements, orientation=orientation,
                            object_file_path=object_file_path)
        self.session.add(part)
        self.session.commit()
        return part.id

    def update_skeletal_part(self, part_id, **kwargs):
        part = self.session.query(SkeletalPart).filter(SkeletalPart.id == part_id).first()
        for key, value in kwargs.items():
            setattr(part, key, value)
        self.session.commit()

    def delete_skeletal_part(self, part_id):
        part = self.session.query(SkeletalPart).filter(SkeletalPart.id == part_id).first()
        self.session.delete(part)
        self.session.commit()

    def get_all_skeletal_parts(self):
        return self.session.query(SkeletalPart).all()

    def add_linkage_point(self, skeletal_part_id, name, coordinates, orientation):
        linkage_point = LinkagePoint(skeletal_part_id=skeletal_part_id, name=name,
                                     coordinates=coordinates, orientation=orientation)
        self.session.add(linkage_point)
        self.session.commit()
        return linkage_point.id

    def update_linkage_point(self, linkage_point_id, **kwargs):
        linkage_point = self.session.query(LinkagePoint).filter(LinkagePoint.id == linkage_point_id).first()
        for key, value in kwargs.items():
            setattr(linkage_point, key, value)
        self.session.commit()

    def delete_linkage_point(self, linkage_point_id):
        linkage_point = self.session.query(LinkagePoint).filter(LinkagePoint.id == linkage_point_id).first()
        self.session.delete(linkage_point)
        self.session.commit()

    def get_all_linkage_points(self):
        return self.session.query(LinkagePoint).all()

    def add_skeletal_configuration(self, name, description, parts):
        config = SkeletalConfiguration(name=name, description=description, parts=parts)
        self.session.add(config)
        self.session.commit()
        return config.id

    def update_skeletal_configuration(self, config_id, **kwargs):
        config = self.session.query(SkeletalConfiguration).filter(SkeletalConfiguration.id == config_id).first()
        for key, value in kwargs.items():
            setattr(config, key, value)
        self.session.commit()

    def delete_skeletal_configuration(self, config_id):
        config = self.session.query(SkeletalConfiguration).filter(SkeletalConfiguration.id == config_id).first()
        self.session.delete(config)
        self.session.commit()

    def get_all_skeletal_configurations(self):
        return self.session.query(SkeletalConfiguration).all()
