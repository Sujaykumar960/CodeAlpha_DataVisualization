import pandas as pd
import matplotlib.pyplot as plt

# Load Excel
Excel_File_path = input("Enter Excel file path: ").strip('"').strip("'")

try:
    df = pd.read_excel(Excel_File_path)
    print("\n Excel File loaded successfully!\n")
except Exception as e:
    print(f" Error loading file: {e}")
    exit()

print(" Preview of First 5 rows of the Data:")
print(df.head())

# Select filter columns
print("\nAvailable columns in DataTable :")
print(df.columns.tolist())
selected_cols = input("Enter column names to filter (comma-separated): ").split(',')
selected_cols = [col.strip() for col in selected_cols if col.strip() in df.columns]

filters = {}
for col in selected_cols:
    unique_values = df[col].dropna().unique()
    print(f"\nValues in '{col}': {list(unique_values)}")
    val = input(f"Enter values to filter '{col}' (comma-separated, or press Enter to skip): ").strip()
    if val:
        filters[col] = [v.strip() for v in val.split(',')]

filtered_df = df.copy()
for col, val_list in filters.items():
    filtered_df = filtered_df[filtered_df[col].astype(str).str.lower().isin([v.lower() for v in val_list])]


# Choose chart
print("\n Chart options: bar, column, line, pie, area")
chart_type = input("Chart type: ").strip().lower()

# Axis selection
print("\nColumns:")
print(df.columns.tolist())

x_col = input("X-axis (categorical or numeric): ").strip()
y_col = input("Y-axis (numeric): ").strip()

if x_col not in filtered_df.columns or y_col not in filtered_df.columns:
    print(" Invalid column selection.")
    exit()

# Group and Plot
grouped_df = filtered_df.groupby(x_col)[y_col].sum().reset_index()

plt.figure(figsize=(10, 6))

if chart_type in ['bar', 'column']:
    plt.bar(grouped_df[x_col], grouped_df[y_col])
elif chart_type == 'line':
    plt.plot(grouped_df[x_col], grouped_df[y_col], marker='o')
elif chart_type == 'area':
    plt.fill_between(grouped_df[x_col], grouped_df[y_col])
elif chart_type == 'pie':
    plt.pie(grouped_df[y_col], labels=grouped_df[x_col], autopct='%1.1f%%')
else:
    print(" Unsupported chart type.")
    exit()

plt.title(f"{chart_type.capitalize()} Chart of {y_col} by {x_col}")
if chart_type != 'pie':
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.xticks(rotation=45)

plt.tight_layout()
plt.show()