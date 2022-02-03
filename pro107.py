import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("projectdata107.csv")
mean = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()
print(mean)
fig = px.scatter(mean, x = "student_id", y = "level", size = "attempt", color = "attempt")
fig.show()

