""" import plotly.express as px

country = input("Enter country name : ")
data = {
    'Country' : [country],
    'Values' : [100]}
fig = px.choropleth(
    data,
    locations=  'Country',
    locationmode= 'Country name',
    color= 'Values',
    color_continuous_scale = 'Interno',
    title = f'Country Map Highlighting{country}' 
)
fig.show() """

import plotly.express as px

country = input("Enter country name: ")
data = {
    'Country': [country],
    'Values': [100]
}

fig = px.choropleth(
    data,
    locations='Country',
    locationmode='country names',
    color='Values',
    color_continuous_scale='Viridis',  # Changed to a valid color scale
    title=f'Country Map Highlighting {country}'  # Added a space after "Highlighting"
)

fig.show()
