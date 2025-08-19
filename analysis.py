# analysis.py
# Author: 23f2003651@ds.study.iitm.ac.in

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Interactive widgets for Marimo/Jupyter
try:
    from ipywidgets import interact, IntSlider
    from IPython.display import display, Markdown
except ImportError:
    raise ImportError("ipywidgets and IPython are required for interactive slider.")

# --------------------------
# Cell 1: Generate dataset
# --------------------------
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = 3*x + np.random.normal(0, 3, 100)

df = pd.DataFrame({'x': x, 'y': y})

# Display dataset
print("Dataset preview:")
print(df.head())

# --------------------------
# Cell 2: Interactive slider
# --------------------------
def update(threshold=5):
    """
    Filter dataset and display results interactively
    """
    filtered = df[df['x'] <= threshold]

    # Plot
    plt.figure(figsize=(8,5))
    plt.scatter(filtered['x'], filtered['y'], color='blue')
    plt.plot(filtered['x'], 3*filtered['x'], color='red', linestyle='--', label='y = 3*x')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Scatter plot for x ≤ {threshold}')
    plt.legend()
    plt.show()

    # Dynamic Markdown
    mean_y = filtered['y'].mean()
    display(Markdown(f"**Dynamic analysis:** For x ≤ {threshold}, mean of y = {mean_y:.2f}"))

# Slider widget
slider = IntSlider(value=5, min=0, max=10, step=1, description='x threshold')
interact(update, threshold=slider)
