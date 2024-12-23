from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash
import yfinance as yf

btc_data = yf.download('BTC-USD', start='2023-01-01')
eth_data = yf.download('ETH-USD', start='2023-01-01')
near_data = yf.download('NEAR-USD', start='2023-01-01')
inj_data = yf.download('INJ-USD', start='2023-01-01')
rndr_data = yf.download('RNDR-USD', start='2023-01-01')
op_data = yf.download('OP-USD', start='2023-01-01')

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('Comparação de Valorização Criptomoedas'), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.Label('Selecione uma opção: '),
            dcc.Dropdown(
                id='cripto1-dropdown',
                options=[
                    {'label': 'Bitcoin', 'value': 'BTC'},
                    {'label': 'Ethereum', 'value': 'ETH'},
                    {'label': 'NEAR', 'value': 'NEAR'},
                    {'label': 'Injective', 'value': 'INJ'},
                    {'label': 'Render', 'value': 'RNDR'},
                    {'label': 'Optimism', 'value': 'OP'}
                ],
                value='BTC'  # valor padrão
            )
        ]),
        dbc.Col([
            html.Label('Escolha uma Opção: '),
            dcc.Dropdown(
                id='cripto2-dropdown',
                options=[
                    {'label': 'Bitcoin', 'value': 'BTC'},
                    {'label': 'Ethereum', 'value': 'ETH'},
                    {'label': 'NEAR', 'value': 'NEAR'},
                    {'label': 'Injective', 'value': 'INJ'},
                    {'label': 'Render', 'value': 'RNDR'},
                    {'label': 'Optimism', 'value': 'OP'}
                ],
                value='ETH'  # Valor padrão
            )
        ])
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='cripto-comparison-graph'), width=12)
    ])
])

@app.callback(
    Output('cripto-comparison-graph', 'figure'),
    [Input('cripto1-dropdown', 'value')],
    [Input('cripto2-dropdown', 'value')]
)


def update_graph(cripto1, cripto2):
    if cripto1 == 'BTC':
        cripto1_data = btc_data
    elif cripto1 == 'ETH':
        cripto1_data = eth_data
    elif cripto1 == 'NEAR':
        cripto1_data = near_data
    elif cripto1 == 'INJ':
        cripto1_data = inj_data
    elif cripto1 == 'RNDR':
        cripto1_data = rndr_data
    elif cripto1 == 'OP':
        cripto1_data = op_data


    if cripto2 == 'BTC':
        cripto2_data = btc_data
    elif cripto2 == 'ETH':
        cripto2_data = eth_data
    elif cripto2 == 'NEAR':
        cripto2_data = near_data
    elif cripto2 == 'INJ':
        cripto2_data = inj_data
    elif cripto2 == 'RNDR':
        cripto2_data = rndr_data
    elif cripto2 == 'OP':
        cripto2_data = op_data

    fig = {
        'data': [
            {'x': cripto1_data.index, 'y': cripto1_data['Close'] / cripto1_data['Close'][0], 'type': 'line', 'name': cripto1},
            {'x': cripto2_data.index, 'y': cripto2_data['Close'] / cripto2_data['Close'][0], 'type': 'line', 'name': cripto2}
        ],
        'layout': {
            'title': 'Comparação da Valorização de Criptomoedas ao Longo dos Anos',
            'xaxis': {'title': 'Ano'},
            'yaxis': {'title': 'Preço de Fechamento (USD)'}
        }
    }
    return fig


if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
