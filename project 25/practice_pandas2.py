import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("project 24/air_quality_no2.csv", index_col=0, parse_dates=True)
# print(air_quality)


## plot the data based on datetime object
# air_quality.plot()
# plt.show()

## only plot station_paris column data
# air_quality["station_paris"].plot()
# plt.show()

# # visually compare paris and london
# air_quality.plot.scatter(x="station_paris", y="station_london", alpha=0.5)
# plt.show()

# # compare station_antwerp and station_paris
# air_quality.plot.scatter(x="station_antwerp", y="station_paris", alpha=0.5)
# plt.show()



# method_names = [method_name for method_name in dir(air_quality.plot) if not method_name.startswith("_")]
# print(method_names)

air_quality.plot.area(subplots=True)
plt.show()