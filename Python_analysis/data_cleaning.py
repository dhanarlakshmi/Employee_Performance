import pandas as pd
import os

# Folder where your raw CSVs are
raw_folder = r"C:\Users\dhana\OneDrive\Desktop\Employee_Performance\Data\Raw"

# Load CSVs
employee_df = pd.read_csv(os.path.join(raw_folder, "Employee_Table.csv"))
attrition_df = pd.read_csv(os.path.join(raw_folder, "Attrition_Table.csv"))
performance_df = pd.read_csv(os.path.join(raw_folder, "Performance_Table.csv"))

# ---- Cleaning Steps ----
def clean_df(df):
    df.columns = df.columns.str.strip()  # Remove spaces from column names
    df = df.drop_duplicates()            # Remove duplicate rows
    df = df.fillna("")                    # Replace missing values with empty string
    return df

employee_df = clean_df(employee_df)
attrition_df = clean_df(attrition_df)
performance_df = clean_df(performance_df)

# Save cleaned CSVs in a new folder
clean_folder = r"C:\Users\dhana\OneDrive\Desktop\Employee_Performance\Data\Clean"
os.makedirs(clean_folder, exist_ok=True)

employee_df.to_csv(os.path.join(clean_folder, "Employee_Table_Clean.csv"), index=False)
attrition_df.to_csv(os.path.join(clean_folder, "Attrition_Table_Clean.csv"), index=False)
performance_df.to_csv(os.path.join(clean_folder, "Performance_Table_Clean.csv"), index=False)

print("All CSVs cleaned and saved successfully in 'Data\\Clean' ✅")
