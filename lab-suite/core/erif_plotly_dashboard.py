# erif_plotly_dashboard.py
# Real-time ERIF T/R dashboard with Plotly

import plotly.graph_objects as go
import numpy as np

def generate_dashboard(steps=50):
    T = np.cumsum(np.random.normal(0, 0.1, steps)) + 0.5
    R = np.cumsum(np.random.normal(0, 0.1, steps)) + 0.5
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=T, y=R, mode='lines+markers', name='Mind Path'))
    fig.update_layout(title='ERIF Real-Time Dashboard',
                      xaxis_title='Stability (T)',
                      yaxis_title='Integration (R)')
    fig.show()

if __name__ == "__main__":
    generate_dashboard()