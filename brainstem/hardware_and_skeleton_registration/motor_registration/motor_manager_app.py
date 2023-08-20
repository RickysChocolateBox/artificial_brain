import tkinter as tk
from tkinter import ttk, messagebox
from motor_manager_db import MotorDatabase


class MotorManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Motor Management")
        self.motor_db = MotorDatabase() # Create an instance of MotorDatabase
        self.current_motor_id = None
        self.create_widgets()
        self.load_motors()

    def create_widgets(self):
        # Motor Type
        ttk.Label(self.root, text="Motor Type:").grid(row=0, column=0, sticky='w')
        self.motor_type = ttk.Combobox(self.root, values=["DC", "Stepper", "Servo", "Linear Actuator"])
        self.motor_type.grid(row=0, column=1)
        self.motor_type.bind("<FocusOut>", self.validate_motor_type) # Bind the validation function
        self.motor_type_label = ttk.Label(self.root, text="", foreground="red")
        self.motor_type_label.grid(row=0, column=2)

        # Brush Type
        ttk.Label(self.root, text="Brush Type:").grid(row=1, column=0, sticky='w')
        self.brush_type = ttk.Combobox(self.root, values=["Brushed", "Brushless"])
        self.brush_type.grid(row=1, column=1)
        self.brush_type.bind("<FocusOut>", self.validate_brush_type) # Bind the validation function
        self.brush_type_label = ttk.Label(self.root, text="", foreground="red")
        self.brush_type_label.grid(row=1, column=2)


        # Motor Name
        ttk.Label(self.root, text="Motor Name:").grid(row=2, column=0, sticky='w')
        self.motor_name = ttk.Entry(self.root)
        self.motor_name.grid(row=2, column=1)
        self.motor_name.bind("<FocusOut>", self.validate_motor_name) # Bind validation
        self.motor_name_label = ttk.Label(self.root, text="", foreground="red")
        self.motor_name_label.grid(row=2, column=2)

        # RPM
        ttk.Label(self.root, text="RPM:").grid(row=3, column=0, sticky='w')
        self.rpm = ttk.Entry(self.root)
        self.rpm.grid(row=3, column=1)
        self.rpm.bind("<FocusOut>", self.validate_positive_integer) # Bind validation
        self.rpm_label = ttk.Label(self.root, text="", foreground="red")
        self.rpm_label.grid(row=3, column=2)

        # Gear Reduction
        ttk.Label(self.root, text="Gear Reduction:").grid(row=4, column=0, sticky='w')
        self.gear_reduction = ttk.Entry(self.root)
        self.gear_reduction.grid(row=4, column=1)
        self.gear_reduction.bind("<FocusOut>", self.validate_positive_float) # Bind validation
        self.gear_reduction_label = ttk.Label(self.root, text="", foreground="red")
        self.gear_reduction_label.grid(row=4, column=2)

        # Resistance
        ttk.Label(self.root, text="Resistance:").grid(row=5, column=0, sticky='w')
        self.resistance = ttk.Entry(self.root)
        self.resistance.grid(row=5, column=1)
        self.resistance.bind("<FocusOut>", self.validate_positive_float) # Bind validation
        self.resistance_label = ttk.Label(self.root, text="", foreground="red")
        self.resistance_label.grid(row=5, column=2)

        # Torque
        ttk.Label(self.root, text="Torque:").grid(row=6, column=0, sticky='w')
        self.torque = ttk.Entry(self.root)
        self.torque.grid(row=6, column=1)
        self.torque.bind("<FocusOut>", self.validate_positive_float) # Bind validation
        self.torque_label = ttk.Label(self.root, text="", foreground="red")
        self.torque_label.grid(row=6, column=2)

        # Voltage
        ttk.Label(self.root, text="Voltage:").grid(row=7, column=0, sticky='w')
        self.voltage = ttk.Entry(self.root)
        self.voltage.grid(row=7, column=1)
        self.voltage.bind("<FocusOut>", self.validate_positive_float) # Bind validation
        self.voltage_label = ttk.Label(self.root, text="", foreground="red")
        self.voltage_label.grid(row=7, column=2)

        # Current
        ttk.Label(self.root, text="Current:").grid(row=8, column=0, sticky='w')
        self.current = ttk.Entry(self.root)
        self.current.grid(row=8, column=1)
        self.current.bind("<FocusOut>", self.validate_positive_float) # Bind validation
        self.current_label = ttk.Label(self.root, text="", foreground="red")
        self.current_label.grid(row=8, column=2)

        # Encoder Ratio
        ttk.Label(self.root, text="Encoder Ratio:").grid(row=9, column=0, sticky='w')
        self.encoder_ratio = ttk.Entry(self.root)
        self.encoder_ratio.grid(row=9, column=1)
        self.encoder_ratio.bind("<FocusOut>", self.validate_positive_float) # Bind validation
        self.encoder_ratio_label = ttk.Label(self.root, text="", foreground="red")
        self.encoder_ratio_label.grid(row=9, column=2)

                # Safe Temperature
        ttk.Label(self.root, text="Safe Temperature:").grid(row=10, column=0, sticky='w')
        self.safe_temperature = ttk.Entry(self.root)
        self.safe_temperature.grid(row=10, column=1)
        self.safe_temperature.bind("<FocusOut>", self.validate_temperature_relationship) # Bind validation
        self.safe_temperature_label = ttk.Label(self.root, text="", foreground="red")
        self.safe_temperature_label.grid(row=10, column=2)

         # Warning Temperature
        ttk.Label(self.root, text="Warning Temperature:").grid(row=11, column=0, sticky='w')
        self.warning_temperature = ttk.Entry(self.root)
        self.warning_temperature.grid(row=11, column=1)
        self.warning_temperature.bind("<FocusOut>", self.validate_temperature_relationship) # Bind validation
        self.warning_temperature_label = ttk.Label(self.root, text="", foreground="red")
        self.warning_temperature_label.grid(row=11, column=2)

         # Red Flag Temperature
        ttk.Label(self.root, text="Red Flag Temperature:").grid(row=12, column=0, sticky='w')
        self.red_flag_temperature = ttk.Entry(self.root)
        self.red_flag_temperature.grid(row=12, column=1)
        self.red_flag_temperature.bind("<FocusOut>", self.validate_temperature_relationship) # Bind validation
        self.red_flag_temperature_label = ttk.Label(self.root, text="", foreground="red")
        self.red_flag_temperature_label.grid(row=12, column=2)
        
        # Bind to a new method for temperature validation
        self.safe_temperature.bind("<FocusOut>", self.validate_temperature_event)
        self.warning_temperature.bind("<FocusOut>", self.validate_temperature_event)
        self.red_flag_temperature.bind("<FocusOut>", self.validate_temperature_event)
        
        # Description
        ttk.Label(self.root, text="Description:").grid(row=13, column=0, sticky='w')
        self.description = ttk.Entry(self.root)
        self.description.grid(row=13, column=1)
        # Optional validation for Description if needed
    def clear_fields(self):
        # Clear Motor Type
        self.motor_type.set('')

        # Clear Brush Type
        self.brush_type.set('')

        # Clear Motor Name
        self.motor_name.delete(0, tk.END)

        # Clear other numeric fields
        for attribute in [self.rpm, self.gear_reduction, self.resistance, self.torque,
                         self.voltage, self.current, self.encoder_ratio,
                         self.safe_temperature, self.warning_temperature, self.red_flag_temperature]:
            attribute.delete(0, tk.END)

        # Clear Description
        self.description.delete(0, tk.END)

        # Clear Validation Labels
        for label in [self.motor_type_label, self.brush_type_label, self.motor_name_label,
                      self.rpm_label, self.gear_reduction_label, self.resistance_label,
                      self.torque_label, self.voltage_label, self.current_label,
                      self.encoder_ratio_label, self.safe_temperature_label,
                      self.warning_temperature_label, self.red_flag_temperature_label]:
            label.config(text="")

        # Submit Button
        ttk.Button(self.root, text="Submit", command=self.add_motor).grid(row=14, column=0, columnspan=2)
        
        # Update Button
        ttk.Button(self.root, text="Update", command=self.update_motor).grid(row=15, column=0, columnspan=2)

        # List of motors
        self.motors_listbox = tk.Listbox(self.root, height=10, width=50, bg="white", activestyle="none",
                                         font="Arial", fg="black")
        self.motors_listbox.grid(row=16, column=0, columnspan=2)
        self.motors_listbox.bind('<<ListboxSelect>>', self.load_selected_motor)

        # Delete Button
        ttk.Button(self.root, text="Delete", command=self.delete_motor).grid(row=17, column=0, columnspan=2)
        
    def validate_motor_type(self, event):
        motor_type = self.motor_type.get()
        if motor_type not in ["DC", "Stepper", "Servo", "Linear Actuator"]:
            self.motor_type_label.config(text="Invalid Motor Type!")
        else:
            self.motor_type_label.config(text="")

    def validate_brush_type(self, event):
        brush_type = self.brush_type.get()
        if brush_type not in ["Brushed", "Brushless"]:
            self.brush_type_label.config(text="Invalid Brush Type!")
        else:
            self.brush_type_label.config(text="")

    def validate_positive_integer(self, event):
        widget_name = str(event.widget)
        value = self.root.nametowidget(widget_name).get()
        label = getattr(self, widget_name.split(".")[-1] + "_label")

        if not value.isdigit() or int(value) <= 0:
            label.config(text="Must be a positive integer!")
        else:
            label.config(text="")

    def validate_positive_float(self, event):
        widget_name = str(event.widget)
        value = self.root.nametowidget(widget_name).get()
        label = getattr(self, widget_name.split(".")[-1] + "_label")
        try:
           if float(value) <= 0:
              label.config(text="Must be a positive number!")
           else:
            label.config(text="")
        except ValueError:
            label.config(text="Must be a positive number!")
        
    def validate_motor_name(self, event):
        motor_name = self.motor_name.get()
        if not motor_name.strip():
            self.motor_name_label.config(text="Motor Name must not be empty!")
        else:
            self.motor_name_label.config(text="")

    def validate_temperature_event(self, event):
        # Call the method to validate temperature relationship
        is_valid = self.validate_temperature_relationship()
        if not is_valid:
            # Display an error message if validation fails
            self.safe_temperature_label.config(text="Invalid Temperature Relationship!")
            self.warning_temperature_label.config(text="Invalid Temperature Relationship!")
            self.red_flag_temperature_label.config(text="Invalid Temperature Relationship!")
        else:
            # Clear the error message if validation succeeds
            self.safe_temperature_label.config(text="")
            self.warning_temperature_label.config(text="")
            self.red_flag_temperature_label.config(text="")

    def validate_temperature_relationship(self):
        try:
            safe_temp = float(self.safe_temperature.get())
            warning_temp = float(self.warning_temperature.get())
            red_flag_temp = float(self.red_flag_temperature.get())

            if safe_temp < warning_temp < red_flag_temp:
                return True
            else:
                return False
        except ValueError:
            return False

    def add_motor(self):
        try:  # Start of the try block
            # Validate Motor Type
            motor_type = self.motor_type.get()
            if motor_type not in ["DC", "Stepper", "Servo", "Linear Actuator"]:
                messagebox.showerror("Validation Error", "Invalid Motor Type! Select one of: DC, Stepper, Servo, Linear Actuator.")
                return

            # Validate Brush Type
            brush_type = self.brush_type.get()
            if brush_type not in ["Brushed", "Brushless"]:
                messagebox.showerror("Validation Error", "Invalid Brush Type! Select one of: Brushed, Brushless.")
                return

            # Validate RPM
            rpm = self.rpm.get()
            if not rpm.isdigit() or int(rpm) <= 0:
                messagebox.showerror("Validation Error", "RPM must be a positive integer!")
                return

            # Validate other float attributes
            for value, field_name in zip([self.gear_reduction.get(), self.resistance.get(), self.torque.get(),
                                          self.voltage.get(), self.current.get(), self.encoder_ratio.get(),
                                          self.safe_temperature.get(), self.warning_temperature.get(), self.red_flag_temperature.get()],
                                         ["Gear Reduction", "Resistance", "Torque", "Voltage", "Current", "Encoder Ratio",
                                          "Safe Temperature", "Warning Temperature", "Red Flag Temperature"]):
                try:
                    if float(value) <= 0:
                        messagebox.showerror("Validation Error", f"{field_name} must be a positive number!")
                        return
                except ValueError:
                    messagebox.showerror("Validation Error", f"{field_name} must be a positive number!")
                    return

            # Validate temperature relationship
            if not self.validate_temperature_relationship():
                messagebox.showerror("Validation Error", "Safe Temperature < Warning Temperature < Red Flag Temperature must hold true!")
                return

            # All validations passed, proceed to add the motor to the database
            motor_data = {
                'motor_type': motor_type,
                'brush_type': brush_type,
                'motor_name': self.motor_name.get(),
                'rpm': int(rpm),
                'gear_reduction': float(self.gear_reduction.get()),
                'resistance': float(self.resistance.get()),
                'torque': float(self.torque.get()),
                'voltage': float(self.voltage.get()),
                'current': float(self.current.get()),
                'encoder_ratio': float(self.encoder_ratio.get()),
                'safe_temperature': float(self.safe_temperature.get()),
                'warning_temperature': float(self.warning_temperature.get()),
                'red_flag_temperature': float(self.red_flag_temperature.get()),
                'description': self.description.get()
            }
            self.motor_db.add_motor(motor_data) # Call to MotorDatabase's method
            self.load_motors()
            self.clear_fields()
            messagebox.showinfo("Success", "Motor added successfully!")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def load_motors(self):
        motors = self.motor_db.get_all_motors()
        self.motors_listbox.delete(0, tk.END)
        for motor in motors:
            self.motors_listbox.insert(tk.END, motor['motor_name'])

    def load_selected_motor(self, event):
        index = self.motors_listbox.curselection()[0]
        selected_motor = self.motor_db.get_motor_by_index(index)  # Use get_motor_by_index here
        self.current_motor_id = selected_motor.id  # Updated to selected_motor.id as selected_motor is an object
        self.motor_type.set(selected_motor.motor_type)
        self.brush_type.set(selected_motor.brush_type)
        self.motor_name.delete(0, tk.END)
        self.motor_name.insert(tk.END, selected_motor.motor_name)
        self.rpm.delete(0, tk.END)
        self.rpm.insert(tk.END, selected_motor.rpm)
        self.gear_reduction.delete(0, tk.END)
        self.gear_reduction.insert(tk.END, selected_motor.gear_reduction)
        self.resistance.delete(0, tk.END)
        self.resistance.insert(tk.END, selected_motor.resistance)
        self.torque.delete(0, tk.END)
        self.torque.insert(tk.END, selected_motor.torque)
        self.voltage.delete(0, tk.END)
        self.voltage.insert(tk.END, selected_motor.voltage)
        self.current.delete(0, tk.END)
        self.current.insert(tk.END, selected_motor.current)
        self.encoder_ratio.delete(0, tk.END)
        self.encoder_ratio.insert(tk.END, selected_motor.encoder_ratio)
        self.safe_temperature.delete(0, tk.END)
        self.safe_temperature.insert(tk.END, selected_motor.safe_temperature)
        self.warning_temperature.delete(0, tk.END)
        self.warning_temperature.insert(tk.END, selected_motor.warning_temperature)
        self.red_flag_temperature.delete(0, tk.END)
        self.red_flag_temperature.insert(tk.END, selected_motor.red_flag_temperature)
        self.description.delete(0, tk.END)
        self.description.insert(tk.END, selected_motor.description)

    def update_motor(self):
        try:  # Start of the try block
            motor_data = {
                'motor_type': self.motor_type.get(),
                'brush_type': self.brush_type.get(),
                'motor_name': self.motor_name.get(),
                'rpm': int(self.rpm.get()),
                'gear_reduction': float(self.gear_reduction.get()),
                'resistance': float(self.resistance.get()),
                'torque': float(self.torque.get()),
                'voltage': float(self.voltage.get()),
                'current': float(self.current.get()),
                'encoder_ratio': float(self.encoder_ratio.get()),
                'safe_temperature': float(self.safe_temperature.get()),
                'warning_temperature': float(self.warning_temperature.get()),
                'red_flag_temperature': float(self.red_flag_temperature.get()),
                'description': self.description.get()
            }
            self.motor_db.update_motor(self.current_motor_id, motor_data)
            self.load_motors()
            self.clear_fields()
            messagebox.showinfo("Success", "Motor updated successfully!")
        except Exception as e:  # Corrected here
            messagebox.showerror("Database Error", str(e))

    def delete_motor(self):
        try:  # Start of the try block
            self.motor_db.delete_motor(self.current_motor_id)
            self.load_motors()
            self.clear_fields()
            messagebox.showinfo("Success", "Motor deleted successfully!")
        except Exception as e:  # Corrected here
            messagebox.showerror("Database Error", str(e))