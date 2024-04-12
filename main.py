# Get the first row of each group in a Pandas DataFrame

import pandas as pd

df = pd.DataFrame({
    'Animal': ['Cat', 'Cat', 'Cat', 'Dog', 'Dog', 'Dog'],
    'Max Speed': [25, 35, 40, 45, 55, 65]
})

#         Max Speed
# Animal
# Cat            25
# Dog            45
print(df.groupby('Animal').first())