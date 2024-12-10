import pandas as pd
import time

# File paths
students_file_path = "students.csv"
fees_file_path = "student_fees.csv"

# Load the datasets
students_df = pd.read_csv(students_file_path)
fees_df = pd.read_csv(fees_file_path)

# Measure the start time
start_time = time.time()

# Extract the day from the Payment Date in the fees dataset
fees_df['Day'] = fees_df['Payment Date'].str.extract(r'(\d+)$').astype(int)

# Group by Student ID and calculate the most consistent payment day
consistent_payment_days = fees_df.groupby('Student ID')['Day'].agg(lambda x: x.mode()[0]).reset_index()
consistent_payment_days.rename(columns={'Day': 'Most Consistent Payment Day'}, inplace=True)

# Merge the consistent payment data with the student information
merged_df = pd.merge(students_df, consistent_payment_days, on='Student ID', how='inner')

# Measure the end time
end_time = time.time()
execution_time = end_time - start_time

# Display runtime and a preview of the merged dataset
print(f"Execution Time: {execution_time} seconds")
merged_df
