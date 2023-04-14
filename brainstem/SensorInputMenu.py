import threading
from AdaptiveNeuralNetwork import AdaptiveNeuralNetwork
from Brainstem import Brainstem
from StereoVisionSource import StereoVisionSource
from StereoAudioSource import AudioSource
from ThermalImagingSource import ThermalImagingSource
from LiDARSource import LiDARSource
from PressureSensorSource import PressureSensorSource
from TextureSensorSource import TextureSensorSource
from ExternalHeatSensorSource import ExternalHeatSensorSource
from GyroscopicSensorSource import GyroscopicSensorSource
from MotorJointPositionSensorSource import MotorJointPositionSensorSource
from InternalTemperatureSensorSource import InternalTemperatureSensorSource
from MotorSource import Motor

class SensorInputMenuClass:
    def __init__(self,Brainstem,
                 AdaptiveNeuralNetwork,
                 HebbianLearning,
                 SynapticScaling,
                 AutoTuneToolkit,
                 
                 ):

        # Initialize the adaptive neural network and brainstem
        AdaptiveNeuralNetwork = AdaptiveNeuralNetwork()
        brainstem = Brainstem(AdaptiveNeuralNetwork)

        pressure_sensor_sources = []

    while True:
        print("\nChoose an option:")
        print("1. Add Sensor")
        print("2. Add Motor")
        print("3. Quit")

        main_choice = int(input("Enter the number corresponding to your choice: "))

        if main_choice == 1:
            print("\nChoose a sensor to add:")
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

            choice = int(input("Enter the number corresponding to your choice: "))

            if choice == 1:
               port = input("Enter the port name for the stereo vision system (e.g., COM3 on Windows or /dev/ttyACM0 on Linux): ")
               stereo_vision_source = StereoVisionSource(port)
               stereo_vision_source.connect()
               Brainstem.add_sensory_source("stereo_camera", stereo_vision_source)

            elif choice == 2:
                 audio_source = AudioSource()
                 audio_source.start_recording()
                 # Apply high-pass filter (optional)
                 audio_source.apply_high_pass_filter(cutoff_frequency=100)
                 # Apply noise reduction (optional)
                 audio_source.apply_noise_reduction(noise_reduction_factor=0.9)
                 # Apply pitch shift (optional)
                 audio_source.apply_pitch_shift(pitch_shift_factor=2)
                 Brainstem.add_sensory_source("audio", audio_source)
 
            elif choice == 3:
                thermal_imaging_source_left = ThermalImagingSource()
                thermal_imaging_source_right = ThermalImagingSource()
                Brainstem.add_sensory_source("thermal_imaging_left", thermal_imaging_source_left)
                Brainstem.add_sensory_source("thermal_imaging_right", thermal_imaging_source_right)

            elif choice == 4:
                 port = input("Enter the port name for the LiDAR system (e.g., COM3 on Windows or /dev/ttyACM0 on Linux): ")
                 lidar_source = LiDARSource(port)
                 lidar_source.connect()
                 Brainstem.add_sensory_source("lidar", lidar_source)

            elif choice == 5:
                num_sensors = int(input("Enter the number of pressure sensors you want to add: "))
                pressure_sensors = []

                for i in range(num_sensors):
                    port = input(f"Enter the port name for pressure sensor {i+1} (e.g., COM3 on Windows or /dev/ttyACM0 on Linux): ")
                    pressure_sensor_source = PressureSensorSource(port)
                    pressure_sensor_source.connect()
                    Brainstem.add_sensory_source(f"pressure_sensor_{i+1}", pressure_sensor_source)
                    pressure_sensors.append(pressure_sensor_source)

                print(f"{num_sensors} pressure sensors added successfully!")

            elif choice == 6:
                 sensor_type = input("Enter the sensor type ('biotac_sp', 'biotac_toccare', or 'optoforce'): ")
    
                 if sensor_type == "biotac_sp" or sensor_type == "biotac_toccare":
                    port = input("Enter the serial port for the BioTac sensor (e.g., '/dev/ttyUSB0'): ")
                    texture_sensor_source = TextureSensorSource(sensor_type, port=port)
                 elif sensor_type == "optoforce":
                    bus_number = int(input("Enter the I2C bus number (e.g., 1): "))
                    sensor_address = int(input("Enter the I2C sensor address (e.g., 0x29): "), 0)
                    texture_sensor_source = TextureSensorSource(sensor_type, bus_number=bus_number, sensor_address=sensor_address)
                 else:
                    print("Invalid sensor type. Please try again.")
                    continue

                 Brainstem.add_sensory_source("texture", texture_sensor_source)

            elif choice == 7:
                external_heat_sensor_source = ExternalHeatSensorSource()
                Brainstem.add_sensory_source("external_heat", external_heat_sensor_source)

            elif choice == 8:
                gyroscopic_sensor_source = GyroscopicSensorSource()
                Brainstem.add_sensory_source("gyro", gyroscopic_sensor_source)

            elif choice == 9:
                motor_joint_position_sensor_source = MotorJointPositionSensorSource()
                Brainstem.add_sensory_source("motor_joint_position", motor_joint_position_sensor_source)

            elif choice == 10:
                internal_temperature_sensor_source = InternalTemperatureSensorSource()
                Brainstem.add_sensory_source("internal_temperature", internal_temperature_sensor_source)

            else:
                print("Invalid choice. Please try again.")

            print("Sensor added successfully!")

        elif main_choice == 2:
            motor_name = input("Enter a name for the motor (e.g., left_arm, right_leg): ")
            motor = Motor(motor_name)
            Brainstem.add_motor(motor_name, motor)

            # Automatically add the corresponding sensor
            motor_joint_position_sensor_source = MotorJointPositionSensorSource(motor)
            Brainstem.add_sensory_source(f"{motor_name}_joint_position", motor_joint_position_sensor_source)

            print("Motor and corresponding sensor added successfully!")

        elif main_choice == 3:
            break

        else:
            print("Invalid choice. Please try again.")
