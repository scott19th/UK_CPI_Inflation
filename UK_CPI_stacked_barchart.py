

# Python script to create a stacked bar chart to display the contributing sectors to the overall UK CPI

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Step 1 import UK CPI CSV, since this was sourced from U

Sector_CPI = pd.read_csv('UK_CPI_sector_data.csv')


fig = px.bar(Sector_CPI, x="month",
             y=["Food and non-alcoholic beverages",
                "Alcohol and tobacco",
                "Clothing and footwear",
                "Housing and household services",
                "Furniture and household goods",
                "Transport", "Recreation and culture",
                "Restaurants and hotels",
                 "Other goods and services"],
             title="UK CPI Sector Contributions")

fig.add_trace(go.Scatter(x=Sector_CPI['month'],
                         y=Sector_CPI['CPIH 12-month inflation rate'],
                         mode='lines',
                         name='CPI Inflation Rate (12 month)',
                         line=dict(color='red')))


fig.write_image("UK_CPI_Sector.png")
fig.show()
