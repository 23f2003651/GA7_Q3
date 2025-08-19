# notebook.py
# 23f2003651@ds.study.iitm.ac.in

import marimo

app = marimo.App()


# Cell: email
@app.cell
def email_cell():
    from marimo import Markdown
    Markdown("**Email:** 23f2003651@ds.study.iitm.ac.in")
    return

# Cell: data_initialization
@app.cell
def data_initialization():
    import numpy as np
    import pandas as pd

    # Generate example dataset with two variables
    np.random.seed(0)
    x = np.linspace(0, 10, 100)
    y = 3 * x + np.random.normal(0, 3, size=x.shape)

    df = pd.DataFrame({"x": x, "y": y})
    return df


# Cell: data_analysis
@app.cell
def data_analysis(df):
    # Using df from previous cell to compute statistics
    mean_y = df["y"].mean()
    std_y = df["y"].std()
    mean_y, std_y
    return mean_y, std_y


# ✅ Correct Cell: slider_widget
@app.cell
def slider_widget():
    import marimo as mo

    # Proper interactive slider widget
    multiplier = mo.ui.slider(
        start=0.5,
        stop=3.0,
        step=0.1,
        value=1.0,
        label="Multiplier"
    )
    multiplier  # display slider
    return multiplier


# Cell: dynamic_markdown
@app.cell
def dynamic_markdown(df, multiplier):
    from marimo import Markdown
    import numpy as np

    # Update dataset using multiplier interactively
    df_updated = df.copy()
    df_updated["x"] = df["x"] * multiplier.value
    df_updated["y"] = 3 * df_updated["x"] + np.random.normal(
        0, 3, size=df_updated.shape[0]
    )

    updated_mean_y = df_updated["y"].mean()

    Markdown(
        f"""
### Interactive Analysis  
- Current multiplier: **{multiplier.value:.1f}**  
- Updated mean of y: **{updated_mean_y:.2f}**
"""
    )
    return df_updated, updated_mean_y


if __name__ == "__main__":
    app.run()
