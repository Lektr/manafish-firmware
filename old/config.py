import configparser
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_config():
    '''Load and return configuration from config.ini'''
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), './config.ini')
    if not os.path.exists(config_path):
        logging.error('Config file not found')
        raise FileNotFoundError('config.ini not found')
    config.read(config_path)
    return config

# Network
def get_ip_address():
    return load_config()['network']['ip_address']

def get_device_controls_port():
    return load_config()['network']['device_controls_port']

# Thrusters
def get_user_max_thrust():
    return float(load_config()['thrusters']['user_max_thrust'])

def get_regulator_max_thrust():
    return float(load_config()['thrusters']['regulator_max_thrust'])

def get_thruster1_pin():
    return int(load_config()['thrusters']['thruster1_pin'])

def get_thruster2_pin():
    return int(load_config()['thrusters']['thruster2_pin'])

def get_thruster3_pin():
    return int(load_config()['thrusters']['thruster3_pin'])

def get_thruster4_pin():
    return int(load_config()['thrusters']['thruster4_pin'])

def get_thruster5_pin():
    return int(load_config()['thrusters']['thruster5_pin'])

def get_thruster6_pin():
    return int(load_config()['thrusters']['thruster6_pin'])

def get_thruster7_pin():    
    return int(load_config()['thrusters']['thruster7_pin'])

def get_thruster8_pin():
    return int(load_config()['thrusters']['thruster8_pin'])

# Regulator
def get_Kp_pitch():
    return float(load_config()['regulator']['Kp_pitch'])
def get_Ki_pitch():
    return float(load_config()['regulator']['Ki_pitch'])
def get_Kd_pitch():
    return float(load_config()['regulator']['Kd_pitch']) # HAS TO BE NEGATIVE.... WEIRD

def get_Kp_roll():
    return float(load_config()['regulator']['Kp_roll'])
def get_Ki_roll():
    return float(load_config()['regulator']['Ki_roll'])
def get_Kd_roll():
    return float(load_config()['regulator']['Kd_roll'])

def get_Kp_depth():
    return float(load_config()['regulator']['Kp_depth'])
def get_Ki_depth():
    return float(load_config()['regulator']['Ki_depth'])
def get_Kd_depth():
    return float(load_config()['regulator']['Kd_depth'])

def get_forward_speed_coefficient():
    return float(load_config()['regulator']['forward_speed_coefficient'])

def get_upward_speed_coefficient():
    return float(load_config()['regulator']['upward_speed_coefficient'])

def get_sideways_speed_coefficient():
    return float(load_config()['regulator']['sideways_speed_coefficient'])

def get_pitch_turn_coefficient():
    return float(load_config()['regulator']['pitch_turn_coefficient'])

def get_yaw_turn_coefficient():
    return float(load_config()['regulator']['yaw_turn_coefficient'])

def get_roll_turn_coefficient():
    return float(load_config()['regulator']['roll_turn_coefficient'])


def get_turn_speed():
    return float(load_config()['regulator']['turn_speed'])

# imu
def get_CF_alpha():
    return float(load_config()['imu']['CF_alpha'])

def get_GYRO_HPF_tau():
    return float(load_config()['imu']['GYRO_HPF_tau'])

# Pressure Sensor
def get_pressure_fluid():
    return load_config()['pressure']['fluid']

