import pandas as pd

def remove_duplicates(file_path):
    # Read the txt file into a Pandas DataFrame
    df = pd.read_csv(file_path, names=['urls'])
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Write the distinct values to a new txt file
    df.to_csv('distinct_xml_urls_2.txt', index=False, header=False)

remove_duplicates('/workspace/danish-business-insights/data_xmls/xml_urls_2.txt')