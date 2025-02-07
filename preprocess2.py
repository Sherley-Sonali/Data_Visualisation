import pandas as pd
import re

# Load CSV file
df = pd.read_csv("preprocess1.csv")

# Function to extract age group (removing gender)
def extract_age_group(category):
    return re.sub(r'^(Male|Female)\s+', '', category)  # Remove "Male " or "Female "

# Apply transformation
df["Category"] = df["Category"].apply(extract_age_group)

# Group by Event and Age Group, then average the time and performance score
df_combined = df.groupby(["Event", "Category"]).agg({
    "Avg Time (sec)": "mean",
    "Performance Score": "mean"
}).reset_index()

# Save to new CSV
df_combined.to_csv("preprocess2.csv", index=False)

print("✅ Processed CSV generated: preprocess2.csv")
