'''
A script to visualize the Top 10 plastic pollutants from the TOP integrated dataset.
Utilizes the pandas library to analyze the data.
'''
import pandas as pd 

top_10 = pd.read_csv("data/Top_10_Most_Common_Plastics_by_Country.csv")
print(top_10.info())
print(top_10.loc[top_10["Top1_Value"] > 10000, ["NAME", "Top1_Name"]])
print(top_10.loc[top_10["Top2_Value"] > 10000, ["NAME", "Top2_Name"]])
print(top_10.loc[top_10["Top3_Value"] > 10000, ["NAME", "Top3_Name"]])
print(top_10.loc[top_10["Top4_Value"] > 10000, ["NAME", "Top4_Name"]])
print(top_10.loc[top_10["Top5_Value"] > 10000, ["NAME", "Top5_Name"]])
print(top_10.loc[top_10["Top6_Value"] > 10000, ["NAME", "Top6_Name"]])
print(top_10.loc[top_10["Top7_Value"] > 10000, ["NAME", "Top7_Name"]])
print(top_10.loc[top_10["Top8_Value"] > 10000, ["NAME", "Top8_Name"]])
print(top_10.loc[top_10["Top9_Value"] > 10000, ["NAME", "Top9_Name"]])
print(top_10.loc[top_10["Top10_Value"] > 10000, ["NAME", "Top10_Name"]])
