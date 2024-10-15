from pathlib import Path


def save_to_print(to_print: str, path_to_output: str):
    Path(path_to_output).write_text(to_print)


if __name__ == "__main__":
    save_to_print(
        to_print=snakemake.params.to_print,
        path_to_output=snakemake.output[0],
    )
