import json
import os
from thrusters import Thrusters
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rov_types import IMUData, PressureData, ROVConfig, RegulatorData


class ROVState:
    config_path: str
    rov_config: "ROVConfig"
    imu: "IMUData"
    pressure: "PressureData"
    pitch_stabilization: bool
    roll_stabilization: bool
    depth_stabilization: bool
    regulator: "RegulatorData"
    battery_percentage: int
    thrusters: Thrusters

    def __init__(self) -> None:
        self.config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(self.config_path, "r") as f:
            self.rov_config: "ROVConfig" = json.load(f)

        self.imu: "IMUData" = {"acceleration": 0.0, "gyroscope": 0.0, "temperature": 0.0}
        self.pressure: "PressureData" = {
            "pressure": 0.0,
            "temperature": 0.0,
            "depth": 0.0,
        }
        self.regulator: "RegulatorData" = {
            "pitch": 0.0,
            "roll": 0.0,
            "desiredPitch": 0.0,
            "desiredRoll": 0.0,
        }
        self.pitch_stabilization = False
        self.roll_stabilization = False
        self.depth_stabilization = False
        self.battery_percentage = 100
        self.thrusters = Thrusters(self)

    def set_config(self, config: "ROVConfig") -> None:
        self.rov_config = config
        with open(self.config_path, "w") as f:
            json.dump(config, f, indent=2)
