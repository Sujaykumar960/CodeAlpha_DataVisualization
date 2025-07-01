import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load Excel File
# Ask user for the file path and load the Excel data into a DataFrame using pandas

Excel_File_path = input("Enter Excel file path: ").strip('"').strip("'")

try:
    df = pd.read_excel(Excel_File_path)
    print("\n Excel File loaded successfully!\n")

except Exception as e:
    print(f" Error loading file: {e}")
    exit()

#  Preview Data
print(" Preview of First 5 rows of the Data:")
print(df.head())

print("\nAvailable columns in DataTable :")    # Step 2: Select Columns to Filter
print(df.columns.tolist())

selected_cols = input("Enter column names to filter (comma-separated): ").split(',')
selected_cols = [col.strip() for col in selected_cols if col.strip() in df.columns]

filters = {}   # Step 3: Apply Filters on Selected Columns
for col in selected_cols:
    unique_values = df[col].dropna().unique()
    print(f"\nValues in '{col}': {list(unique_values)}")
    val = input(f"Enter values to filter '{col}' (comma-separated, or press Enter to skip): ").strip()
    if val:
        filters[col] = [v.strip() for v in val.split(',')]

# Apply filtering to DataFrame
filtered_df = df.copy()
for col, val_list in filters.items():
    filtered_df = filtered_df[filtered_df[col].astype(str).str.lower().isin([v.lower() for v in val_list])]


print("\n Chart options: bar, column, line, pie, area")   # Step 4: Choose Chart Type
chart_type = input("Chart type: ").strip().lower()

# Step 5: Select X and Y Axes ---
# User selects two columns for plotting:
#  X-axis: Categorical 
#  Y-axis: Numerical data to visualize 
print("\nAvailable columns for plotting: ")
print(df.columns.tolist())

x_col = input("X-axis (categorical or numeric): ").strip()
y_col = input("Y-axis (numeric): ").strip()

if x_col not in filtered_df.columns or y_col not in filtered_df.columns:
    print(" Invalid column selection.")
    exit()

grouped_df = filtered_df.groupby(x_col)[y_col].sum().reset_index()   # Step 6: Group Data for Visualization

plt.figure(figsize=(10, 6))   # Step 7: Plotting the Chart

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

# Add chart details
plt.title(f"{chart_type.capitalize()} Chart of {y_col} by {x_col}")

if chart_type != 'pie':
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

