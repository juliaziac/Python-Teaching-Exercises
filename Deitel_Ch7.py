import pandas as pd
grades = pd.Series([90, 97, 100])
#print(grades.describe())

grades_dict = pd.DataFrame({'Alice': [90, 99, 100], 'Bob': [88, 89, 92], 'Cat': [100, 99, 100]})
grades_dict.index = ['Test 1', 'Test 2', 'Test 3']

print(grades_dict[grades_dict > 95])

