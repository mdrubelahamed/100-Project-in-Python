import pandas as pd
import matplotlib.pyplot as plt


titanic = pd.read_csv("project 24/titanic_data.csv")
# print(titanic.head())

# ages = titanic["Age"]
# print(ages.head())

# print(type(titanic))
# print(type(titanic["Age"]))

# print(titanic[["Age", "Sex"]].shape)
# print(titanic.shape)
# print(titanic[["Age", "Sex"]])


# above_35 = titanic[titanic["Age"] > 35]
# print(above_35)

# below_18 = titanic[titanic["Age"] < 18]
# print(below_18)

# # average age
# print(titanic["Age"].mean())

# # highest fare ticket price
# print(titanic["Fare"].max())

# #unique values are in Embarked colums
# unique_column = titanic["Embarked"].unique()
# print(unique_column) 
# print(len(unique_column))


# # What is the most common ticket class (Pclass) among passengers?
# most_common_Pclass = titanic["Pclass"].mode().iloc[0]
# print(most_common_Pclass)

# # print(titanic["Pclass"].value_counts())

# # standard deviation
# std_ages = titanic["Age"].std()
# print(std_ages)

# # create box plot
# plt.figure(figsize=(8, 6))
# plt.boxplot(titanic["Age"], vert=False)
# plt.title("Passengers Ages")
# plt.xlabel("Age")
# plt.show()


# # ticket fare range
# fare_range = titanic["Fare"].max() - titanic["Fare"].min()
# print(fare_range)

# print(titanic["Fare"].describe())
print(titanic["Fare"].quantile(0.75))