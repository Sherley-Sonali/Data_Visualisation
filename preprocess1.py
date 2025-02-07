import pandas as pd
import re

# Function to convert time string to total seconds
def time_to_seconds(time_str):
    parts = time_str.split(":")
    if len(parts) == 3:  # HH:MM:SS
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])
    elif len(parts) == 2:  # MM:SS.sss or SS.sss
        return int(parts[0]) * 60 + float(parts[1])
    else:  # SS.sss
        return float(parts[0])

# Read the input file
with open("event_results.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Initialize variables
data = []
current_event = None
current_category = None

# Process each line
for line in lines:
    line = line.strip()

    # Detect event names (assume they have no indentation and are in title case)
    if re.match(r"^\(\d+\)\s", line):  
        current_event = line.split(") ")[1]  # Extract event name
        continue

    # Detect category (e.g., "Male 0-22")
    if re.match(r"^(Male|Female)\s\d", line):
        current_category = line
        continue

    # Detect race times (format: "1 169 Souryan Dubois 4:35:45")
    match = re.match(r"^\d+\s+\d+\s+[\w\s-]+\s+([\d:]+(?:\.\d+)?)", line)
    if match:
        time_str = match.group(1)  # Extract time
        data.append([current_event, current_category, time_to_seconds(time_str)])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Event", "Category", "Time (sec)"])

# Compute average time and performance score
df_grouped = df.groupby(["Event", "Category"]).agg({"Time (sec)": "mean"}).reset_index()
df_grouped.rename(columns={"Time (sec)": "Avg Time (sec)"}, inplace=True)

# Compute Performance Score (1 / Avg Time)
df_grouped["Performance Score"] = 1 / df_grouped["Avg Time (sec)"]

# Save to CSV
df_grouped.to_csv("preprocess1.csv", index=False)

print("✅ CSV file generated: performance_data.csv")
