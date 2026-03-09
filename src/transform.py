import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic transformations:
    - Convert fecha to datetime
    - Create total_animales column
    """

    # Convert fecha column to datetime
    df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m")

    # List of animal category columns (según tu dataset real)
    animal_columns = [
        "vaca",
        "vaquillona",
        "novillo",
        "novillito",
        "ternero",
        "ternera",
        "torito",
        "toro",
        "bueyes"
    ]

    # Create total_animales column
    df["total_animales"] = df[animal_columns].sum(axis=1)

    print("Transformation completed.")
    print("New shape:", df.shape)

    return df


def summarize_by_month_province(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group by month and provincia_origen, summing total_animales.
    """

    # Ensure fecha is datetime
    if not pd.api.types.is_datetime64_any_dtype(df["fecha"]):
        df = df.copy()
        df["fecha"] = pd.to_datetime(df["fecha"])

    # Create year-month period
    df["year_month"] = df["fecha"].dt.to_period("M")

    grouped = (
        df
        .groupby(["year_month", "provincia_origen"], dropna=False)["total_animales"]
        .sum()
        .reset_index()
    )

    # Convert period back to timestamp (optional but cleaner)
    grouped["year_month"] = grouped["year_month"].dt.to_timestamp()

    print("Aggregation completed.")
    print("Aggregated shape:", grouped.shape)

    return grouped