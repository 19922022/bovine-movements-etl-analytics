import os
from extract import load_csv
from transform import transform_data, summarize_by_month_province

# Extract
df = load_csv("movimiento-bovinos-2018.csv")

# Transform
df = transform_data(df)

# Aggregate
df_agg = summarize_by_month_province(df)

# Preview
print("\nFirst 5 rows after aggregation:")
print(df_agg.head())


output_path = os.path.join("data", "processed")

# Create folder if it doesn't exist
os.makedirs(output_path, exist_ok=True)

file_output = os.path.join(output_path, "movimientos_bovinos_mensual_provincia.csv")

df_agg.to_csv(file_output, index=False)

print(f"\nFile saved successfully at {file_output}")