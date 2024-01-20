# -------------------------------------------------- #
# ---------------------- Pandas ------------------------------- #

# import pandas as pd

# titanic = pd.read_csv("draw/titanic_data.csv")

# # print(titanic.head(8))
# # print(titanic.tail(8))
# # print(titanic.dtypes)

# titanic.to_excel("titanic_data.xlsx", sheet_name="passengers", index=False)

# titanic = pd.read_excel("titanic_data.xlsx", sheet_name="passengers")

# # print(titanic.head())
# # titanic.info()

# --------------------------- Pandas Things --------------------------- #
# 

# import pandas

# data = pandas.read_csv("draw/weather_data.csv")
# # print(data)
# data_dict = data.to_dict(orient='records')
# # print(data_dict)

# for _ in range(110):
#     print("-", end="")

# --------------------------- Pandas Work --------------------------- #

import pandas as pd

# df = pd.read_csv("my_bin/basic_file.csv")


# # # How many elements does the dataframe have ?
# # print(df.info())

# # How much old 'Alice' are ?
# print(df[df.Name == "Alice"].Age)

#-----------
df = pd.read_csv("my_bin/nyc_weather.csv")

# print(df)

# find_ans = df.EST[df.Events == "Rain"] # Which date rain


# average WindSpeedMPH
df.fillna(0, inplace=True)
find_ans = df.WindSpeedMPH.mean()

print(find_ans)