# notebook.py

import marimo

app = marimo.App()


# Cell: email
@app.cell
def email_cell():
    from marimo import Markdown
    Markdown("**Email:** 23f2003651@ds.study.iitm.ac.in")


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


# ✅ Reactive dynamic Markdown
@app.cell
def dynamic_markdown(df, multiplier):
    from marimo import Markdown
    import numpy as np

    def render_markdown(mult_val):
        df_updated = df.copy()
        df_updated["x"] = df["x"] * mult_val
        df_updated["y"] = 3 * df_updated["x"] + np.random.normal(
            0, 3, size=df_updated.shape[0]
        )
        updated_mean_y = df_updated["y"].mean()
        return f"""
### Interactive Analysis
- Current multiplier: **{mult_val:.1f}**  
- Updated mean of y: **{updated_mean_y:.2f}**
"""

    # Make Markdown reactive to multiplier.value
    Markdown(lambda: render_markdown(multiplier.value))


if __name__ == "__main__":
    app.run()
