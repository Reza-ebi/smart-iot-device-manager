from device_manager import DeviceManager

if __name__ == "__main__":
    print("🔌 Smart IoT Device Manager Started...\n")

    manager = DeviceManager()
    manager.load_devices("data/devices.json")

    manager.display_status()
    manager.apply_energy_rules()
