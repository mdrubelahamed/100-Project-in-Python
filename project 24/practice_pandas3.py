# import pandas as pd

# air_quality = pd.read_csv("project 24/air_quality_no2.csv", index_col=0, parse_dates=True)

# # print(air_quality.head())

# # air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882

# # air_quality["ratio_paris_antwerp"]  = air_quality["station_paris"] / air_quality["station_antwerp"]

# air_quality_renamed = air_quality.rename(
#     columns= {
#         "station_antwerp": "A",
#         "station_paris": "P",
#         "station_london": "L",
        
#     }
# )


# print(air_quality.head())


# #change column name printed
# print(air_quality_renamed.head())

# #change column name into lowercase
# air_quality_renamed = air_quality_renamed.rename(columns= str.lower)
# print(air_quality_renamed.head())



#################################
# How to Calculate Summary Statistics
import pandas as pd

titanic = pd.read_csv("project 24/titanic_data.csv")

# print(titanic["Age"].mean())

# print(titanic[["Age", "Fare"]].median())

# print(titanic[["Age", "Fare"]].describe())

# agg_titanic = titanic.agg(
#     {
#         "Age": ["min", "max", "median", ],
#         "Fare": ["min", "max", "median", "mean"],
#     }
# )

# print(agg_titanic)

compare_sex_age = titanic[["Sex", "Age"]].groupby("Sex").mean()

print(compare_sex_age)