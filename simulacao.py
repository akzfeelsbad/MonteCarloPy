import yfinance as yf  # Importa a biblioteca para baixar dados financeiros
import numpy as np  # Biblioteca para manipulação numérica
import matplotlib.pyplot as plt  # Biblioteca para visualização de dados

# Baixa os dados históricos da ação da Microsoft (MSFT) do Yahoo Finance
df = yf.download("MSFT")

# Calcula os retornos logarítmicos com base no preço ajustado de fechamento
# O uso de logaritmo simplifica cálculos de retorno composto
returns = np.log(1 + df['Adj Close'].pct_change())

# Calcula a média (mu) e o desvio padrão (sigma) dos retornos diários
mu, sigma = returns.mean(), returns.std()

# Simula 365 retornos diários com base na distribuição normal
# A distribuição normal é criada usando a média e desvio padrão dos retornos históricos
sim_rets = np.random.normal(mu, sigma, 365)

# Pega o preço de fechamento ajustado mais recente como valor inicial
initial = df['Adj Close'].iloc[-1]

# Calcula os preços simulados para os próximos 365 dias
# O preço inicial é multiplicado pelo retorno acumulado (sim_rets + 1).cumprod() calcula o produto cumulativo
sim_prices = initial * (sim_rets + 1).cumprod()

# Plota a primeira simulação de preços
plt.plot(sim_prices)

# Realiza 100 simulações adicionais para observar o comportamento do preço
for i in range(100):
    # Para cada iteração, gera uma nova série de 365 retornos diários simulados
    sim_rets = np.random.normal(mu, sigma, 365)
    
    # Calcula os preços simulados para os próximos 365 dias baseados nos retornos simulados
    sim_prices = initial * (sim_rets + 1).cumprod()
    
    # Adiciona uma linha horizontal no gráfico para destacar o preço inicial (último preço real)
    plt.axhline(initial, c='k')
    
    # Plota a nova série de preços simulados no gráfico
    plt.plot(sim_prices)

# Exibe o gráfico com todas as simulações
plt.show()
