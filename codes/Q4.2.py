years = ['Before Route Optimization','After Route Optimization']
pallets_per_trip = [16.72, 18.34]
colors = ['rgb(227, 139, 49)', 'rgb(193, 57, 43)']

fig = go.Figure()

fig.add_trace(go.Bar(
    x=years,
    y=pallets_per_trip,
    text=pallets_per_trip,
    textposition='outside',
    marker_color=colors,
    width=0.3
))

fig.update_layout(
    title={
        'text': "Route Optimization",
        'y': 0.8,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 15,
            'color': 'rgb(202,120,46)'
        }
    },
    annotations=[
        {
            'text': "",
            'xref': 'paper',
            'yref': 'paper',
            'x': 0.5,
            'y': 1.05,
            'showarrow': False,
            'font': {
                'size': 16,
                'color': 'rgb(202,120,46)'
            }
        }
    ],
    #xaxis_title="Year",
    yaxis_title="Number of Pallets",
    yaxis_tickformat=",.0f",
    # yaxis_ticksuffix="K",
    margin=dict(t=100, b=40),
    yaxis_range=[0, 20],
    showlegend=False,
    width=500, height=400
)
#fig.show()