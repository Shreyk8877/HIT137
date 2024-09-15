import pandas as pd

def extract_text_from_csv_files(file_paths, output_file):
    # Open the output text file in write mode
    with open(output_file, 'w') as txt_file:
        # Loop through each specified file path
        for file_path in file_paths:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)
            
            # Iterate over each column in the DataFrame
            for column in df.columns:
                # Check if the column contains text data
                if df[column].dtype == 'object':
                    # Write each text entry to the output file
                    for text in df[column].dropna():
                        txt_file.write(str(text) + '\n')

if __name__ == "__main__":
    # Specify the paths to the CSV files
    csv_files = [
        'CSV1.csv',
        'CSV2.csv',
        'CSV3.csv',
        'CSV4.csv'
    ]
    
    # Specify the output text file path
    output_txt_file = 'CSV_file.txt'
    
    # Call the function to extract text and store it in the .txt file
    extract_text_from_csv_files(csv_files, output_txt_file)