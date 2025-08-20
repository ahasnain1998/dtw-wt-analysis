import pandas as pd
import os

# Directory path where the CSV files are located
directory = '/media/obiwan/Elements/Sohraby/TauRAMD-MainRun/CO/WT/TIT-WT/contacts_chain_B'

# Initialize a list to store the results
results = []

# Iterate over each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Read the CSV file
        filepath = os.path.join(directory, filename)
        df = pd.read_csv(filepath)

        # Get the column names for the residue contacts (excluding 'Frame.#' columns)
        residue_columns = [col for col in df.columns if not col.startswith('Frame.')]

        # Initialize a dictionary to store the counts for the current file
        file_counts = {'Filename': filename}

        # Count the number of non-zero values for each column in the current file
        for column in residue_columns:
            non_zero_count = (df[column] != 0).sum()
            file_counts[column] = non_zero_count

        # Append the counts for the current file to the results list
        results.append(file_counts)

# Create a DataFrame from the results list
results_df = pd.DataFrame(results)

# Write the results to a new CSV file (excluding 'Frame.#' columns)
results_df.to_csv('counts_results-wT-B.csv', index=False, columns=residue_columns.insert(0, 'Filename'))

