import sys
from extract.extract import Extract
from load.load import Load
from transform.transform import Transform
sys.path.insert(0, 'D:\lina_lau\C339_datafundamentals\data_analysis_project')



e = Extract()
mydata_mean = e.getCSV("testDirectory/NCD_BMI_MEAN.csv")
mydata_under = e.getCSV("testDirectory/NCD_BMI_18A.csv")
mydata_over = e.getCSV("testDirectory/NCD_BMI_30A.csv")

mydata_list = [mydata_mean, mydata_under, mydata_over]
my_transformed_data_list = []

for dataset in mydata_list:
    t = Transform(dataset)
    t.rename_columns()
    t.rename_column_values()
    my_transformed_data_list.append(t.get_df())

#print(my_transformed_data_list)

for dataset, name in zip(my_transformed_data_list, ['mean', 'under', 'over']):
    print(f"Uploading {name}...")
    l = Load(f'dataset_{name}.csv', dataset)
    l.azure_push()

