import plotly.express as px
import dash
import pandas 
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


df = pandas.read_csv("df_tratado.csv")
col_options = [dict(label=x, value=x) for x in df.columns]
dimensions = ["x", "y", "color", "facet_col", "facet_row","size"]
graph_options = [dict(label=x, value=x) for x in ["scatterplot","boxplot","histogram"]]
hist_functions = [dict(label=x, value=x) for x in ["count","sum","avg","min","max"]]


app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

app.layout = html.Div(
    [
        html.H1("Análise microdados ENADE 2017"),
        html.Div(
            [

                html.P(["Graph options:", dcc.Dropdown(id="graph_options", options=graph_options)])

            ],
            style={"width": "25%", "float": "topleft"},
        ),
        html.Div(
            [
               
                html.P(["Aggregation function(histogram only):", dcc.Dropdown(id="hist_functions", options=hist_functions)])
                
            ],
            style={"width": "25%", "float": "topleft"},
        ),
        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ],
            style={"width": "25%", "float": "left"},
        ),
        dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"}),
    ]
)

@app.callback(
    dash.dependencies.Output('hist_functions', 'options'),
    [dash.dependencies.Input('graph_options', 'value')]
)           
def update_aggregation_function_dropdown(graph):
    if graph == "histogram":
        return [dict(label=x, value=x) for x in ["count","sum","avg","min","max"]]
    else:
        return [dict(label=x, value=x) for x in [""]]

@app.callback(
    dash.dependencies.Output('size', 'options'),
    [dash.dependencies.Input('graph_options', 'value')]
)           
def update_size_dropdown(graph):
    if graph == "scatterplot":
        return [dict(label=x, value=x) for x in df.columns]
    else:
        return [dict(label=x, value=x) for x in [""]]


@app.callback(Output("graph", "figure"), [Input(d, "value") for d in (dimensions+["graph_options"]+["hist_functions"])])
def make_figure(x, y, color, facet_col, facet_row,size,graph, hist_function):

    if graph == "scatterplot":
        try:
            return px.scatter(
                df,
                x=x,
                y=y,
                color=color,
                facet_col=facet_col,
                facet_row=facet_row,
                size=size,
                height=700,
            )
        except:
            return null
    elif graph == "boxplot":
        try:
            return px.box(
                df,
                x=x,
                y=y,
                color=color,
                facet_col=facet_col,
                facet_row=facet_row,
                height=700,
            )
        except:
            return null
    else :
         try:
            return px.histogram(
                df,
                x=x,
                y=y,
                color=color,
                facet_col=facet_col,
                facet_row=facet_row,
                histfunc=hist_function,
                height=700,
                
            )
         except:
            return null


app.run_server(host='0.0.0.0',debug=True
    , use_reloader=False
    ,dev_tools_ui=False
    )