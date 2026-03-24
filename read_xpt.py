"""XPT (SAS Transport) dosyasını okuyup içeriğini görüntüleyen script."""

import argparse
import sys

import pandas as pd


def read_xpt(filepath: str) -> pd.DataFrame:
    """Read an XPT (SAS Transport) file and return a DataFrame.

    Parameters
    ----------
    filepath : str
        Path to the .xpt file.

    Returns
    -------
    pd.DataFrame
        Contents of the XPT file as a DataFrame.
    """
    df = pd.read_sas(filepath, format="xport", encoding="utf-8")
    return df


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Read and display the contents of an XPT (SAS Transport) file."
    )
    parser.add_argument(
        "filepath",
        nargs="?",
        default="data.xpt",
        help="Path to the .xpt file (default: data.xpt)",
    )
    args = parser.parse_args()

    try:
        df = read_xpt(args.filepath)
    except FileNotFoundError:
        print(f"Error: '{args.filepath}' not found.")
        sys.exit(1)
    except Exception as exc:
        print(f"Error reading '{args.filepath}': {exc}")
        sys.exit(1)

    print(f"File: {args.filepath}")
    print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
    print(f"Columns: {list(df.columns)}")
    print()
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
