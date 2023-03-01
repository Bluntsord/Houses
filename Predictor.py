import pandas as pd

# Load the data into a Pandas DataFrame
hdb_df = pd.read_csv('hdb.csv')

# Filter the data for units with area <= 50 SQM
two_room_hdb_df = hdb_df[hdb_df['Area (SQM)'] <= 50]

# Filter the data for units with area between 60 SQM and 80 SQM (inclusive)
three_room_hdb_df = hdb_df[(hdb_df['Area (SQM)'] >= 60) & (hdb_df['Area (SQM)'] <= 80)]

# Get the summary statisis for the two-room HDB units prices
two_room_hdb_price_summary = two_room_hdb_df['Transacted Price ($)'].mean()
three_room_hdb_price_summary = three_room_hdb_df['Transacted Price ($)'].mean()

print(two_room_hdb_price_summary)
print('====================================================================')
print(three_room_hdb_price_summary)


