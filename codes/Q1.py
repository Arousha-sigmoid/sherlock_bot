## dataset
df_cost_split = pd.read_csv('data/cost_split.csv')
df_cost_split = df_cost_split.sort_values(by='Cost (Euros)')
cost_types = df_cost_split['Cost Type']
total_cost = df_cost_split['Cost (Euros)'].sum()
tot_cost_in_m = round(total_cost/10**6,2)
costs = df_cost_split['Cost (Euros)'] / 10**6
percentages = df_cost_split['Cost (Euros)'] / total_cost * 100

fig = go.Figure()

fig.add_trace(go.Bar(
    x=cost_types,
    y=costs,
    text=[f'{p:.2f}%<br>{c:.2f}M' for p, c in zip(percentages, costs)],
    textposition='outside',
    marker_color='rgb(202,120,46)',
    width=0.5
))

fig.update_layout(
    title={
        'text': "Percentage Share by Cost Type",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 20,
            'color': 'rgb(202,120,46)'
        }
    },
    annotations=[
        {
            'text': f"Total Cost: € {tot_cost_in_m} M",
            'xref': 'paper',
            'yref': 'paper',
            'x': 0.5,
            'y': 1.1,
            'showarrow': False,
            'font': {
                'size': 16,
                'color': 'rgb(202,120,46)'
            }
        }
    ],
    xaxis_title="Cost Type",
    yaxis_title="Cost (Euros)",
    yaxis_tickformat=",.0f",
    yaxis_range=[0, 10],
    yaxis_ticksuffix="M",
    margin=dict(t=100, b=40)
)
#fig.show()
