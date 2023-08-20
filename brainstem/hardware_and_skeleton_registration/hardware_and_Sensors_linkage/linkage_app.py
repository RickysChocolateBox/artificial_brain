import tkinter as tk
from tkinter import ttk, messagebox
from linkage_db import LinkedDatabase

class LinkageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Linkage Manager")
        self.linked_db = LinkedDatabase()
        self.create_widgets()

    def create_widgets(self):
        # Dropdown for motors
        motors = [motor.name for motor in self.linked_db.get_all_motors()]
        self.motor_combobox = ttk.Combobox(self.root, values=motors)
        self.motor_combobox.grid(row=0, column=1)

        # Dropdown for sensors
        sensors = [sensor.name for sensor in self.linked_db.get_all_sensors()]
        self.sensor_combobox = ttk.Combobox(self.root, values=sensors)
        self.sensor_combobox.grid(row=1, column=1)

        # Relationship Entry
        ttk.Label(self.root, text="Relationship:").grid(row=2, column=0)
        self.relationship_entry = ttk.Entry(self.root)
        self.relationship_entry.grid(row=2, column=1)

        # Link Button
        self.link_button = ttk.Button(self.root, text="Link", command=self.link_hardware)
        self.link_button.grid(row=3, column=0)

        # Unlink Button
        self.unlink_button = ttk.Button(self.root, text="Unlink", command=self.unlink_hardware)
        self.unlink_button.grid(row=3, column=1)

        # List of linked hardware
        self.linked_listbox = tk.Listbox(self.root)
        self.linked_listbox.grid(row=4, column=0, columnspan=2)
        self.load_links()

    def link_hardware(self):
        motor_index = self.motor_combobox.current()
        sensor_index = self.sensor_combobox.current()
        relationship = self.relationship_entry.get()

        # Validation
        if motor_index == -1 or sensor_index == -1 or not relationship:
            messagebox.showwarning("Validation Error", "Please select motor, sensor, and relationship.")
            return

        # Confirmation Dialog
        if not messagebox.askyesno("Confirmation", "Do you want to link the selected hardware?"):
            return

        motor = self.linked_db.get_all_motors()[motor_index]
        sensor = self.linked_db.get_all_sensors()[sensor_index]

        motor_id = motor.id
        sensor_id = sensor.id
        try:
            self.linked_db.add_link(motor_id, sensor_id, relationship)
            self.load_links()
            messagebox.showinfo("Success", "Hardware linked successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def unlink_hardware(self):
        selected_index = self.linked_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "Please select a link to unlink.")
            return

        if not messagebox.askyesno("Confirmation", "Do you want to unlink the selected hardware?"):
            return

        link = self.linked_db.get_all_links()[selected_index[0]]
        try:
            self.linked_db.delete_link(link.id)
            self.load_links()
            messagebox.showinfo("Success", "Hardware unlinked successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_links(self):
        links = self.linked_db.get_all_links()
        self.linked_listbox.delete(0, tk.END)
        for link in links:
            self.linked_listbox.insert(tk.END, f"Motor: {link.motor.name}, Sensor: {link.sensor.name}, Relationship: {link.relationship}")



