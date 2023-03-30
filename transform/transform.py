# Transform
import pandas as pd
import sys

sys.path.insert(0, 'D:\lina_lau\C339_datafundamentals\data_analysis_project')

class Transform:
    def __init__(self, df):
        self.df = df

    def rename_columns(self):
        self.df = self.df.rename(columns={"DisaggregatingDimension1ValueCode": "Sex",
                                          "NumericValue": "Prevalence",
                                          "SpatialDimensionValueCode": "WorldBankIncomeGroup"})

        #for col in self.df.columns:
        #    print(col)

        return
    
    def rename_column_values(self):       
        self.df = self.df.replace({'WorldBankIncomeGroup': {'WB_HI': 'HighIncome',
                                                            'WB_LI': 'LowerIncome',
                                                           'WB_LMI': 'LowerMiddleIncome',
                                                           'WB_UMI': 'UpperMiddleIncome'}})      
        self.df = self.df.replace({'Sex': {'BTSX': 'BothSexes',
                                          'MLE': 'Male',
                                          'FMLE': 'Female'}})
        return 

    def get_df(self):
        return self.df


