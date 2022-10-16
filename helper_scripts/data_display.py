import pandas as pd
from IPython.display import HTML, display


def show_largest(data: pd.DataFrame, col: str, top_n: int = 10):
    return pd.DataFrame(data.sum() / data.shape[0], columns=[col]).nlargest(top_n, col)


def display_side_by_side(dfs: list, captions: list):
    """Display tables side by side to save vertical space
    Input:
        dfs: list of pandas.DataFrame
        captions: list of table captions

    Credit:
    https://stackoverflow.com/questions/38783027/
    jupyter-notebook-display-two-pandas-tables-side-by-side
    """
    output = ""
    combined = dict(zip(captions, dfs))
    for caption, df in combined.items():
        output += (
            df.style.set_table_attributes("style='display:inline'")
            .set_caption(caption)
            ._repr_html_()
        )
        output += "\xa0\xa0\xa0"
    display(HTML(output))


def main():
    return ()


if __name__ == "__main__":
    main()
