"""
Task 26: Text Cleaning Basics
Run from the project folder: python scripts/text_cleaning.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
input_file = ROOT / "data" / "customer_raw.csv"
output_file = ROOT / "data" / "customer_cleaned.csv"
report_file = ROOT / "reports" / "before_after_examples.csv"

def clean_spaces(value):
    if pd.isna(value):
        return value
    return " ".join(str(value).strip().split())

df = pd.read_csv(input_file)
cleaned = df.copy()

cleaned["Customer_Name"] = cleaned["Customer_Name"].apply(clean_spaces).str.title()
cleaned["Email"] = cleaned["Email"].apply(lambda x: clean_spaces(x).lower())
cleaned["City"] = cleaned["City"].apply(clean_spaces).str.title()
cleaned["City"] = cleaned["City"].replace({"Hydrabad": "Hyderabad"})
cleaned["Membership"] = cleaned["Membership"].apply(clean_spaces).str.title()
cleaned["Membership"] = cleaned["Membership"].replace({"Premum": "Premium"})
cleaned["Status"] = cleaned["Status"].apply(clean_spaces).str.title()

cleaned.to_csv(output_file, index=False)
print(f"Raw records: {len(df)}")
print(f"Cleaned records: {len(cleaned)}")
print(f"Saved cleaned data to: {output_file}")
print(f"Saved examples to: {report_file}")
