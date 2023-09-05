'''
This Program is used to match the images collected with Ground_Truth csv file 
and then creating the new ground_truth csv file matching the actual image file counts for each town
'''

import os
import pandas as pd;

dir = os.listdir(r'D:\CARLA_0.9.14\WindowsNoEditor\PythonAPI\examples\testing\Town06')
print(len(dir))
res = [ele.lstrip('0') for ele in dir]
print(len(res))
file = open('items.txt','w')
countIn=0
for  item in res:
    if(item != 'ground_truth.txt'):
        file.write(item+"\n")
file.close()


# Read in the text file using the appropriate delimiter
df1 = pd.read_csv(r'D:\CARLA_0.9.14\WindowsNoEditor\PythonAPI\examples\testing\Town06\ground_truth.txt')
df2 = pd.read_csv('items.txt')
# Write the DataFrame to a new CSV file
columns_df1= ['A','B']
columns_df2=['A']

df1.to_csv('ground_truth.csv', index=False,)
df2.to_csv('image_folder.csv',index=False)

#Creating the Ground_Truth data csv file

df1 = pd.read_csv('ground_truth.csv')
print(df1.shape)

df2 = pd.read_csv('image_folder.csv')
print(df2.shape)
df1 = df1[df1['A'].isin(df2['A'])]
print(df1.shape)
merged_df = pd.merge(df1, df2, on='A', how='outer', indicator=True)
final_df = merged_df[merged_df['_merge'] == 'both']
final_df.drop(['_merge'], axis=1, inplace=True)
print(final_df.shape)
final_df.to_csv('final_result.csv',index=False)
