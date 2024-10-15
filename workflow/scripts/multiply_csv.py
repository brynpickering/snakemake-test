import pandas as pd


def multiply_csv_values(to_multiply: str, multiplier: int, path_to_output: str):
    df = pd.read_csv(to_multiply, index_col=0)
    df *= multiplier
    df.to_csv(path_to_output)


if __name__ == "__main__":
    multiply_csv_values(
        to_multiply=snakemake.input.to_multiply,
        multiplier=int(snakemake.wildcards.multiplier),
        path_to_output=snakemake.output.multiplied,
    )
