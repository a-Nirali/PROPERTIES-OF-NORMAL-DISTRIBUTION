import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("StudentsPerformance.csv")
performance = df["reading score"].tolist()

#mean
mean = sum(performance) / len(performance)
print(mean)
#median
performance_median=statistics.median(performance)
print(performance_median)
#mode
performance_mode=statistics.mode(performance)
print(performance_mode)
#sd
sd=statistics.stdev(performance)
print(sd)

first_sd_start, first_sd_end = mean-sd, mean+sd
second_sd_start, second_sd_end = mean-(2*sd), mean+(2*sd)
third_sd_start, third_sd_end = mean-(3*sd), mean+(3*sd)

#ploting a graph
fig = ff.create_distplot([performance], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_sd_start, first_sd_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_sd_end, first_sd_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_sd_start, second_sd_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_sd_end, second_sd_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[third_sd_start, third_sd_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[third_sd_end, third_sd_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.show()

list_of_data_within_1_sd = [result for result in data if result > first_sd_start and result < first_sd_end]
list_of_data_within_2_sd = [result for result in data if result > second_sd_start and result < second_sd_end]
list_of_data_within_3_sd = [result for result in data if result > third_sd_start and result < third_sd_end]

print("Standard deviation of this data is {}".format(performance_sd))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_sd)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_sd)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_sd)*100.0/len(data)))
