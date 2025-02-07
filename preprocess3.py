import pandas as pd
import re

# Load CSV file
df = pd.read_csv("removed_+.csv")

# Define function to map age groups into broader categories
def merge_age_groups(category):
    age = re.findall(r'\d+', category)  # Extract numbers from category
    if not age:
        return category  # Return as is if no digits (e.g., "Elite", "Advanced")
    
    age = int(age[0])  # Convert first number to integer
    if age <= 10:
        return "0-10"
    elif age <= 20:
        return "11-20"
    elif age <= 30:
        return "21-30"
    elif age <= 40:
        return "31-40"
    elif age <= 50:
        return "41-50"
    else:
        return "51+"

# Apply the function to categorize age groups
df["Merged Category"] = df["Category"].apply(merge_age_groups)

# Group by Event and new age group, then average the values
df_merged = df.groupby(["Event", "Merged Category"]).agg({
    "Avg Time (sec)": "mean",
    "Performance Score": "mean"
}).reset_index()

# Save to new CSV
df_merged.to_csv("final.csv", index=False)

print("✅ Processed CSV generated: final.csv")
