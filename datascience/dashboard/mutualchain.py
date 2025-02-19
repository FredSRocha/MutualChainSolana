# -*- coding: utf-8 -*-
"""MutualChain.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n8aNBQI5svaLCmV7yLeXSFnz35Ad06z_
"""

!pip install pandas plotly dash

# Importações necessárias
import random
import time
from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
from sklearn.ensemble import IsolationForest
import threading

# ====================
# Configurações Globais
# ====================

# Número de transações iniciais a serem simuladas
NUM_TRANSACOES_INICIAIS = 500

# Número de dias para a simulação de datas de transações
NUM_DIAS = 30

# Limite padrão de conformidade (valor máximo permitido por transação)
LIMITE_CONFORMIDADE = 5.0

# DataFrame global para armazenar as transações
df_transacoes = pd.DataFrame()

# Lock para controlar o acesso ao DataFrame em threads
lock = threading.Lock()

# ====================
# Funções para Simulação de Dados
# ====================

def gerar_contas_lista_negra(num_contas=10):
    """
    Gera uma lista de contas que estão na lista negra (suspeitas ou bloqueadas).
    """
    return [f'Account{acc}' for acc in random.sample(range(1000, 9999), num_contas)]

def gerar_transacao(i, data_inicio, contas_lista_negra):
    """
    Gera uma transação simulada com dados aleatórios.
    """
    data_transacao = data_inicio + timedelta(
        days=random.randint(0, NUM_DIAS),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59)
    )
    transacao = {
        'Transaction_ID': f'TX{i:08}',
        'Date': data_transacao,
        'Sender_ID': f'Account{random.randint(1000, 9999)}',
        'Receiver_ID': f'Account{random.randint(0, 9999)}',
        'Amount_SOL': round(random.uniform(0.01, 20.0), 4),
        'Transaction_Type': random.choice(['Pagamento', 'Reembolso', 'Transferência', 'Depósito', 'Saque', 'Investimento']),
        'Fee_SOL': round(random.uniform(0.0001, 0.01), 5),
        'Status': random.choice(['Pendente', 'Concluída', 'Falhada']),
        'Compliance_Status': "Pending",
        'Location': random.choice(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília', 'Curitiba', 'Porto Alegre', 'Recife', 'Salvador']),
        'Anomaly_Score': 0
    }
    return transacao

def simular_transacoes_iniciais():
    """
    Simula as transações iniciais antes de iniciar o dashboard.
    """
    global df_transacoes, contas_lista_negra
    contas_lista_negra = gerar_contas_lista_negra()
    data_inicio = datetime.now() - timedelta(days=NUM_DIAS)
    transacoes = []
    for i in range(1, NUM_TRANSACOES_INICIAIS + 1):
        transacao = gerar_transacao(i, data_inicio, contas_lista_negra)
        transacoes.append(transacao)
    df_transacoes = pd.DataFrame(transacoes)
    df_transacoes = aplicar_verificacao_conformidade(df_transacoes, LIMITE_CONFORMIDADE, contas_lista_negra)
    df_transacoes['Blockchain_Status'] = 'Registered'
    df_transacoes = detectar_anomalias(df_transacoes)
    df_transacoes['Notification'] = df_transacoes.apply(enviar_notificacao, axis=1)

# ====================
# Funções de Verificação de Conformidade
# ====================

def verificar_conformidade(transacao, limite_conformidade, contas_lista_negra):
    """
    Verifica se uma transação está em conformidade com as regras estabelecidas.
    """
    if transacao['Amount_SOL'] > limite_conformidade:
        return "Não Conforme"
    if transacao['Sender_ID'] in contas_lista_negra or transacao['Receiver_ID'] in contas_lista_negra:
        return "Não Conforme"
    if transacao['Transaction_Type'] in ['Reembolso', 'Saque']:
        return "Não Conforme"
    return "Conforme"

def aplicar_verificacao_conformidade(df_transacoes, limite_conformidade, contas_lista_negra):
    """
    Aplica a verificação de conformidade a um DataFrame de transações.
    """
    df_transacoes['Compliance_Status'] = df_transacoes.apply(
        lambda transacao: verificar_conformidade(transacao, limite_conformidade, contas_lista_negra), axis=1)
    return df_transacoes

# ====================
# Função para Enviar Notificações
# ====================

def enviar_notificacao(transacao):
    """
    Gera uma notificação com base no status de conformidade e anomalias da transação.
    """
    if transacao['Compliance_Status'] == "Não Conforme" or transacao['Anomaly_Score'] == -1:
        return f"⚠️ Alerta: Transação {transacao['Transaction_ID']} não conforme ou suspeita!"
    return "Transação Conforme"

# ====================
# Função para Detecção de Anomalias
# ====================

def detectar_anomalias(df):
    """
    Utiliza Isolation Forest para detectar transações anômalas.
    """
    model = IsolationForest(contamination=0.05, random_state=42)
    features = df[['Amount_SOL', 'Fee_SOL']]
    model.fit(features)
    df['Anomaly_Score'] = model.predict(features)
    return df

# ====================
# Simulação de Transações em Tempo Real
# ====================

def simular_transacoes_tempo_real():
    """
    Simula transações acontecendo em tempo real e atualiza o DataFrame global.
    """
    global df_transacoes, contas_lista_negra
    data_inicio = datetime.now() - timedelta(days=NUM_DIAS)
    i = NUM_TRANSACOES_INICIAIS + 1
    while True:
        time.sleep(random.uniform(0.5, 1.5))
        with lock:
            transacao = gerar_transacao(i, data_inicio, contas_lista_negra)
            transacao_df = pd.DataFrame([transacao])
            transacao_df = aplicar_verificacao_conformidade(transacao_df, LIMITE_CONFORMIDADE, contas_lista_negra)
            transacao_df['Blockchain_Status'] = 'Registered'
            transacao_df = detectar_anomalias(transacao_df)
            transacao_df['Notification'] = transacao_df.apply(enviar_notificacao, axis=1)
            df_transacoes = pd.concat([df_transacoes, transacao_df], ignore_index=True)
            i += 1

# Inicia a simulação das transações iniciais
simular_transacoes_iniciais()

# Inicia a thread para simular transações em tempo real
threading.Thread(target=simular_transacoes_tempo_real, daemon=True).start()

# ====================
# Configuração do Dashboard com Plotly Dash
# ====================

# Inicializa o aplicativo Dash
app = dash.Dash(__name__)
server = app.server  # Necessário para implantação

# Layout do aplicativo Dash
app.layout = html.Div([
    html.H1("Dashboard de Gestão para Entidades Mutualistas com Blockchain e IA"),
    html.H2("Transações em Tempo Real na Blockchain Solana"),
    html.Div([
        # Div para filtros
        html.Div([
            html.H3("Filtros"),
            html.Label("Período:"),
            dcc.DatePickerRange(
                id='date-range-picker',
                min_date_allowed=df_transacoes['Date'].min().date(),
                max_date_allowed=df_transacoes['Date'].max().date(),
                start_date=df_transacoes['Date'].min().date(),
                end_date=df_transacoes['Date'].max().date()
            ),
            html.Br(),
            html.Label("Limite de Conformidade (SOL):"),
            dcc.Slider(
                id='amount-threshold-slider',
                min=0,
                max=20,
                step=0.1,
                value=LIMITE_CONFORMIDADE,
                marks={i: f'{i}' for i in range(0, 21, 2)}
            ),
            html.Br(),
            html.Label("Tipos de Transação:"),
            dcc.Dropdown(
                id='transaction-type-dropdown',
                options=[{'label': t, 'value': t} for t in df_transacoes['Transaction_Type'].unique()],
                value=df_transacoes['Transaction_Type'].unique().tolist(),
                multi=True
            ),
            html.Br(),
            html.Label("Localização:"),
            dcc.Dropdown(
                id='location-dropdown',
                options=[{'label': loc, 'value': loc} for loc in df_transacoes['Location'].unique()],
                value=df_transacoes['Location'].unique().tolist(),
                multi=True
            ),
        ], style={'width': '25%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '20px'}),
        # Div para gráficos e resumo
        html.Div([
            html.Div(id='summary-div', style={'padding': '20px'}),
            dcc.Graph(id='transactions-time-series'),
            dcc.Graph(id='compliance-pie'),
            dcc.Graph(id='ai-impact-histogram'),
            dcc.Graph(id='geolocation-map'),
            dcc.Graph(id='heatmap-graph'),
        ], style={'width': '70%', 'display': 'inline-block', 'padding': '20px'}),
    ]),
    # Div para tabela de transações
    html.Div([
        html.H3("Detalhes das Transações"),
        html.Div(id='transactions-table')
    ], style={'padding': '20px'}),
    # Componente Intervalo para atualização em tempo real
    dcc.Interval(
        id='interval-component',
        interval=2*1000,  # Atualiza a cada 2 segundos
        n_intervals=0
    )
])

# ====================
# Callback para Atualização do Dashboard
# ====================

@app.callback(
    [Output('transactions-time-series', 'figure'),
     Output('compliance-pie', 'figure'),
     Output('ai-impact-histogram', 'figure'),
     Output('geolocation-map', 'figure'),
     Output('heatmap-graph', 'figure'),
     Output('summary-div', 'children'),
     Output('transactions-table', 'children')],
    [Input('date-range-picker', 'start_date'),
     Input('date-range-picker', 'end_date'),
     Input('amount-threshold-slider', 'value'),
     Input('transaction-type-dropdown', 'value'),
     Input('location-dropdown', 'value'),
     Input('interval-component', 'n_intervals')]
)
def update_dashboard(start_date, end_date, amount_threshold, transaction_types, locations, n_intervals):
    """
    Atualiza os componentes do dashboard com base nos filtros e dados em tempo real.
    """
    global df_transacoes
    with lock:
        # Filtragem dos dados com base nos filtros selecionados
        filtered_df = df_transacoes.copy()
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date) + timedelta(days=1)
        filtered_df = filtered_df[(filtered_df['Date'] >= start_date) & (filtered_df['Date'] < end_date)]
        filtered_df = filtered_df[filtered_df['Transaction_Type'].isin(transaction_types)]
        filtered_df = filtered_df[filtered_df['Location'].isin(locations)]
        contas_lista_negra_atualizada = gerar_contas_lista_negra()
        filtered_df = aplicar_verificacao_conformidade(filtered_df, amount_threshold, contas_lista_negra_atualizada)
        filtered_df = detectar_anomalias(filtered_df)
        filtered_df['Notification'] = filtered_df.apply(enviar_notificacao, axis=1)

        # Cálculos para o resumo
        total_sol = filtered_df['Amount_SOL'].sum()
        conformes = filtered_df[filtered_df['Compliance_Status'] == "Conforme"].shape[0]
        nao_conformes = filtered_df[filtered_df['Compliance_Status'] == "Não Conforme"].shape[0]
        suspeitas = filtered_df[filtered_df['Anomaly_Score'] == -1].shape[0]
        lucro_esperado = (conformes * 0.05 * total_sol) - ((nao_conformes + suspeitas) * 0.02 * total_sol)

        # Gráfico de séries temporais de transações
        fig_time_series = px.line(filtered_df.sort_values('Date'), x='Date', y='Amount_SOL', color='Compliance_Status',
                                  title="Transações ao Longo do Tempo",
                                  labels={'Amount_SOL': 'Valor (SOL)', 'Date': 'Data'})

        # Gráfico de pizza de conformidade
        fig_conformidade = px.pie(filtered_df, names='Compliance_Status',
                                  title="Distribuição de Conformidade",
                                  color_discrete_sequence=px.colors.sequential.RdBu)

        # Gráfico de impacto dos agentes de IA
        fig_impacto_ia = px.histogram(filtered_df, x='Compliance_Status',
                                      title="Impacto dos Agentes de IA",
                                      labels={'Compliance_Status': 'Status de Conformidade'})

        # Gráfico de barras com cores distintas por localização
        fig_mapa = px.bar(filtered_df, x='Location', y='Amount_SOL', color='Location',
                          title="Distribuição Geográfica",
                          labels={'Amount_SOL': 'Valor (SOL)', 'Location': 'Localização'},
                          color_discrete_sequence=px.colors.qualitative.Vivid)

        # Mapa de calor (heatmap) para análise de valor médio por localização e tipo de transação
        heatmap_data = filtered_df.groupby(['Location', 'Transaction_Type'])['Amount_SOL'].mean().reset_index()
        fig_heatmap = px.density_heatmap(heatmap_data, x='Location', y='Transaction_Type', z='Amount_SOL',
                                         color_continuous_scale='Viridis',
                                         title='Mapa de Calor do Valor Médio por Localização e Tipo de Transação')

        # Resumo das informações
        summary_div = html.Div([
            html.H3("Resumo"),
            html.P(f"Total Movimentado: {total_sol:.2f} SOL"),
            html.P(f"Transações Conformes: {conformes}"),
            html.P(f"Transações Não Conformes: {nao_conformes}"),
            html.P(f"Transações Suspeitas: {suspeitas}"),
            html.P(f"Lucro Potencial com Automação: {lucro_esperado:.2f} SOL")
        ])

        # Tabela de transações
        transactions_table = dash_table.DataTable(
            data=filtered_df.tail(500).to_dict('records'),
            columns=[{'name': col, 'id': col} for col in filtered_df.columns],
            style_table={'overflowX': 'auto'},
            page_size=10,
            style_cell={'textAlign': 'left'},
            filter_action='native',
            sort_action='native'
        )

    return fig_time_series, fig_conformidade, fig_impacto_ia, fig_mapa, fig_heatmap, summary_div, transactions_table

# ====================
# Execução do Aplicativo Dash
# ====================

if __name__ == '__main__':
    app.run_server(debug=False, use_reloader=False)