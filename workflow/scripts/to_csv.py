import pandas as pd


def save_to_csv(to_csv: dict, path_to_output: str):
    df = pd.Series(to_csv)
    df.to_csv(path_to_output)


if __name__ == "__main__":
    save_to_csv(
        to_csv=snakemake.params.to_csv,
        path_to_output=snakemake.output[0],
    )
