data_dict = {"Cost_Type" : ['Inbound Transportation','Inbound Handling','Inventory Storage','Outbound Handling','Outbound Transportation','Cross Transfers',
                       'Administrative cost'],
        "2022" : [5.65,1.29,2.67,2.04,8.0,0.52,4.26],
        "2023" : [5.13,1.27,2.66,1.93,8.35,0.43,3.89]}

data = pd.DataFrame(data_dict)
data['2022_e'] = data['2022']*10**6
data['2023_e'] = data['2023']*10**6
data['diff_bw_years'] = data['2023_e'] - data['2022_e']
data['diff_bw_years'] = data['diff_bw_years'].astype(int)
data['diff_bw_years_in_k'] = data['diff_bw_years'] / 10**3
data['diff_bw_years_in_k'] = data['diff_bw_years_in_k'].astype(int)
data['perc_diff_bw_years'] = round(data['diff_bw_years'] / data['2022_e']*100,2)
data_sorted = data.sort_values(by='diff_bw_years_in_k',ascending=False)
cost_2022 = round(data_sorted['2022_e'].sum()/10**6,2)
cost_2023 = round(data_sorted['2023_e'].sum()/10**6,2)
cost_2022_in_k = int(data_sorted['2022_e'].sum()/10**3)
cost_2023_in_k = int(data_sorted['2023_e'].sum()/10**3)
cost_types = ["2022"] + data_sorted['Cost_Type'].to_list() + ["2023"]
costs = [cost_2022_in_k] + data_sorted['diff_bw_years_in_k'].to_list() + [cost_2023_in_k]  # In 1000s
text = [str(cst)+"K" for cst in costs]
colors = [
    'rgb(93, 109, 126)', 'rgb(46, 204, 113)', 'rgb(46, 204, 113)',
    'rgb(46, 204, 113)', 'rgb(46, 204, 113)', 'rgb(46, 204, 113)',
    'rgb(231, 76, 60)', 'rgb(231, 76, 60)', 'rgb(93, 109, 126)'
]

fig = go.Figure(go.Waterfall(
    name="20",
    orientation="v",
    measure=["absolute", "relative", "relative", "relative", "relative", "relative", "relative", "relative", "absolute"],
    x=cost_types,
    y=costs,
    text=text,
    textposition="outside",
    decreasing={"marker":{"color":"rgb(231, 76, 60)"}},
    increasing={"marker":{"color":"rgb(46, 204, 113)"}},
    totals={"marker":{"color":"rgb(93, 109, 126)"}}
))


fig.update_layout(
    title={
        'text': "Cost Waterfall between 2022 and 2023",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 20,
            'color': 'rgb(202,120,46)'
        }
    },
    yaxis_title="Cost",
    xaxis_title="Year",
    yaxis_range=[23500, 25000],
    showlegend=True,
    legend=dict(
        title="Legend",
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    font=dict(
        size=12,
    ),
    margin=dict(t=100, b=40),
    waterfallgap=0.2,
)

#fig.show()
