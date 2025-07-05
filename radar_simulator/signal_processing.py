import numpy as np

def apply_noise(signal_strength, noise_level=0.1):
    noise = np.random.normal(0, noise_level)
    return max(signal_strength + noise, 0)

def detect_targets(echoes, threshold=0.5):
    detected = [e for e in echoes if e["strength"] > threshold]
    return detected
