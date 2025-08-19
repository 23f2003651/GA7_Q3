# analysis.py
# Author: 23f2003651@ds.study.iitm.ac.in
# Description: Interactive data analysis notebook demonstrating relationships between variables

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider
from IPython.display import display, Markdown

# --------------------------
# Cell 1: Generate dataset
# --------------------------
# Creating a synthetic dataset with two variables x and y
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = 3*x + np.random.normal(0, 3, 100)  # y depends on x

df = pd.DataFrame({'x': x, 'y': y})

# Display first few rows
print("Dataset preview:")
print(df.head())

# --------------------------
# Cell 2: Interactive slider
# --------------------------
# The slider selects a subset of data based on x threshold
def filter_data(threshold=5):
    """
    Filters the dataset where x <= threshold and updates the plot and markdown output
    """
    filtered = df[df['x'] <= threshold]

    # Plotting the filtered data
    plt.figure(figsize=(8,5))
    plt.scatter(filtered['x'], filtered['y'], color='blue')
    plt.plot(filtered['x'], 3*filtered['x'], color='red', linestyle='--', label='y = 3*x')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Scatter plot for x <= {threshold}')
    plt.legend()
    plt.show()

    # Dynamic markdown output
    mean_y = filtered['y'].mean()
    display(Markdown(f"**Dynamic analysis:** For x ≤ {threshold}, mean of y = {mean_y:.2f}"))

# Creating the interactive widget
interact(filter_data, threshold=IntSlider(min=0, max=10, step=1, value=5))
