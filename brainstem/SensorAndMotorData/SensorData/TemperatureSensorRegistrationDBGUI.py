from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


Base = declarative_base()

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
    semiconductors = relationship("Semiconductors", uselist=False, back_populates="sensor")
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

class Semiconductors(Base):
    __tablename__ = 'semiconductors'
    id = Column(Integer, primary_key=True)
    output_type = Column(String)  # Analog, Digital
    interface = Column(String)  # I2C, SPI
    sensor_id = Column(Integer, ForeignKey('sensorbase.id'))
    sensor = relationship("SensorBase", back_populates="semiconductors")

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
    __tablename__ = 'fiberoptic'
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

# Connecting to SQLite and creating tables
engine = create_engine('sqlite:///sensors.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class SensorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sensor Registration")

        self.sensor_type_label = ttk.Label(self, text="Sensor Type:")
        self.sensor_type_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        self.sensor_types = ["Select", "RTD", "Thermocouple", "Thermistor", "Semiconductor", "Bimetallic", "IR", "Fiber Optic", "Digital"]
        self.sensor_type_var = tk.StringVar()
        self.sensor_type_dropdown = ttk.Combobox(self, textvariable=self.sensor_type_var, values=self.sensor_types)
        self.sensor_type_dropdown.grid(row=0, column=1, padx=10, pady=5)
        self.sensor_type_dropdown.bind("<<ComboboxSelected>>", self.show_fields_based_on_selection)

        self.field_widgets = {}
        self.create_common_fields()

        self.add_button = ttk.Button(self, text="Add Sensor", command=self.add_sensor)
        self.add_button.grid(row=9, column=0, columnspan=2, pady=5)

        self.update_button = ttk.Button(self, text="Update Sensor", command=self.update_sensor)
        self.update_button.grid(row=10, column=0, columnspan=2, pady=5)

        self.delete_button = ttk.Button(self, text="Delete Sensor", command=self.delete_sensor)
        self.delete_button.grid(row=11, column=0, columnspan=2, pady=5)

    def create_common_fields(self):
        self.create_field("Sensor ID", row=1)
        self.create_field("Sensor Name", row=2)
        self.create_field("Description", row=3)
        self.create_field("Operating Temperature Range", row=4)
        self.create_field("Accuracy", row=5)

    def create_field(self, label_text, row):
        label = ttk.Label(self, text=label_text + ":")
        label.grid(row=row, column=0, sticky=tk.W, padx=10, pady=5)
        entry_var = tk.StringVar()
        entry = ttk.Entry(self, textvariable=entry_var)
        entry.grid(row=row, column=1, padx=10, pady=5)
        self.field_widgets[label_text] = entry_var

    def show_fields_based_on_selection(self, event):
         sensor_type = self.sensor_type_var.get()
         self.clear_specific_fields()
         self.show_specific_fields(sensor_type)

    def clear_specific_fields(self):
        for widget in self.field_widgets.values():
            widget.set("")
        for widget in self.grid_slaves():
            if int(widget.grid_info()["row"]) > 5:
                widget.grid_forget()
        self.field_widgets = {k: v for k, v in self.field_widgets.items() if int(v._tk.eval(f'grid_info({v._name})["row"]')) <= 5}

    def show_specific_fields(self, sensor_type=None):
        # Remove existing specific fields
        self.clear_specific_fields()
        if sensor_type is None:
            sensor_type = self.sensor_type_var.get()

        # Create specific fields based on sensor type
        specific_fields = {
            "RTD": [("Nominal Resistance (e.g., 100 ohms at 0°C)", 6), ("Coefficient (e.g., 0.00385)", 7)],
            "Thermocouple": [("Type (J, K, E, T, N, B, R, S, etc.)", 6), ("Seebeck Coefficient (μV/°C)", 7)],
            "Thermistor": [("Resistance at 25°C (e.g., 10k ohms)", 6), ("Beta Value", 7), ("Type (NTC or PTC)", 8)],
            "Semiconductor": [("Output Type (e.g., Analog, Digital)", 6), ("Interface (e.g., I2C, SPI)", 7)],
            "Bimetallic": [("Material Types (e.g., copper & iron)", 6), ("Switch Point Temperature", 7)],
            "IR": [("Field of View (e.g., 90°)", 6), ("Wavelength Range", 7)],
            "Fiber Optic": [("Fiber Type (e.g., single-mode, multi-mode)", 6), ("Wavelength", 7)],
            "Digital": [("Interface (e.g., I2C, SPI)", 6), ("Resolution (e.g., 12-bit)", 7)],
        }

        for label_text, row in specific_fields.get(sensor_type, []):
            self.create_field(label_text, row)


    def add_sensor(self):
        try:
            sensor_data = self.collect_sensor_data()
            if self.validate_sensor_data(sensor_data):
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


def update_sensor_in_db(sensor_data):
    conn = sqlite3.connect('sensors.db')
    cursor = conn.cursor()
    sensor_id = sensor_data['Sensor ID']
    update_values = ', '.join(f"{key} = ?" for key in sensor_data.keys() if key != 'Sensor ID')
    query = f'UPDATE sensors SET {update_values} WHERE Sensor_ID = ?'
    cursor.execute(query, list(sensor_data.values()) + [sensor_id])
    conn.commit()
    conn.close()

def delete_sensor_from_db(sensor_id):
    conn = sqlite3.connect('sensors.db')
    cursor = conn.cursor()
    query = 'DELETE FROM sensors WHERE Sensor_ID = ?'
    cursor.execute(query, (sensor_id,))
    conn.commit()
    conn.close()

    def collect_sensor_data(self):
        sensor_data = {}
        for key, value in self.field_widgets.items():
            sensor_data[key] = value.get()
        return sensor_data

    def validate_sensor_data(self, sensor_data):
        sensor_type = sensor_data['Sensor Type']
        if sensor_type == 'RTD':
            return self.validate_rtd_data(sensor_data)
        elif sensor_type == 'Thermocouple':
            return self.validate_thermocouple_data(sensor_data)
        elif sensor_type == 'Thermistor':
            return self.validate_thermistor_data(sensor_data)
        elif sensor_type == 'Semiconductors':
            return self.validate_semiconductors_data(sensor_data)
        elif sensor_type == 'IR':
            return self.validate_ir_data(sensor_data)
        elif sensor_type == 'Bimetallic':
            return self.validate_bimetallic_data(sensor_data)
        elif sensor_type == 'Fiber Optic':
            return self.validate_fiber_optic_data(sensor_data)
        elif sensor_type == 'Digital':
            return self.validate_digital_data(sensor_data)
        else:
            return False

    def validate_rtd_data(self, sensor_data):
        nominal_resistance = float(sensor_data['Nominal Resistance'])
        coefficient = float(sensor_data['Coefficient'])
        return 0 < nominal_resistance <= 1000 and 0 < coefficient <= 1

    def validate_thermocouple_data(self, sensor_data):
        valid_types = ['J', 'K', 'E', 'T', 'N', 'B', 'R', 'S']
        thermocouple_type = sensor_data['Type']
        seebeck_coefficient = float(sensor_data['Seebeck Coefficient'])
        return thermocouple_type in valid_types and 0 < seebeck_coefficient <= 100

    def validate_thermistor_data(self, sensor_data):
        resistance_at_25C = float(sensor_data['Resistance at 25°C'])
        beta_coefficient = float(sensor_data['Beta Value'])
        return 0 < resistance_at_25C <= 10000 and 0 < beta_coefficient <= 10000

    def validate_semiconductors_data(self, sensor_data):
        voltage_output = float(sensor_data['Voltage Output'])
        return 0 < voltage_output <= 10

    def validate_ir_data(self, sensor_data):
        wavelength_range = sensor_data['Wavelength Range']
        return True

    def validate_bimetallic_data(self, sensor_data):
        material_type = sensor_data['Material Type']
        return True

    def validate_fiber_optic_data(self, sensor_data):
        fiber_type = sensor_data['Fiber Type']
        wavelength = float(sensor_data['Wavelength'])
        return fiber_type in ['single-mode', 'multi-mode'] and 0 < wavelength <= 1000

    def validate_digital_data(self, sensor_data):
        interface = sensor_data['Interface']
        resolution = int(sensor_data['Resolution'])
        return interface in ['I2C', 'SPI'] and 8 <= resolution <= 16


if __name__ == "__main__":
    app = SensorApp()
    app.mainloop()
