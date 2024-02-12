import gspread
import pandas as pd

sa = gspread.service_account(filename='credentials.json')

sheet = sa.open('Portfolio Performance')
worksheet = sheet.worksheet('2024')

# Get range values
print(worksheet.get_all_values())

# Create a sample pandas df
data = {'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']}
df = pd.DataFrame(data)

# Write the whole df to the worksheet starting A1 replacing existing values
title_raw = [df.columns.values.tolist()]
other_raws = df.values.tolist()
print(title_raw)
print(other_raws)
print(title_raw + other_raws)
worksheet.update([df.columns.values.tolist()] + df.values.tolist())
