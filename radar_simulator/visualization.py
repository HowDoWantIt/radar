import matplotlib.pyplot as plt
import numpy as np

def plot_radar(targets, detected_targets, radar_range):
    plt.figure(figsize=(8, 8))
    plt.xlim(-radar_range, radar_range)
    plt.ylim(-radar_range, radar_range)
    plt.xlabel("X (meters)")
    plt.ylabel("Y (meters)")
    plt.title("Radar Display")

    for target in targets:
        plt.plot(target.position[0], target.position[1], 'ro', label='Target')

    for echo in detected_targets:
        t = echo["target"]
        plt.plot(t.position[0], t.position[1], 'go', label='Detected Target')

    plt.grid(True)
    plt.show()
