from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3



Base = declarative_base()
# Connecting to SQLite and creating tables
engine = create_engine('sqlite:///temperature_sensors.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class SensorBase(Base):
    __tablename__ = 'sensorbase'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    operating_temp_range = Column(String)
    accuracy = Column(Float)
    type = Column(String)

    rtd = relationship("RTD", uselist=False, back_populates="sensor")
    thermocouple = relationship("Thermocouple", uselist=False, back_populates="sensor")
    thermistor = relationship("Thermistor", uselist=False, back_populates="sensor")
    semiconductor = relationship("Semiconductor", uselist=False, back_populates="sensor")
    ir = relationship("IR", uselist=False, back_populates="sensor")
    bimetallic = relationship("Bimetallic", uselist=False, back_populates="sensor")
    fiber_optic = relationship("FiberOptic", uselist=False, back_populates="sensor")
    digital = relationship("Digital", uselist=False, back_populates="sensor")
    
class RTD(Base):
    __tablename__ = 'rtd'
    id = Column(Integer, primary_key=True)
    nominal_resistance = Column(Float)
    coefficient = Column(Float)
    sensor_id = Column(Integer, ForeignKey('sensorbase.id'))
    sensor = relationship("SensorBase", back_populates="rtd")

class Thermocouple(Base):
    __tablename__ = 'thermocouple'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    seebeck_coefficient = Column(Float)
    sensor_id = Column(Integer, ForeignKey('sensorbase.id'))
    sensor = relationship("SensorBase", back_populates="thermocouple")

class Thermistor(Base):
    __tablename__ = 'thermistor'
    id = Column(Integer, primary_key=True)
    resistance_at_25C = Column(Float)
    beta_value = Column(Float)
    sensor_type = Column(String)  # NTC or PTC
    sensor_id = Column(Integer, ForeignKey('sensorbase.id'))
    sensor = relationship("SensorBase", back_populates="thermistor")

class Semiconductor(Base):
    __tablename__ = 'semiconductor'
    id = Column(Integer, primary_key=True)
    output_type = Column(String)  # Analog, Digital
    interface = Column(String)  # I2C, SPI
    sensor_id = Column(Integer, ForeignKey('sensorbase.id'))
    sensor = relationship("SensorBase", back_populates="semiconductor")

class IR(Base):
    __tablename__ = 'ir'
    id = Column(Integer, primary_key=True)
    field_of_view = Column(String)  # 90°
    wavelength_range = Column(String)
    sensor_id = Column(Integer, ForeignKey('sensorbase.id'))
    sensor = relationship("SensorBase", back_populates="ir")

class Bimetallic(Base):
    __tablename__ = 'bimetallic'
    id = Column(Integer, primary_key=True)
    material_types = Column(String)  # copper & iron
    switch_point_temperature = Column(Float)
    sensor_id = Column(Integer, ForeignKey('sensorbase.id'))
    sensor = relationship("SensorBase", back_populates="bimetallic")

class FiberOptic(Base):
    __tablename__ = 'fiber_optic'
    id = Column(Integer, primary_key=True)
    fiber_type = Column(String)  # single-mode, multi-mode
    wavelength = Column(Float)
    sensor_id = Column(Integer, ForeignKey('sensorbase.id'))
    sensor = relationship("SensorBase", back_populates="fiber_optic")

class Digital(Base):
    __tablename__ = 'digital'
    id = Column(Integer, primary_key=True)
    interface = Column(String)  # I2C, SPI
    resolution = Column(String)  # 12-bit
    sensor_id = Column(Integer, ForeignKey('sensorbase.id'))
    sensor = relationship("SensorBase", back_populates="digital")

def add_sensor(sensor_data):
        try:
            sensor_data = sensor_data.collect_sensor_data()
            if sensor_data.validate_sensor_data(sensor_data):
                # Create a sensor object based on the sensor type and add it to the database
                sensor = SensorBase(**sensor_data)
                session = Session()
                session.add(sensor)
                session.commit()
                messagebox.showinfo("Success", "Sensor added successfully!")
            else:
                messagebox.showwarning("Validation Error", "Invalid sensor data. Please check the input fields.")
        except Exception as e:  # Catching a general exception
            messagebox.showerror("Database Error", f"An error occurred while adding the sensor: {e}")


def update_sensor(sensor_data):
        try:
            sensor_data = sensor_data.collect_sensor_data()
            sensor_id = int(sensor_data['Sensor ID'])
            session = Session()
            sensor = session.query(SensorBase).filter_by(id=sensor_id).first()
            if sensor:
                # Update common attributes
                sensor.name = sensor_data['Sensor Name']
                sensor.description = sensor_data['Description']
                sensor.operating_temp_range = sensor_data['Operating Temperature Range']
                sensor.accuracy = float(sensor_data['Accuracy'])
                sensor_type = sensor_data['Sensor Type']

                # Update or create specific sensor attributes based on type
                if sensor_type == "RTD":
                    rtd_data = {
                        'nominal_resistance': float(sensor_data['Nominal Resistance (e.g., 100 ohms at 0°C)']),
                        'coefficient': float(sensor_data['Coefficient (e.g., 0.00385)'])
                    }
                    if sensor.rtd:
                        sensor.rtd.nominal_resistance = rtd_data['nominal_resistance']
                        sensor.rtd.coefficient = rtd_data['coefficient']
                    else:
                        sensor.rtd = RTD(**rtd_data)
                elif sensor_type == "Thermocouple":
                    thermocouple_data = {
                        'type': sensor_data['Type (J, K, E, T, N, B, R, S, etc.)'],
                        'seebeck_coefficient': float(sensor_data['Seebeck Coefficient (μV/°C)'])
                    }
                    if sensor.thermocouple:
                        sensor.thermocouple.type = thermocouple_data['type']
                        sensor.thermocouple.seebeck_coefficient = thermocouple_data['seebeck_coefficient']
                    else:
                        sensor.thermocouple = Thermocouple(**thermocouple_data)
                elif sensor_type == "Thermistor":
                    thermistor_data = {
                        'resistance_at_25C': float(sensor_data['Resistance at 25°C (e.g., 10k ohms)']),
                        'beta_value': float(sensor_data['Beta Value']),
                        'sensor_type': sensor_data['Type (NTC or PTC)']
                    }
                    if sensor.thermistor:
                        sensor.thermistor.resistance_at_25C = thermistor_data['resistance_at_25C']
                        sensor.thermistor.beta_value = thermistor_data['beta_value']
                        sensor.thermistor.sensor_type = thermistor_data['sensor_type']
                    else:
                        sensor.thermistor = Thermistor(**thermistor_data)

                elif sensor_type == "Semiconductor":  # Use title case
                    semiconductor_data = {
                        'output_type': sensor_data['Output Type (e.g., Analog, Digital)'],
                        'interface': sensor_data['Interface (e.g., I2C, SPI)']
                    }
                    if sensor.semiconductor:
                        sensor.semiconductor.output_type = semiconductor_data['output_type']
                        sensor.semiconductor.interface = semiconductor_data['interface']
                    else:
                        sensor.semiconductor = Semiconductor(**semiconductor_data)
  
                elif sensor_type == "IR":
                    ir_data = {
                        'field_of_view': sensor_data['Field of View (e.g., 90°)'],
                        'wavelength_range': sensor_data['Wavelength Range']
                    }
                    if sensor.ir:
                        sensor.ir.field_of_view = ir_data['field_of_view']
                        sensor.ir.wavelength_range = ir_data['wavelength_range']
                    else:
                        sensor.ir = IR(**ir_data)

                elif sensor_type == "Bimetallic":
                    bimetallic_data = {
                        'material_types': sensor_data['Material Types (e.g., copper & iron)'],
                        'switch_point_temperature': float(sensor_data['Switch Point Temperature'])
                    }
                    if sensor.bimetallic:
                        sensor.bimetallic.material_types = bimetallic_data['material_types']
                        sensor.bimetallic.switch_point_temperature = bimetallic_data['switch_point_temperature']
                    else:
                        sensor.bimetallic = Bimetallic(**bimetallic_data)

                elif sensor_type == "Fiber Optic":
                    fiber_optic_data = {
                        'fiber_type': sensor_data['Fiber Type (e.g., single-mode, multi-mode)'],
                        'wavelength': float(sensor_data['Wavelength'])
                    }
                    if sensor.fiber_optic:
                        sensor.fiber_optic.fiber_type = fiber_optic_data['fiber_type']
                        sensor.fiber_optic.wavelength = fiber_optic_data['wavelength']
                    else:
                        sensor.fiber_optic = FiberOptic(**fiber_optic_data)

                elif sensor_type == "Digital":
                    digital_data = {
                        'interface': sensor_data['Interface (e.g., I2C, SPI)'],
                        'resolution': sensor_data['Resolution (e.g., 12-bit)']
                    }
                    if sensor.digital:
                        sensor.digital.interface = digital_data['interface']
                        sensor.digital.resolution = digital_data['resolution']
                    else:
                        sensor.digital = Digital(**digital_data)

                # Commit the changes
                session.commit()
                messagebox.showinfo("Success", "Sensor updated successfully!")
            else:
                messagebox.showwarning("Error", "Sensor not found.")
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred while updating the sensor: {e}")

def delete_selected_sensor(sensor_id):
        selected_sensor = sensor_id.sensor_listbox.get(sensor_id.sensor_listbox.curselection())
        sensor_id = int(selected_sensor.split(":")[0])
        session = Session()
        sensor = session.query(SensorBase).filter_by(id=sensor_id).first()
        if sensor:
            session.delete(sensor)
            session.commit()
            messagebox.showinfo("Success", "Sensor deleted successfully!")
            sensor_id.populate_sensor_listbox()  # Refresh the listbox
        else:
            messagebox.showwarning("Error", "Sensor not found.")