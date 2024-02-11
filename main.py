'''Default credentials are stored in $HOME/.config/gspread/service_account.json
Setup a service account and share spreadsheet with service account email.'''

import gspread

sa = gspread.service_account(filename='credentials.json')

sheet = sa.open('Portfolio Performance')
worksheet = sheet.worksheet('Sheet1')

# Get the num of rows and columns
print('Rows: ', worksheet.row_count)
print('Columns: ', worksheet.column_count)

# Get the value of cell
print(worksheet.acell('A1').value)

# Get range values
print(worksheet.get('A1:B5'))
print(worksheet.get_all_values())

# Update cell
worksheet.update([['Updated']], 'A2')
print(worksheet.acell('A2').value)
