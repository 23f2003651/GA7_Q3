# 23f2003651@ds.study.iitm.ac.in
# Interactive Marimo Notebook: Exploring Relationship Between x and y

# Cell 1: Data Initialization
import numpy as np
import pandas as pd

# Generate synthetic dataset
np.random.seed(42)
x = np.linspace(0, 10, 50)                # Independent variable
noise = np.random.normal(0, 2, size=x.size)
y = 2 * x + 5 + noise                     # Dependent variable (linear relationship with noise)

# Create DataFrame
df = pd.DataFrame({"x": x, "y": y})

# Cell 2: Interactive Slider Widget
import marimo as mo

# Slider to select slope multiplier dynamically
slope_slider = mo.ui.slider(1, 5, value=2)  # initial slope = 2

# Cell 3: Dependent Variable Update
# This cell depends on slope_slider
adjusted_y = slope_slider.value * x + 5 + noise

# Cell 4: Dynamic Markdown Output
# Display the current slope and a small visual bar
mo.md(f"### Current slope: {slope_slider.value}\n" + "🟢" * slope_slider.value)

# Cell 5: Data Visualization
import matplotlib.pyplot as plt

# Plot original y vs x and adjusted_y vs x
plt.figure(figsize=(8, 4))
plt.scatter(x, y, label="Original y", color="blue")
plt.plot(x, adjusted_y, label=f"Adjusted y (slope={slope_slider.value})", color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interactive Slope Adjustment")
plt.legend()
plt.show()

# Comments:
# - Changing the slope_slider will automatically update adjusted_y and the plot.
# - Cell dependencies: slope_slider → adjusted_y → plot & markdown.
# - This demonstrates reactive programming in Marimo, similar to a spreadsheet.
