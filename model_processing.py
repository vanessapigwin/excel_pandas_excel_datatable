import pandas as pd

def process_files(file1, file2, file3):
    df1 = pd.read_excel(file1)

    # DO STUFF HERE 
    
    return df1[['url','name','developer']].head().to_html(
        index=False, 
        table_id='output_table',
        classes=['dataTable', 'table', 'table-striped'],
        border = 0
        )