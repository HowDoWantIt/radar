# Radar Simulator by IDC

This is a modular and extensible radar simulator developed by **IDC**, implemented entirely in Python.  
It is designed for simulation of radar pulses, moving targets, and signal detection in a customizable environment.

---

## 🚀 Features

- 📡 Simulates radar pulses and echo returns
- 🎯 Models moving targets with position and velocity
- 🔊 Adds noise and detection thresholds to signals
- 🧭 Real-time radar display with target detection visualization
- 🧩 Fully modular structure (easy to extend)

---

## 🛠 Installation

Using `pip`:

---


flowchart TD
    Start[Start Program] --> LoadConfig[Load Radar Settings]
    LoadConfig --> CreateTargets[Create Moving Targets]
    CreateTargets --> SimulatePulse[Simulate Radar Pulse]
    SimulatePulse --> ReceiveEcho[Receive Echo Signal]
    ReceiveEcho --> ProcessSignal[Process Signal]
    ProcessSignal --> DetectTarget{Target Detected?}
    DetectTarget -->|Yes| DisplayTarget[Display Target]
    DetectTarget -->|No| ContinueSim[Continue Simulation]
    DisplayTarget --> ContinueSim
    ContinueSim --> StopSim{Stop Simulation?}
    StopSim -->|No| CreateTargets
    StopSim -->|Yes| End[End Program]


```bash
pip install -r requirements.txt
