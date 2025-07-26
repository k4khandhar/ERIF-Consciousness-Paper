# erif_python_netlogo_bridge.py
# Bridge for running ERIF simulations in NetLogo from Python
# Requires pyNetLogo (pip install pyNetLogo) and NetLogo installed

import pyNetLogo
import numpy as np

def run_erif_bridge(model_path, steps=100):
    nl = pyNetLogo.NetLogoLink(gui=False)
    nl.load_model(model_path)
    nl.command('setup')
    
    T_values = []
    R_values = []
    for _ in range(steps):
        nl.command('go')
        T = nl.report('mean [stability] of turtles')
        R = nl.report('mean [integration] of turtles')
        T_values.append(T)
        R_values.append(R)
    
    nl.kill_workspace()
    return np.array(T_values), np.array(R_values)

if __name__ == "__main__":
    T, R = run_erif_bridge('path/to/erif_agents.nlogo')
    print("Simulation complete! T:", T[:5], "R:", R[:5])