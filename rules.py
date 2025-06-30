class EnergyOptimizer:
    def optimize(self, device):
        # Rule-based: turn off if consumption > 1000 Wh/day
        consumption = device.daily_consumption()
        if consumption > 1000:
            return "TURN_OFF"
        return "KEEP_ON"
