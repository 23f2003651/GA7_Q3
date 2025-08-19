# Email: 23f2003651@ds.study.iitm.ac.in
# Interactive Data Analysis Notebook
# Demonstrates relationship between variables with interactive widgets

# Cell 1: Import libraries and generate dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider
from IPython.display import display, Markdown

# Seed for reproducibility
np.random.seed(42)

# Generate sample dataset
x = np.linspace(0, 10, 100)
y = 3 * x + np.random.normal(0, 3, size=x.shape)  # dependent on x
z = 2 * x**2 + np.random.normal(0, 5, size=x.shape)  # dependent on x

# Store in DataFrame for easy manipulation
df = pd.DataFrame({'x': x, 'y': y, 'z': z})

# Show first few rows
df.head()

# Cell 2: Function to plot variables based on slider input
def plot_data(multiplier=1):
    """
    Plots y and z vs x, applying multiplier to y.
    Demonstrates variable dependency: y_scaled depends on slider value.
    """
    y_scaled = df['y'] * multiplier  # variable dependency
    
    plt.figure(figsize=(10, 5))
    plt.plot(df['x'], y_scaled, label=f'y_scaled = y * {multiplier}')
    plt.plot(df['x'], df['z'], label='z')
    plt.xlabel('x')
    plt.ylabel('Values')
    plt.title('Interactive Relationship between Variables')
    plt.legend()
    plt.show()
    
    # Dynamic markdown output
    display(Markdown(f"**Slider Multiplier:** {multiplier}  \n**Mean of y_scaled:** {y_scaled.mean():.2f}"))
    
# Create interactive slider
interact(plot_data, multiplier=IntSlider(value=1, min=1, max=10, step=1, description='Multiplier'));
