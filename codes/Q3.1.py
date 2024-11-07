# Data
years = ["2022", "2023"]
volumes = [275490, 262320]
volumes_in_k = [vol/10**3 for vol in volumes]
text = [str(vol) + "K" for vol in volumes_in_k]

colors = ['rgb(227, 139, 49)', 'rgb(193, 57, 43)']
decrease_percentage = ((volumes[0] - volumes[1]) / volumes[0]) * 100
fig = go.Figure()
fig.add_trace(go.Bar(
    x=years,
    y=volumes_in_k,
    text=text,
    textposition='outside',
    marker_color=colors,
    width=0.3
))
fig.update_layout(
    title={
        'text': "Number of Pallets",
        'y': 0.88,
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
            'text': f"Decrease in Volume: {decrease_percentage:.1f}%",
            'xref': 'paper',
            'yref': 'paper',
            'x': 0.5,
            'y': 1.1,
            'showarrow': False,
            'font': {
                'size': 14,
                'color': 'rgb(202,120,46)'
            }
        }
    ],
    xaxis_title="Year",
    yaxis_title="Volume",
    yaxis_tickformat=",.0f",
    yaxis_ticksuffix="K",
    margin=dict(t=100, b=40),
    yaxis_range=[0, 300],
    showlegend=False,
    bargap=1,
    width=500, height=400
)
#fig.show()