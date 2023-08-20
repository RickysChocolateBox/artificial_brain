import tkinter as tk
from tkinter import ttk, messagebox
from skeletal_database import SkeletalDatabase  # Ensure this is the correct import for the database class

class SkeletalDatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Skeletal Configuration Manager")
        self.skeletal_db = SkeletalDatabase()
        self.create_widgets()

    def create_widgets(self):
        self.create_linkage_points_widgets()
        self.create_parts_widgets()
        self.create_configurations_widgets()
        self.create_orientation_widgets()

    def create_linkage_points_widgets(self):
        # Linkage Points Management Frame
        self.linkage_points_frame = ttk.LabelFrame(self.root, text="Linkage Points Management")
        self.linkage_points_frame.grid(row=0, column=0, sticky="nsew")

        # Dropdown for linkage types
        ttk.Label(self.linkage_points_frame, text="Linkage Type:").grid(row=0, column=0)
        self.linkage_type_combobox = ttk.Combobox(self.linkage_points_frame, values=['Point', 'Rotational', 'Rigid'])
        self.linkage_type_combobox.grid(row=0, column=1)

        # Entry for linkage orientation
        ttk.Label(self.linkage_points_frame, text="Linkage Orientation:").grid(row=1, column=0)
        self.linkage_orientation_combobox = ttk.Combobox(self.linkage_points_frame, values=['Parallel', 'Right Angle', 'Horizontal', 'Vertical'])
        self.linkage_orientation_combobox.grid(row=1, column=1)

        # Buttons for CRUD operations
        self.add_linkage_button = ttk.Button(self.linkage_points_frame, text="Add Linkage", command=self.add_linkage_point)
        self.add_linkage_button.grid(row=2, column=0)
        self.update_linkage_button = ttk.Button(self.linkage_points_frame, text="Update Linkage", command=self.update_linkage_point, state=tk.DISABLED)
        self.update_linkage_button.grid(row=2, column=1)
        self.delete_linkage_button = ttk.Button(self.linkage_points_frame, text="Delete Linkage", command=self.delete_linkage_point, state=tk.DISABLED)
        self.delete_linkage_button.grid(row=2, column=2)

        # List of linkage points
        self.linkage_points_listbox = tk.Listbox(self.linkage_points_frame)
        self.linkage_points_listbox.grid(row=3, column=0, columnspan=3)
        self.linkage_points_listbox.bind('<<ListboxSelect>>', self.on_linkage_point_select)  # Add binding
        self.load_linkage_points()

    def create_parts_widgets(self):
        # Skeletal Parts Management Frame
        self.parts_frame = ttk.LabelFrame(self.root, text="Skeletal Parts Management")
        self.parts_frame.grid(row=1, column=0, sticky="nsew")
        self.search_criteria_combobox = ttk.Combobox(self.root, values=['Part Name', 'Orientation'])
        self.search_criteria_combobox.grid(row=9, column=0)
        self.search_entry = ttk.Entry(self.root)
        self.search_entry.grid(row=9, column=1)
        self.search_button = ttk.Button(self.root, text="Search", command=self.search_items)
        self.search_button.grid(row=9, column=2)
        # Entry for part name
        ttk.Label(self.parts_frame, text="Part Name:").grid(row=0, column=0)
        self.part_name_entry = ttk.Entry(self.parts_frame)
        self.part_name_entry.grid(row=0, column=1)

        # Entry for part description
        ttk.Label(self.parts_frame, text="Part Description:").grid(row=1, column=0)
        self.part_description_entry = ttk.Entry(self.parts_frame)
        self.part_description_entry.grid(row=1, column=1)

        # Buttons for CRUD operations
        self.add_part_button = ttk.Button(self.parts_frame, text="Add Part", command=self.add_part)
        self.add_part_button.grid(row=2, column=0)
        self.update_part_button = ttk.Button(self.parts_frame, text="Update Part", command=self.update_part, state=tk.DISABLED)
        self.update_part_button.grid(row=2, column=1)
        self.delete_part_button = ttk.Button(self.parts_frame, text="Delete Part", command=self.delete_part, state=tk.DISABLED)
        self.delete_part_button.grid(row=2, column=2)

        # List of parts
        self.parts_listbox = tk.Listbox(self.parts_frame)
        self.parts_listbox.grid(row=3, column=0, columnspan=3)
        self.parts_listbox.bind('<<ListboxSelect>>', self.on_parts_select)  # Add binding
        self.load_parts()

    def create_configurations_widgets(self):
        # Skeletal Configurations Management Frame
        self.configurations_frame = ttk.LabelFrame(self.root, text="Skeletal Configurations Management")
        self.configurations_frame.grid(row=2, column=0, sticky="nsew")

        # Entry for configuration name
        ttk.Label(self.configurations_frame, text="Configuration Name:").grid(row=0, column=0)
        self.config_name_entry = ttk.Entry(self.configurations_frame)
        self.config_name_entry.grid(row=0, column=1)

        # Entry for configuration description
        ttk.Label(self.configurations_frame, text="Configuration Description:").grid(row=1, column=0)
        self.config_description_entry = ttk.Entry(self.configurations_frame)
        self.config_description_entry.grid(row=1, column=1)

        # Buttons for CRUD operations
        self.add_config_button = ttk.Button(self.configurations_frame, text="Add Configuration", command=self.add_configuration)
        self.add_config_button.grid(row=2, column=0)
        self.update_config_button = ttk.Button(self.configurations_frame, text="Update Configuration", command=self.update_configuration, state=tk.DISABLED)
        self.update_config_button.grid(row=2, column=1)
        self.delete_config_button = ttk.Button(self.configurations_frame, text="Delete Configuration", command=self.delete_configuration, state=tk.DISABLED)
        self.delete_config_button.grid(row=2, column=2)

        # List of configurations
        self.configurations_listbox = tk.Listbox(self.configurations_frame)
        self.configurations_listbox.grid(row=3, column=0, columnspan=3)
        self.configurations_listbox.bind('<<ListboxSelect>>', self.on_configurations_select)  # Add binding
        self.load_configurations()

    def create_orientation_widgets(self):
        # Orientation Configuration Frame
        self.orientation_frame = ttk.LabelFrame(self.root, text="Orientation Configuration")
        self.orientation_frame.grid(row=3, column=0, sticky="nsew")

        # Entries for XYZ axes
        ttk.Label(self.orientation_frame, text="X Axis:").grid(row=0, column=0)
        self.x_axis_entry = ttk.Entry(self.orientation_frame)
        self.x_axis_entry.grid(row=0, column=1)

        ttk.Label(self.orientation_frame, text="Y Axis:").grid(row=1, column=0)
        self.y_axis_entry = ttk.Entry(self.orientation_frame)
        self.y_axis_entry.grid(row=1, column=1)

        ttk.Label(self.orientation_frame, text="Z Axis:").grid(row=2, column=0)
        self.z_axis_entry = ttk.Entry(self.orientation_frame)
        self.z_axis_entry.grid(row=2, column=1)

        # Button to update orientation
        self.update_orientation_button = ttk.Button(self.orientation_frame, text="Update Orientation", command=self.update_orientation)
        self.update_orientation_button.grid(row=3, column=0, columnspan=2)

    def on_linkage_point_select(self, event):
        # Enable update and delete buttons when an item is selected
        if self.linkage_points_listbox.curselection():
            self.update_linkage_button.config(state=tk.NORMAL)
            self.delete_linkage_button.config(state=tk.NORMAL)
        else:
            self.update_linkage_button.config(state=tk.DISABLED)
            self.delete_linkage_button.config(state=tk.DISABLED)

    def on_parts_select(self, event):
        # Enable update and delete buttons when an item is selected
        if self.parts_listbox.curselection():
            self.update_part_button.config(state=tk.NORMAL)
            self.delete_part_button.config(state=tk.NORMAL)
        else:
            self.update_part_button.config(state=tk.DISABLED)
            self.delete_part_button.config(state=tk.DISABLED)

    def on_configurations_select(self, event):
        # Enable update and delete buttons when an item is selected
        if self.configurations_listbox.curselection():
            self.update_config_button.config(state=tk.NORMAL)
            self.delete_config_button.config(state=tk.NORMAL)
        else:
            self.update_config_button.config(state=tk.DISABLED)
            self.delete_config_button.config(state=tk.DISABLED)

    # Linkage Points Management
    def add_linkage_point(self):
        linkage_type = self.linkage_type_combobox.get()
        linkage_orientation = self.linkage_orientation_combobox.get()

        if not linkage_type or not linkage_orientation:
            messagebox.showerror("Error", "Please select a linkage type and orientation!")
            return

        self.skeletal_db.add_linkage_point(linkage_type, linkage_orientation)
        self.load_linkage_points()
        messagebox.showinfo("Success", "Linkage point added successfully!")
        self.linkage_type_combobox.set('') # Clearing input
        self.linkage_orientation_combobox.set('') # Clearing input

    def update_linkage_point(self):
        selected_linkage_index = self.linkage_points_listbox.curselection()
        linkage_type = self.linkage_type_combobox.get()
        linkage_orientation = self.linkage_orientation_combobox.get()

        if not selected_linkage_index:
            messagebox.showerror("Error", "No linkage point selected!")
            return

        self.skeletal_db.update_linkage_point(selected_linkage_index[0], linkage_type, linkage_orientation)
        self.load_linkage_points()

    def delete_linkage_point(self):
        selected_linkage_index = self.linkage_points_listbox.curselection()

        if not selected_linkage_index:
            messagebox.showerror("Error", "No linkage point selected!")
            return

        self.skeletal_db.delete_linkage_point(selected_linkage_index[0])
        self.load_linkage_points()

    def load_linkage_points(self):
        self.linkage_points_listbox.delete(0, tk.END)
        linkage_points = self.skeletal_db.get_all_linkage_points()
        for linkage_point in linkage_points:
            self.linkage_points_listbox.insert(tk.END, f"{linkage_point['type']} - {linkage_point['orientation']}")

    # Skeletal Parts Management
    def add_part(self):
        part_name = self.part_name_entry.get().strip()
        part_description = self.part_description_entry.get().strip()

        if part_name == "" or part_description == "":
            messagebox.showerror("Error", "Part name and description cannot be empty!")
            return

        self.skeletal_db.add_part(part_name, part_description)
        self.load_parts()
        messagebox.showinfo("Success", "Part added successfully!")
        self.part_name_entry.delete(0, tk.END) # Clearing input
        self.part_description_entry.delete(0, tk.END) # Clearing input

    def update_part(self):
        selected_part_index = self.parts_listbox.curselection()
        part_name = self.part_name_entry.get()
        part_description = self.part_description_entry.get()

        if not selected_part_index:
            messagebox.showerror("Error", "No part selected!")
            return

        self.skeletal_db.update_part(selected_part_index[0], part_name, part_description)
        self.load_parts()

    def delete_part(self):
        selected_part_index = self.parts_listbox.curselection()

        if not selected_part_index:
            messagebox.showerror("Error", "No part selected!")
            return

        self.skeletal_db.delete_part(selected_part_index[0])
        self.load_parts()

    def load_parts(self):
        self.parts_listbox.delete(0, tk.END)
        parts = self.skeletal_db.get_all_parts()
        for part in parts:
            self.parts_listbox.insert(tk.END, f"{part['name']} - {part['description']}")

    # Skeletal Configurations Management
    def add_configuration(self):
        config_name = self.config_name_entry.get()
        config_description = self.config_description_entry.get()
        self.skeletal_db.add_configuration(config_name, config_description)
        self.load_configurations()

    def update_configuration(self):
        selected_config_index = self.configurations_listbox.curselection()
        config_name = self.config_name_entry.get()
        config_description = self.config_description_entry.get()

        if not selected_config_index:
            messagebox.showerror("Error", "No configuration selected!")
            return

        self.skeletal_db.update_configuration(selected_config_index[0], config_name, config_description)
        self.load_configurations()

    def delete_configuration(self):
        selected_config_index = self.configurations_listbox.curselection()

        if not selected_config_index:
            messagebox.showerror("Error", "No configuration selected!")
            return

        self.skeletal_db.delete_configuration(selected_config_index[0])
        self.load_configurations()

    def load_configurations(self):
        self.configurations_listbox.delete(0, tk.END)
        configurations = self.skeletal_db.get_all_configurations()
        for config in configurations:
            self.configurations_listbox.insert(tk.END, f"{config['name']} - {config['description']}")

    # Orientation Configuration
    def update_orientation(self):
        x_axis = self.x_axis_entry.get()
        y_axis = self.y_axis_entry.get()
        z_axis = self.z_axis_entry.get()

        if not all(map(self.is_valid_number, [x_axis, y_axis, z_axis])):
            messagebox.showerror("Error", "XYZ axes must be valid numbers!")
            return

        self.skeletal_db.update_orientation(float(x_axis), float(y_axis), float(z_axis))
        messagebox.showinfo("Success", "Orientation updated successfully!")

    def is_valid_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def search_items(self):
        query = self.search_entry.get().lower()
        criteria = self.search_criteria_combobox.get()

        # Filter items based on selected criteria
        if criteria == 'Part Name':
            filtered_items = [item for item in self.items if query in item['name'].lower()]
        elif criteria == 'Orientation':
            filtered_items = [item for item in self.items if query in str(item['orientation']).lower()]

        # Clear the listbox and populate with filtered items
        self.listbox.delete(0, tk.END)
        for item in filtered_items:
            self.listbox.insert(tk.END, item['name']) # Assuming 'name' is the display attribute
            

