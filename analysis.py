# notebook.py

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

    np.random.seed(0)
    x = np.linspace(0, 10, 100)
    y = 3 * x + np.random.normal(0, 3, size=x.shape)

    df = pd.DataFrame({"x": x, "y": y})
    return df


# Cell: data_analysis
@app.cell
def data_analysis(df):
    mean_y = df["y"].mean()
    std_y = df["y"].std()
    return mean_y, std_y


# Cell: slider_widget
@app.cell
def slider_widget():
    import marimo as mo

    multiplier = mo.ui.slider(
        start=0.5,
        stop=3.0,
        step=0.1,
        value=1.0,
        label="Multiplier"
    )
    return multiplier


# ✅ Cell: dynamic_markdown (reactive)
@app.cell
def dynamic_markdown(df, multiplier):
    from marimo import Markdown
    import numpy as np

    # This updates whenever multiplier.value changes
    df_updated = df.copy()
    df_updated["x"] = df["x"] * multiplier.value
    df_updated["y"] = 3 * df_updated["x"] + np.random.normal(
        0, 3, size=df_updated.shape[0]
    )

    updated_mean_y = df_updated["y"].mean()

    # Dynamic markdown content
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
