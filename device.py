class Device:
    def __init__(self, name, power_watts, usage_hours_per_day):
        self.name = name
        self.power = power_watts
        self.usage_hours = usage_hours_per_day
        self.status = "ON"

    def daily_consumption(self):
        return self.power * self.usage_hours  # in Wh

    def __str__(self):
        return f"{self.name}: {self.status}, {self.daily_consumption()} Wh/day"
