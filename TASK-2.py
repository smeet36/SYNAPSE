#############################(PIE-CHART)
import json  
import pandas as pd  
from pandas.io.json import json_normalize  

with open('bifircate.json') as text: 
    d = json.load(text)

pd_v = json_normalize(d['data_v'])
pd_f = json_normalize(d['data_f']) 

import plotly.graph_objects as gr

labels = ['Fund Raisers','Viewers']
values = [8268,11811]

fig = gr.Figure(data=[gr.Pie(labels=labels, values=values, pull=[0.1, 0], title="RATIO OF FUND_RAISERS AND VIEWERS")])

fig.show()

#############################(BAR-GRAPH)
with open('bifircate.json') as f: 
    d = json.load(f) 
pd_v = json_normalize(d['data_v'])
pd_f= json_normalize(d['data_f']) 
pd_v[pd_v['category']=='Sports']

with open('example.json') as f: 
    d = json.load(f) 
pd = json_normalize(d['data']) 

import plotly.express as px

fig = px.bar(pd, x="category", y=["view", "fund"], title="VIEWS AND FUNDS PER CATEGORIES", height=560, width=410)

fig.show()

#############################(GEO-MAP)
import json
import numpy as np
import pandas as pd_f
from pandas.io.json import json_normalize

import chart_studio as cs
import plotly.graph_objects as gr

cs.tools.set_credentials_file(username='smeet_t', api_key='Ronaldo@7')

with open('bifircate.json') as text:
    data=json.load(text)

pd_v= json_normalize(data['data_v'])
pd_f= json_normalize(data['data_f'])

pd_f['text']= pd_f['location.state'] + ' ' + pd_f['location.city']
fig = gr.Figure(data=gr.Scattergeo(
        locationmode = 'USA-states',
        lon = pd_f['location.longitude'],
        lat = pd_f['location.latitude'],
        text = pd_f['text'],
        mode = 'markers',
        marker = dict(
            size = 8,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = 'Blues',
            cmin = pd_f['amount'].max(),
            color = pd_f['amount'],
            cmax = 0,
            colorbar_title="FUND_RAISED(Rs.)"
        )))
        
fig.update_layout(
        title = 'FUND_RAISER OVER THE STATES',
        geo = dict(
            scope='usa',
            projection_type='albers usa',
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 1,
            subunitwidth = 1,
        ),
    )
fig.show()

##################################(GROUPED-BAR-CHART)
import json  
import pandas as pd  
from pandas.io.json import json_normalize  

with open('bifircate.json') as text: 
    d = json.load(text)

vital= {}

vital["data_age"]= []

for x in d['data_f']:
    if x['age']=='55+' and x['marital_status']=='married':
        vital["data_age"].append(x)
    else:
        pass

len(vital['data_age'])

import plotly.graph_objects as go
age_group=['18-24', '25-34', '35-44', '45-54', '55+']

fig = go.Figure(data=[
    go.Bar(name='MALE', x=age_group, y=[1879,450,455,489,478]),
    go.Bar(name='FEMALE', x=age_group, y=[1975,491,501,466,460]),
    go.Bar(name='SINGLE', x=age_group, y=[1454,357,388,390,286]),
    go.Bar(name='MARRIED', x=age_group, y=[2732,648,644,641,728])
])

fig.update_layout(barmode='group')
fig.show()