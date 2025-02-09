import plotly.graph_objects as go

# Sample data (latitude, longitude)
latitudes = [40.7128, 34.0522, 41.8781]
longitudes = [-74.0060, -118.2437, -87.6298]
locations = ['New York', 'Los Angeles', 'Chicago']

# Create Scattergeo plot
fig = go.Figure(go.Scattergeo(
    locationmode='USA-states',
    lat=latitudes,
    lon=longitudes,
    text=locations,
    mode='markers+text',  # You can also use 'markers' for just the points
    marker=dict(size=8, color='blue'),
))

fig.update_layout(
    geo=dict(
        scope='usa',  # You can change this to 'world' for a global map
        projection_type='albers usa',
        showland=True,
    ),
    title='City Locations on Map',
)

fig.show()