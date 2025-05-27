import pandas as pd
import ast

# Load TSLA data
df = pd.read_csv("TSLA_data.csv")

# Format Support/Resistance as stringified lists
def format_list(val):
    try:
        parsed = ast.literal_eval(str(val))
        if isinstance(parsed, list):
            return str([round(float(v), 2) for v in parsed])
    except:
        return "[]"

df["Support"] = df["Support"].apply(format_list)
df["Resistance"] = df["Resistance"].apply(format_list)

# Fill missing direction with "NONE"
df["direction"] = df["direction"].fillna("NONE").str.upper()

# Rearranged and renamed columns if needed
df_final = df[["timestamp", "open", "high", "low", "close", "direction", "Support", "Resistance"]]

# Save cleaned version
df_final.to_csv("TSLA_data_final.csv", index=False)
print("✅ Converted and saved as TSLA_data_final.csv")
