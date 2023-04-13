class Bone:
    def __init__(self, name, length):
        self.name = name
        self.length = length


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

    def motor_menu(self):
        while True:
            print("\nChoose an option:")
            print("1. Add Bone")
            print("2. Add Joint")
            print("3. Add Motor")
            print("4. Quit")

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
                break

            else:
                print("Invalid choice. Please try again.")

