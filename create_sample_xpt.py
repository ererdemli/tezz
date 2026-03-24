"""data.xpt örnek dosyasını oluşturan yardımcı script."""

import pandas as pd
import pyreadstat


def main() -> None:
    data = {
        "ID": [1, 2, 3, 4, 5],
        "NAME": ["Ali", "Ayse", "Mehmet", "Fatma", "Emre"],
        "AGE": [25, 30, 35, 28, 42],
        "SCORE": [85.5, 92.3, 78.1, 95.0, 88.7],
    }

    df = pd.DataFrame(data)
    pyreadstat.write_xport(df, "data.xpt", file_format_version=5)
    print("data.xpt created successfully.")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
