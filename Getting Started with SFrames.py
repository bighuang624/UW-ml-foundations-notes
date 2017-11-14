# Getting Started with SFrames

import graphlab

sf = graphlab.SFrame('people-example.csv')
sf  # we can view first few lines of table
sf.tail()  # view end of the table

# .show() visualizes any data structure in GraphLab Create
sf.show()

# If you want Canvas visualization to show up on this notebook, 
# rather than popping up a new window, add this line:
graphlab.canvas.set_target('ipynb')
sf['age'].show(view='Categorical')

# Inspect columns of dataset
sf['Country']
# dtype: str
# Rows: 7
# ['United States', 'Canada', 'England', 'USA', 'Poland', 'United States', 'Switzerland']
sf['age']
# dtype: int
# Rows: 7
# [24, 23, 22, 23, 23, 22, 25]

# Some simple columnar operations
sf['age'].mean()
sf['age'].max()

# Create new columns in our SFrame
sf['Full Name'] = sf['First Name'] + ' ' + sf['Last Name']

sf['age'] * sf['age']
# dtype: int
# Rows: 7
# [576, 529, 484, 529, 529, 484, 625]

# 数据转换
def transform_country(country):
    if country == 'USA':
        return 'United States'
    else:
        return country

sf['Country'] = sf['Country'].apply(transform_country)



