import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog
from linkage_db import LinkedDatabase

class EditLinkDialog(simpledialog.Dialog):
    def __init__(self, parent, link):
        self.link = link
        super().__init__(parent)

    def body(self, frame):
        self.motor_combobox = ttk.Combobox(frame, values=[motor.name for motor in self.link.motor])
        self.motor_combobox.grid(row=0, column=1)
        self.motor_combobox.set(self.link.motor.name)

        self.sensor_combobox = ttk.Combobox(frame, values=[sensor.name for sensor in self.link.sensor])
        self.sensor_combobox.grid(row=1, column=1)
        self.sensor_combobox.set(self.link.sensor.name)

        ttk.Label(frame, text="Relationship:").grid(row=2, column=0)
        self.relationship_entry = ttk.Entry(frame)
        self.relationship_entry.grid(row=2, column=1)
        self.relationship_entry.insert(0, self.link.relationship)
        return self.motor_combobox

    def apply(self):
        motor_id = self.link.motor[self.motor_combobox.current()].id
        sensor_id = self.link.sensor[self.sensor_combobox.current()].id
        relationship = self.relationship_entry.get()
        self.link.update_link(self.link.id, motor_id, sensor_id, relationship)

class EditGroupDialog(simpledialog.Dialog):
    def __init__(self, parent, group_name):
        self.group_name = group_name
        super().__init__(parent)

    def body(self, frame):
        ttk.Label(frame, text="Group Name:").grid(row=0, column=0)
        self.group_name_entry = ttk.Entry(frame)
        self.group_name_entry.grid(row=0, column=1)
        self.group_name_entry.insert(0, self.group_name)
        return self.group_name_entry

    def apply(self):
        self.group_name = self.group_name_entry.get()

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
        
         # Search Entry
        self.search_entry = ttk.Entry(self.root)
        self.search_entry.grid(row=0, column=2)
        self.search_button = ttk.Button(self.root, text="Search", command=self.search_links)
        self.search_button.grid(row=0, column=3)

        # Edit Button
        self.edit_button = ttk.Button(self.root, text="Edit", command=self.edit_link)
        self.edit_button.grid(row=5, column=0, columnspan=2)

        # Group Management
        self.group_label = ttk.Label(self.root, text="Group Management:")
        self.group_label.grid(row=6, column=0, columnspan=4)
        self.group_combobox = ttk.Combobox(self.root, values=self.linked_db.get_all_sensor_groups())
        self.group_combobox.grid(row=7, column=0, columnspan=2)
        self.group_add_button = ttk.Button(self.root, text="Add Group", command=self.add_group)
        self.group_add_button.grid(row=7, column=2)
        self.group_edit_button = ttk.Button(self.root, text="Edit Group", command=self.edit_group)
        self.group_edit_button.grid(row=7, column=3)
        self.group_delete_button = ttk.Button(self.root, text="Delete Group", command=self.delete_group)
        self.group_delete_button.grid(row=8, column=2, columnspan=2)

    def edit_link(self):
        selected_index = self.linked_listbox.curselection()
        if selected_index:
            link = self.linked_db.get_all_links()[selected_index[0]]
            EditLinkDialog(self.root, link)
            self.load_links()

    def edit_group(self):
        group_id = self.group_combobox.current()
        group = self.linked_db.get_all_sensor_groups()[group_id]
        dialog = EditGroupDialog(self.root, group.group_name)
        self.linked_db.update_sensor_group(group_id, dialog.group_name)
        self.load_groups()

def search_links(self):

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



