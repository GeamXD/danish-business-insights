import pandas as pd

def check_duplicates(file_path):
    # Read the txt file into a Pandas DataFrame
    df = pd.read_csv(file_path, names=['urls'])
    
    # Check for duplicates
    duplicates = df.duplicated()
    
    # Return the number of duplicates and the duplicate rows
    return {
        'num_duplicates': duplicates.sum(),
        'duplicate_rows': df[duplicates]
    }

result = check_duplicates('xml_urls_testing.txt')
print(f'Number of duplicates: {result["num_duplicates"]}')
print('Duplicate rows:')
print(result['duplicate_rows'])