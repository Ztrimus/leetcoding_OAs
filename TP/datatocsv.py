import pandas as pd
import os

def read_data_file(file_path):
    encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
    
    for encoding in encodings:
        try:
            # Try reading the file with current encoding
            df = pd.read_csv(file_path, header=None, encoding=encoding)
            print(f"Successfully read {file_path} with {encoding} encoding")
            return df
        except Exception as e:
            print(f"Failed to read with {encoding} encoding: {str(e)}")
            
            try:
                # If that fails, try reading with different separator
                df = pd.read_csv(file_path, sep='\s+', header=None, encoding=encoding)
                print(f"Successfully read {file_path} with {encoding} encoding and whitespace separator")
                return df
            except Exception as e:
                print(f"Failed to read with {encoding} encoding and whitespace separator: {str(e)}")
    
    print(f"Failed to read {file_path} with all attempted encodings")
    return None

# Directory containing the .data files
data_directory = "/Users/saurabh/Downloads/heart+disease"

# List all .data files in the directory
data_files = [f for f in os.listdir(data_directory) if f.endswith('.data')]

# Read each .data file
for file in data_files:
    file_path = os.path.join(data_directory, file)
    df = read_data_file(file_path)
    
    if df is not None:
        print(f"Successfully read {file}")
        print(df.head())  # Display the first few rows
        print("\n")

        # Optionally, save as CSV
        csv_file = file_path.replace('.data', '.csv')
        df.to_csv(csv_file, index=False)
        print(f"Saved as {csv_file}")
    else:
        print(f"Failed to read {file}")

    print("-" * 50)