import pandas as pd
import numpy as np
import plotly.express as px
import sys

import dash
import dash_core_components as dcc
import dash_html_components as html

# Importing transformed datasets from Azure:
sys.path.insert(0, 'D:\lina_lau\C339_datafundamentals\data_analysis_project')
from extract.extract import Extract

e = Extract()
dataset_mean = e.getCSV("testDirectory/dataset_mean.csv")
dataset_under = e.getCSV("testDirectory/dataset_under.csv")
dataset_over = e.getCSV("testDirectory/dataset_over.csv")

for col in dataset_mean.columns:
    print(col)

income_group = ['HighIncome', 'LowerIncome', 'LowerMiddleIncome', 'UpperMiddleIncome']
mean_fig = px.line(dataset_mean["WorldBankIncomeGroup"].isin(income_group), 
                   x = 'TimeDim',
                   y = 'Prevalence', 
                   color = 'WorldBankIncomeGroup')
mean_fig.show()