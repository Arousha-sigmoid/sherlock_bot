years = ["2022","2023"]
trips = [14890,15869]
text = ["14,890","15,869"]

increase_percentage = round((trips[1] - trips[0]) / (trips[0]) * 100,2)

colors = ['rgb(227, 139, 49)', 'rgb(193, 57, 43)']
fig = go.Figure()
fig.add_trace(go.Bar(
    x=years,
    y=trips,
    text=text,
    textposition='outside',
    marker_color=colors,
    width=0.3
))

fig.update_layout(
    title={
        'text': "Number of Trips per Year",
        'y': 0.85,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 20,
            'color': 'rgb(202,120,46)'
        }
    },
    annotations=[
        {
            'text': f"Increase in trips: +{increase_percentage}%",
            'xref': 'paper',
            'yref': 'paper',
            'x': 0.5,
            'y': 1.09,
            'showarrow': False,
            'font': {
                'size': 14,
                'color': 'rgb(202,120,46)'
            }
        }
    ],
    xaxis_title="Year",
    yaxis_title="Trips",
    yaxis_tickformat=",.0f",
    # yaxis_ticksuffix="K",
    margin=dict(t=100, b=40),
    yaxis_range=[12000, 17000],
    showlegend=False,
    width=500, height=400
)
#fig.show()