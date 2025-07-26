# erif_main_sim.py
# Main ERIF simulation runner

import numpy as np

def run_erif_sim(steps=100, alpha=0.1, beta=0.1):
    T = 0.5
    R = 0.5
    history = [(T, R)]
    for _ in range(steps):
        success = np.random.uniform(0, 1)
        entropy = np.random.uniform(0, 0.5)
        info_gain = np.random.uniform(0, 1)
        overload = np.random.uniform(0, 0.5)
        dT = alpha * (success - entropy)
        dR = beta * (info_gain - overload)
        T += dT
        R += dR
        history.append((T, R))
    return history

if __name__ == "__main__":
    history = run_erif_sim()
    print("Simulation history (T, R):", history[:5])