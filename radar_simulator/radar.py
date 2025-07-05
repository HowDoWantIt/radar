import numpy as np
from .config import SPEED_OF_LIGHT

class Radar:
    def __init__(self, range_m, pulse_width_s, pulse_repetition_interval_s, antenna_beamwidth_deg):
        self.range = range_m
        self.pulse_width = pulse_width_s
        self.pri = pulse_repetition_interval_s
        self.beamwidth = antenna_beamwidth_deg

    def send_pulse(self, time):
        """Simulate sending a radar pulse at a given time"""
        return {"time": time, "pulse_width": self.pulse_width}

    def receive_echo(self, targets, pulse_time):
        """Simulate receiving echoes from targets within range"""
        echoes = []
        for target in targets:
            distance = np.linalg.norm(target.position)
            round_trip_time = 2 * distance / SPEED_OF_LIGHT
            if round_trip_time <= self.range / SPEED_OF_LIGHT:
                strength = target.reflectivity / (distance ** 2 + 1e-6)
                echoes.append({"target": target, "time": pulse_time + round_trip_time, "strength": strength})
        return echoes
