import pandas as pd

titanic = pd.read_csv("project 24/titanic_data.csv")

# print(titanic.head(8))
# print(titanic.tail(8))
# print(titanic.dtypes)

titanic.to_excel("titanic_data.xlsx", sheet_name="passengers", index=False)

titanic = pd.read_excel("titanic_data.xlsx", sheet_name="passengers")

# print(titanic.head())
# titanic.info()