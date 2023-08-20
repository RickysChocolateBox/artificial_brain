import tkinter as tk
from tkinter import ttk, messagebox
from linked_db import LinkedDatabase
from motor_manager_db.py import MotorDatabase
from temperature_sensor_db import TemperatureSensorDatabase

class LinkageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Linkage Manager")
        self.linked_db = LinkedDatabase()
        self.motor_db = MotorDatabase()
        self.sensor_db = TemperatureSensorDatabase()
        self.create_widgets()

    def create_widgets(self):
        # Dropdown for motors
        motors = [motor.motor_name for motor in self.motor_db.get_all_motors()]
        self.motor_combobox = ttk.Combobox(self.root, values=motors)
        self.motor_combobox.grid(row=0, column=1)

        # Dropdown for temperature sensors
        sensors = [sensor.sensor_name for sensor in self.sensor_db.get_all_sensors()]
        self.sensor_combobox = ttk.Combobox(self.root, values=sensors)
        self.sensor_combobox.grid(row=1, column=1)

        # Relationship Entry
        ttk.Label(self.root, text="Relationship:").grid(row=2, column=0)
        self.relationship_entry = ttk.Entry(self.root)
        self.relationship_entry.grid(row=2, column=1)

        # Link Button
        self.link_button = ttk.Button(self.root, text="Link", command=self.link_hardware)
        self.link_button.grid(row=3, column=0, columnspan=2)

        # List of linked hardware
        self.linked_listbox = tk.Listbox(self.root)
        self.linked_listbox.grid(row=4, column=0, columnspan=2)
        self.load_links()

    def link_hardware(self):
        motor_index = self.motor_combobox.current()
        sensor_index = self.sensor_combobox.current()

        motor = self.motor_db.get_motor_by_index(motor_index)
        sensor = self.sensor_db.get_sensor_by_index(sensor_index)

        motor_id = motor.id
        sensor_id = sensor.id
        relationship = self.relationship_entry.get()

        self.linked_db.link_hardware(motor_id, sensor_id, relationship)
        self.load_links()
        messagebox.showinfo("Success", "Hardware linked successfully!")

    def load_links(self):
        links = self.linked_db.get_all_links()
        self.linked_listbox.delete(0, tk.END)
        for link in links:
            self.linked_listbox.insert(tk.END, f"Motor: {link.motor_id}, Sensor: {link.sensor_id}, Relationship: {link.relationship}")

