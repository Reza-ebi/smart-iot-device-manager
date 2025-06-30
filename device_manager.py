import json
from device import Device
from rules import EnergyOptimizer

class DeviceManager:
    def __init__(self):
        self.devices = []

    def load_devices(self, path):
        with open(path, "r") as file:
            data = json.load(file)
            for d in data["devices"]:
                device = Device(d["name"], d["power_watts"], d["usage_hours_per_day"])
                self.devices.append(device)

    def display_status(self):
        print("📊 Current Device Status:")
        for dev in self.devices:
            print(dev)
        print()

    def apply_energy_rules(self):
        print("🧠 Applying Smart Energy Rules...")
        optimizer = EnergyOptimizer()
        for device in self.devices:
            action = optimizer.optimize(device)
            if action == "TURN_OFF":
                device.status = "OFF"
        print("\n⚙️ Updated Device Status:")
        for dev in self.devices:
            print(dev)
