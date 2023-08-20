from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from temperature_sensor_db import Session, SensorBase
from temperature_sensor_db import add_sensor as db_add_sensor
from temperature_sensor_db import update_sensor as db_update_sensor
from temperature_sensor_db import delete_selected_sensor as db_delete_selected_sensor

class SensorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sensor Registration")

        self.sensor_type_label = ttk.Label(self, text="Sensor Type:")
        self.sensor_type_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.create_sensor_listbox()
        self.sensor_types = ["Select", "RTD", "Thermocouple", "Thermistor", "Semiconductor", "Bimetallic", "IR", "Fiber Optic", "Digital"]
        self.sensor_type_var = tk.StringVar()
        self.sensor_type_dropdown = ttk.Combobox(self, textvariable=self.sensor_type_var, values=self.sensor_types)
        self.sensor_type_dropdown.grid(row=0, column=1, padx=10, pady=5)
        self.sensor_type_dropdown.bind("<<ComboboxSelected>>", self.show_fields_based_on_selection)
        self.delete_button = ttk.Button(self, text="Delete Sensor", command=self.delete_selected_sensor)
        self.delete_button.grid(row=14, column=0, columnspan=2, pady=5)
        self.field_widgets = {}
        self.create_common_fields()

        self.add_button = ttk.Button(self, text="Add Sensor", command=self.add_sensor)
        self.add_button.grid(row=9, column=0, columnspan=2, pady=5)

        self.update_button = ttk.Button(self, text="Update Sensor", command=self.update_sensor)
        self.update_button.grid(row=10, column=0, columnspan=2, pady=5)

    def create_sensor_listbox(self):
        self.sensor_listbox = tk.Listbox(self)
        self.sensor_listbox.grid(row=12, column=0, columnspan=2, padx=10, pady=5)
        self.load_sensors_button = ttk.Button(self, text="Load Sensor", command=self.load_selected_sensor)
        self.load_sensors_button.grid(row=13, column=0, columnspan=2, pady=5)
        self.populate_sensor_listbox()

    def populate_sensor_listbox(self):
        session = Session()
        sensors = session.query(SensorBase).all()
        for sensor in sensors:
            self.sensor_listbox.insert(tk.END, f"{sensor.id}: {sensor.name} ({sensor.type})")

    def load_selected_sensor(self):
        selected_sensor = self.sensor_listbox.get(self.sensor_listbox.curselection())
        sensor_id = int(selected_sensor.split(":")[0])
        session = Session()
        sensor = session.query(SensorBase).filter_by(id=sensor_id).first()
        if sensor:
            # Populate common fields
            self.field_widgets['Sensor ID'].set(sensor.id)
            self.field_widgets['Sensor Name'].set(sensor.name)
            self.field_widgets['Description'].set(sensor.description)
            self.field_widgets['Operating Temperature Range'].set(sensor.operating_temp_range)
            self.field_widgets['Accuracy'].set(sensor.accuracy)
            self.sensor_type_var.set(sensor.type)
            # Populate specific fields based on sensor type here...
        else:
            messagebox.showwarning("Error", "Sensor not found.")


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
        sensor_data = self.collect_sensor_data()
        if self.validate_sensor_data(sensor_data):
            try:
                db_add_sensor(sensor_data)
                self.populate_sensor_listbox()  # Refresh the listbox
            except Exception as e:
                messagebox.showerror("Database Error", f"An error occurred while adding the sensor: {e}")
        else:
            messagebox.showwarning("Validation Error", "Invalid sensor data. Please check the input fields.")

    def update_sensor(self):
        sensor_data = self.collect_sensor_data()
        if self.validate_sensor_data(sensor_data):
            try:
                db_update_sensor(sensor_data)
                self.populate_sensor_listbox()  # Refresh the listbox
            except Exception as e:
                messagebox.showerror("Database Error", f"An error occurred while updating the sensor: {e}")
        else:
            messagebox.showwarning("Validation Error", "Invalid sensor data. Please check the input fields.")

    def delete_selected_sensor(self):
        selected_sensor = self.sensor_listbox.get(self.sensor_listbox.curselection())
        sensor_id = int(selected_sensor.split(":")[0])
        try:
            db_delete_selected_sensor(sensor_id)
            self.populate_sensor_listbox()  # Refresh the listbox
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred while deleting the sensor: {e}")


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
        elif sensor_type == 'Semiconductor':
            return self.validate_semiconductor_data(sensor_data)
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
        try:
            nominal_resistance = float(sensor_data['Nominal Resistance (e.g., 100 ohms at 0°C)'])
            coefficient = float(sensor_data['Coefficient (e.g., 0.00385)'])
            return 0 < nominal_resistance <= 1000 and 0 < coefficient <= 1
        except ValueError:
            return False

    def validate_thermocouple_data(self, sensor_data):
        valid_types = ['J', 'K', 'E', 'T', 'N', 'B', 'R', 'S']
        thermocouple_type = sensor_data['Type (J, K, E, T, N, B, R, S, etc.)']
        try:
            seebeck_coefficient = float(sensor_data['Seebeck Coefficient (μV/°C)'])
            return thermocouple_type in valid_types and 0 < seebeck_coefficient <= 100
        except ValueError:
            return False


    def validate_thermistor_data(self, sensor_data):
        try:
            resistance_at_25C = float(sensor_data['Resistance at 25°C (e.g., 10k ohms)'])
            beta_value = float(sensor_data['Beta Value'])
            sensor_type = sensor_data['Type (NTC or PTC)']
            return 0 < resistance_at_25C <= 10000 and 0 < beta_value <= 10000 and sensor_type in ['NTC', 'PTC']
        except ValueError:
            return False

    def validate_semiconductor_data(self, sensor_data):
        try:
            output_type = sensor_data['Output Type (e.g., Analog, Digital)']
            interface = sensor_data['Interface (e.g., I2C, SPI)']
            return output_type in ['Analog', 'Digital'] and interface in ['I2C', 'SPI']
        except ValueError:
            return False

    def validate_ir_data(self, sensor_data):
        field_of_view = sensor_data['Field of View (e.g., 90°)']
        wavelength_range = sensor_data['Wavelength Range']
        return field_of_view and wavelength_range

    def validate_bimetallic_data(self, sensor_data):
        material_types = sensor_data['Material Types (e.g., copper & iron)']
        try:
            switch_point_temperature = float(sensor_data['Switch Point Temperature'])
            return material_types and 0 < switch_point_temperature
        except ValueError:
            return False

    def validate_fiber_optic_data(self, sensor_data):
        try:
            fiber_type = sensor_data['Fiber Type (e.g., single-mode, multi-mode)']
            wavelength = float(sensor_data['Wavelength'])
            return fiber_type in ['single-mode', 'multi-mode'] and 0 < wavelength <= 1000
        except ValueError:
            return False

    def validate_digital_data(self, sensor_data):
        try:
            interface = sensor_data['Interface (e.g., I2C, SPI)']
            resolution = int(sensor_data['Resolution (e.g., 12-bit)'])
            return interface in ['I2C', 'SPI'] and 8 <= resolution <= 16
        except ValueError:
            return False
