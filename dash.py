import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

#run app 
app = dash.Dash(__name__)

#assign a header
div_header = html.Div(html.H1(children="Jeg er trøtt."), className='header')

#assign a new dcc - checklist
my_checklist = dcc.Checklist(
    options=[
        {'label': 'Morning', 'value': 2},
        {'label': 'Middle', 'value': 5,
        {'label': 'Afternoon', 'value': 9}
    ], value=2, id='my_checklist')

#assign a slider with values
my_energy = dcc.Slider(
    min=0,
    max=10,
    step=1,
    marks={
        0:'veldig trøtt',
        2:'passe trøtt'
        4:'litt trøtt',
        6:'passe opplagt',
        8:'uthvilt',
        10:'masse energi'
    },
    value=0, id='my_energy'
)



#assigning a figure of the sort "line" to my graph
#fig = px.line(x = [6,4,6,2,7,5,6,14,2,5,14,5,12],y = [9,2,5,2,5,7,3,24,3,7,20,5,10])
my_figure = dcc.Graph(id='myfigure')

@app.callback(
    dash.dependencies.Output('myfigure', 'figure'),
    [dash.dependencies.Input('my_energy', 'value'),
    dash.dependencies.Input('my_checklist', 'value')]
)
def callback_figure(last_value, first_y_value):
    x = [0, 6,4,2,5,10,5,10]
    y = [3,6,3,7,9,5]
    y.insert(0, first_y_value)
    y.append(last_value)
    line_plot = px.scatter(x=x, y=y)
    return(line_plot)

#calling on my components to my app
app.layout = html.Div(
    [div_header, my_figure, my_checklist, my_energy], className ='report')

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)


