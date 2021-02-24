{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#https://github.com/plotly/dash-px/blob/master/app.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dash is running on http://0.0.0.0:8050/\n",
      "\n",
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: on\n"
     ]
    }
   ],
   "source": [
    "import plotly.express as px\n",
    "import dash\n",
    "import pandas \n",
    "import dash_html_components as html\n",
    "import dash_core_components as dcc\n",
    "from dash.dependencies import Input, Output\n",
    "\n",
    "\n",
    "df = pandas.read_csv(\"df_tratado.csv\")\n",
    "col_options = [dict(label=x, value=x) for x in df.columns]\n",
    "dimensions = [\"x\", \"y\", \"color\", \"facet_col\", \"facet_row\"]\n",
    "graph_options = [dict(label=x, value=x) for x in [\"scatterplot\",\"boxplot\",\"histogram\"]]\n",
    "hist_functions = [dict(label=x, value=x) for x in [\"count\",\"sum\",\"avg\",\"min\",\"max\"]]\n",
    "\n",
    "\n",
    "app = dash.Dash(\n",
    "    __name__, external_stylesheets=[\"https://codepen.io/chriddyp/pen/bWLwgP.css\"]\n",
    ")\n",
    "\n",
    "app.layout = html.Div(\n",
    "    [\n",
    "        html.H1(\"Análise microdados ENADE 2017\"),\n",
    "        html.Div(\n",
    "            [\n",
    "                html.P([\"Graph options:\", dcc.Dropdown(id=\"graph_options\", options=graph_options)])\n",
    "            ],\n",
    "            style={\"width\": \"25%\", \"float\": \"topleft\"},\n",
    "        ),\n",
    "        html.Div(\n",
    "            [\n",
    "               \n",
    "                html.P([\"Aggregation function(histogram only):\", dcc.Dropdown(id=\"hist_functions\", options=hist_functions)])\n",
    "                \n",
    "            ],\n",
    "            style={\"width\": \"25%\", \"float\": \"topleft\"},\n",
    "        ),\n",
    "        html.Div(\n",
    "            [\n",
    "                html.P([d + \":\", dcc.Dropdown(id=d, options=col_options)])\n",
    "                for d in dimensions\n",
    "            ],\n",
    "            style={\"width\": \"25%\", \"float\": \"left\"},\n",
    "        ),\n",
    "        dcc.Graph(id=\"graph\", style={\"width\": \"75%\", \"display\": \"inline-block\"}),\n",
    "    ]\n",
    ")\n",
    "\n",
    "@app.callback(Output(\"graph\", \"figure\"), [Input(d, \"value\") for d in (dimensions+[\"graph_options\"]+[\"hist_functions\"])])\n",
    "def make_figure(x, y, color, facet_col, facet_row,graph, hist_function):\n",
    "    if graph == \"scatterplot\":\n",
    "        hist_functions = \"\"\n",
    "        return px.scatter(\n",
    "            df,\n",
    "            x=x,\n",
    "            y=y,\n",
    "            color=color,\n",
    "            facet_col=facet_col,\n",
    "            facet_row=facet_row,\n",
    "            height=700,\n",
    "        )\n",
    "    elif graph == \"boxplot\":\n",
    "        hist_functions = \"\"\n",
    "        return px.box(\n",
    "            df,\n",
    "            x=x,\n",
    "            y=y,\n",
    "            color=color,\n",
    "            facet_col=facet_col,\n",
    "            facet_row=facet_row,\n",
    "            height=700,\n",
    "        )\n",
    "    else :\n",
    "        hist_functions = [dict(label=x, value=x) for x in [\"count\",\"sum\",\"avg\",\"min\",\"max\"]]\n",
    "        return px.histogram(\n",
    "            df,\n",
    "            x=x,\n",
    "            y=y,\n",
    "            color=color,\n",
    "            facet_col=facet_col,\n",
    "            facet_row=facet_row,\n",
    "            histfunc=hist_function,\n",
    "            height=700,\n",
    "            \n",
    "        )\n",
    "\n",
    "\n",
    "app.run_server(host='0.0.0.0',debug=True, use_reloader=False,dev_tools_ui=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
