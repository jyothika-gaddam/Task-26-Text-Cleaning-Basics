# Task 26: Text Cleaning Basics

## Objective
Standardize customer names, spaces, capitalization, and common spelling variations using Python and Excel-compatible files.

## Dataset
The sample customer dataset contains 20 records and these columns:
- `Customer_ID`
- `Customer_Name`
- `Email`
- `City`
- `Membership`
- `Status`

## Cleaning performed
1. Removed leading and trailing whitespace.
2. Replaced repeated internal spaces with a single space.
3. Standardized customer names and city names to title case.
4. Converted email addresses to lowercase.
5. Standardized membership and status capitalization.
6. Corrected known variations: `Premum` → `Premium`, `Hydrabad` → `Hyderabad`.

> Note: spelling corrections are rule-based examples. For real business data, confirm unusual spellings against an approved reference list before changing them.

## Files
- `data/customer_raw.csv` — original messy sample data.
- `data/customer_cleaned.csv` — cleaned output.
- `reports/before_after_examples.csv` — examples of changes.
- `scripts/text_cleaning.py` — reproducible Python cleaning script.
- `Task26_Text_Cleaning_Basics.xlsx` — workbook with Raw Data, Cleaned Data, and Before-After Examples sheets.

## Run with Python
Install pandas if needed:
```bash
pip install pandas
```
Run from this project folder:
```bash
python scripts/text_cleaning.py
```

## Excel functions to practice
- `=TRIM(A2)` removes leading/trailing and extra ordinary spaces.
- `=PROPER(A2)` standardizes capitalization for names.
- `=LOWER(A2)` converts email text to lowercase.
- `=UPPER(A2)` converts text to uppercase.

Excel's `TRIM` does not remove every possible non-breaking space, so inspect imported data when results look unusual.

## Result
- Original records: 20
- Cleaned records: 20
- Records removed: 0 (this task standardizes text; it is not a deduplication task)
