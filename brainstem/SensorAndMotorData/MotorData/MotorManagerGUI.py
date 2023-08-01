import tkinter as tk
from tkinter import ttk, messagebox
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Setup
Base = declarative_base()

class Motor(Base):
    __tablename__ = "motors"
    id = Column(Integer, primary_key=True)
    motor_type = Column(String)
    brush_type = Column(String)
    motor_name = Column(String)
    rpm = Column(Integer)
    gear_reduction = Column(Float)
    resistance = Column(Float)
    torque = Column(Float)
    voltage = Column(Float)
    current = Column(Float)
    encoder_ratio = Column(Float)
    safe_temperature = Column(Float)
    warning_temperature = Column(Float)
    red_flag_temperature = Column(Float)
    description = Column(String)

DATABASE_URL = "sqlite:///motors.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

class MotorManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Motor Management")
        self.session = SessionLocal()
        self.current_motor_id = None
        self.create_widgets()
        self.load_motors()

    def create_widgets(self):
        # Motor Type
        ttk.Label(self.root, text="Motor Type:").grid(row=0, column=0, sticky='w')
        self.motor_type = ttk.Combobox(self.root, values=["DC", "Stepper", "Servo", "Linear Actuator"])
        self.motor_type.grid(row=0, column=1)

        # Brush Type
        ttk.Label(self.root, text="Brush Type:").grid(row=1, column=0, sticky='w')
        self.brush_type = ttk.Combobox(self.root, values=["Brushed", "Brushless"])
        self.brush_type.grid(row=1, column=1)

        # Motor Name
        ttk.Label(self.root, text="Motor Name:").grid(row=2, column=0, sticky='w')
        self.motor_name = ttk.Entry(self.root)
        self.motor_name.grid(row=2, column=1)

        # RPM
        ttk.Label(self.root, text="RPM:").grid(row=3, column=0, sticky='w')
        self.rpm = ttk.Entry(self.root)
        self.rpm.grid(row=3, column=1)

        # Gear Reduction
        ttk.Label(self.root, text="Gear Reduction:").grid(row=4, column=0, sticky='w')
        self.gear_reduction = ttk.Entry(self.root)
        self.gear_reduction.grid(row=4, column=1)

        # Resistance
        ttk.Label(self.root, text="Resistance:").grid(row=5, column=0, sticky='w')
        self.resistance = ttk.Entry(self.root)
        self.resistance.grid(row=5, column=1)

        # Torque
        ttk.Label(self.root, text="Torque:").grid(row=6, column=0, sticky='w')
        self.torque = ttk.Entry(self.root)
        self.torque.grid(row=6, column=1)

        # Voltage
        ttk.Label(self.root, text="Voltage:").grid(row=7, column=0, sticky='w')
        self.voltage = ttk.Entry(self.root)
        self.voltage.grid(row=7, column=1)

        # Current
        ttk.Label(self.root, text="Current:").grid(row=8, column=0, sticky='w')
        self.current = ttk.Entry(self.root)
        self.current.grid(row=8, column=1)

        # Encoder Ratio
        ttk.Label(self.root, text="Encoder Ratio:").grid(row=9, column=0, sticky='w')
        self.encoder_ratio = ttk.Entry(self.root)
        self.encoder_ratio.grid(row=9, column=1)

        # Safe Temperature
        ttk.Label(self.root, text="Safe Temperature:").grid(row=10, column=0, sticky='w')
        self.safe_temperature = ttk.Entry(self.root)
        self.safe_temperature.grid(row=10, column=1)

        # Warning Temperature
        ttk.Label(self.root, text="Warning Temperature:").grid(row=11, column=0, sticky='w')
        self.warning_temperature = ttk.Entry(self.root)
        self.warning_temperature.grid(row=11, column=1)

        # Red Flag Temperature
        ttk.Label(self.root, text="Red Flag Temperature:").grid(row=12, column=0, sticky='w')
        self.red_flag_temperature = ttk.Entry(self.root)
        self.red_flag_temperature.grid(row=12, column=1)

        # Description
        ttk.Label(self.root, text="Description:").grid(row=13, column=0, sticky='w')
        self.description = ttk.Entry(self.root)
        self.description.grid(row=13, column=1)

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

    def add_motor(self):
        # Logic to add the motor data to the database
        new_motor = Motor(
            motor_type=self.motor_type.get(),
            brush_type=self.brush_type.get(),
            motor_name=self.motor_name.get(),
            rpm=int(self.rpm.get()),
            gear_reduction=float(self.gear_reduction.get()),
            resistance=float(self.resistance.get()),
            torque=float(self.torque.get()),
            voltage=float(self.voltage.get()),
            current=float(self.current.get()),
            encoder_ratio=float(self.encoder_ratio.get()),
            safe_temperature=float(self.safe_temperature.get()),
            warning_temperature=float(self.warning_temperature.get()),
            red_flag_temperature=float(self.red_flag_temperature.get()),
            description=self.description.get()
        )
        self.session.add(new_motor)
        self.session.commit()
        self.load_motors()

    def load_motors(self):
        motors = self.session.query(Motor).all()
        self.motors_listbox.delete(0, tk.END)
        for motor in motors:
            self.motors_listbox.insert(tk.END, motor.motor_name)

    def load_selected_motor(self, event):
        index = self.motors_listbox.curselection()[0]
        selected_motor = self.session.query(Motor).all()[index]
        self.current_motor_id = selected_motor.id
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
        motor = self.session.query(Motor).filter(Motor.id == self.current_motor_id).first()
        motor.motor_type = self.motor_type.get()
        motor.brush_type = self.brush_type.get()
        motor.motor_name = self.motor_name.get()
        motor.rpm = int(self.rpm.get())
        motor.gear_reduction = float(self.gear_reduction.get())
        motor.resistance = float(self.resistance.get())
        motor.torque = float(self.torque.get())
        motor.voltage = float(self.voltage.get())
        motor.current = float(self.current.get())
        motor.encoder_ratio = float(self.encoder_ratio.get())
        motor.safe_temperature = float(self.safe_temperature.get())
        motor.warning_temperature = float(self.warning_temperature.get())
        motor.red_flag_temperature = float(self.red_flag_temperature.get())
        motor.description = self.description.get()
        self.session.commit()
        self.load_motors()

    def delete_motor(self):
        motor = self.session.query(Motor).filter(Motor.id == self.current_motor_id).first()
        self.session.delete(motor)
        self.session.commit()
        self.load_motors()

if __name__ == "__main__":
    root = tk.Tk()
    app = MotorManager(root)
    root.mainloop()

