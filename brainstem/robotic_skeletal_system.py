from StereoVisionSource import StereoVision
from StereoAudioSource import StereoHearing
from ThermalImagingSource import StereoThermalImaging
from LiDARSource import LiDAR
from PressureSensorSource import PressureSensors
from TextureSensorSource import TextureSensors
from ExternalHeatSensorSource import ExternalHeatSensors
from GyroscopicSensorSource import GyroscopicSensors


class Sensor:
    def __init__(self, name, sensor_type, port):
        self.name = name
        self.sensor_type = sensor_type
        self.port = port


class Bone:
    def __init__(self, name, length, sensors=None):
        self.name = name
        self.length = length
        self.sensors = sensors if sensors else {}

    def attach_sensor(self, sensor):
        self.sensors[sensor.name] = sensor


class Joint:
    def __init__(self, name, parent_bone, child_bone, motor):
        self.name = name
        self.parent_bone = parent_bone
        self.child_bone = child_bone
        self.motor = motor


class Motor:
    def __init__(self, name, motor_type, voltage, amperage):
        self.name = name
        self.motor_type = motor_type
        self.voltage = voltage
        self.amperage = amperage


class MotorSource:
    def __init__(self):
        self.bones = {}
        self.joints = {}
        self.motors = {}

    def add_bone(self, name, length):
        bone = Bone(name, length)
        self.bones[name] = bone

    def add_joint(self, name, parent_bone_name, child_bone_name, motor_name):
        parent_bone = self.bones[parent_bone_name]
        child_bone = self.bones[child_bone_name]
        motor = self.motors[motor_name]
        joint = Joint(name, parent_bone, child_bone, motor)
        self.joints[name] = joint

    def add_motor(self, name, motor_type, voltage, amperage):
        motor = Motor(name, motor_type, voltage, amperage)
        self.motors[name] = motor

    def attach_sensor_to_bone(self, bone_name, sensor):
        bone = self.bones[bone_name]
        bone.attach_sensor(sensor)

    def sensor_selection_menu(self):
        print("\nChoose a sensor type:")
        print("1. Stereo Vision")
        print("2. Stereo Hearing")
        print("3. Stereo Thermal Imaging")
        print("4. LiDAR")
        print("5. Pressure Sensors")
        print("6. Texture Sensors")
        print("7. External Heat Sensors")
        print("8. Gyroscopic Sensors")
        print("9. Motor and Joint Position Sensors")
        print("10. Internal Temperature Sensors")
        print("11. Humidity Sensor Source")
        
        choice = int(input("Enter the number corresponding to your choice: "))
        sensor_name = input("Enter a name for the sensor: ")

        # Make sure to import the sensor classes at the beginning of your file.
        if choice == 1:
            sensor = StereoVision(sensor_name)
        elif choice == 2:
            sensor = StereoHearing(sensor_name)
        elif choice == 3:
            sensor = StereoThermalImaging(sensor_name)
        elif choice == 4:
            sensor = LiDAR(sensor_name)
        elif choice == 5:
            sensor = PressureSensors(sensor_name)
        elif choice == 6:
            sensor = TextureSensors(sensor_name)
        elif choice == 7:
            sensor = ExternalHeatSensors(sensor_name)
        elif choice == 8:
            sensor = GyroscopicSensors(sensor_name)
        elif choice == 9:
            sensor = MotorAndJointPositionSensors(sensor_name)
        elif choice == 10:
            sensor = InternalTemperatureSensors(sensor_name)
        elif choice == 11:
            sensor = HumiditySensorSource(sensor_name)
        else:
            print("Invalid choice. Please try again.")
            return self.sensor_selection_menu()

        return sensor

    def motor_menu(self):
        while True:
            print("\nChoose an option:")
            print("1. Add Bone")
            print("2. Add Joint")
            print("3. Add Motor")
            print("4. Attach Sensor to Bone")
            print("5. Quit")

            choice = int(input("Enter the number corresponding to your choice: "))

            if choice == 1:
                name = input("Enter the bone name: ")
                length = float(input("Enter the bone length: "))
                self.add_bone(name, length)
                print("Bone added successfully!")


            elif choice == 2:
                name = input("Enter the joint name: ")
                parent_bone_name = input("Enter the parent bone name: ")
                child_bone_name = input("Enter the child bone name: ")
                motor_name = input("Enter the motor name: ")
                self.add_joint(name, parent_bone_name, child_bone_name, motor_name)
                print("Joint added successfully!")

            elif choice == 3:
                name = input("Enter the motor name: ")
                motor_type = input("Enter the motor type: ")
                voltage = float(input("Enter the motor voltage: "))
                amperage = float(input("Enter the motor amperage: "))
                self.add_motor(name, motor_type, voltage, amperage)
                print("Motor added successfully!")

            elif choice == 4:
                name = input("Enter the sensor name: ")
                sensor_type = input("Enter the sensor type: ")
                port = input("Enter the sensor port: ")
                self.add_sensor(name, sensor_type, port)
                print("Sensor added successfully!")

            elif choice == 5:
                bone_name = input("Enter the bone name to attach the sensor: ")
                sensor_name = input("Enter the sensor name: ")
                self.attach_sensor_to_bone(bone_name, sensor_name)
                print("Sensor attached to the bone successfully!")

            elif choice == 6:
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    motor_source = MotorSource()
    motor_source.motor_menu()

