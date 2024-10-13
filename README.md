# Simulador de Preços de Ações usando o Método de Monte Carlo

Este projeto é uma simulação de preços de ações utilizando o **Método de Monte Carlo**. O código simula possíveis trajetórias do preço da ação da **Microsoft (MSFT)** com base em dados históricos, utilizando retornos logarítmicos e uma distribuição normal para estimar os retornos futuros.

## Requisitos

Antes de executar o código, certifique-se de que você tenha as seguintes bibliotecas Python instaladas:

- `yfinance`: Para baixar os dados financeiros da ação.
- `numpy`: Para operações numéricas, como geração de números aleatórios.
- `matplotlib`: Para visualização dos preços simulados.

Você pode instalar essas bibliotecas executando o seguinte comando:

```bash
pip install yfinance numpy matplotlib
```

## Funcionamento do Código
 O código realiza os seguintes passos:

Download dos dados históricos: Os preços ajustados da ação MSFT são baixados usando a biblioteca yfinance.


Cálculo dos retornos logarítmicos: Com base nos preços ajustados, são calculados os retornos diários em forma logarítmica.


Cálculo da média e do desvio padrão: Os retornos são usados para calcular a média (mu) e o desvio padrão (sigma), que serão aplicados nas simulações.


Simulação de Preços: Usando uma distribuição normal baseada na média e no desvio padrão, o código gera 365 dias de retornos simulados e projeta os preços futuros.


Visualização das Simulações: O código realiza 100 simulações de preços futuros e as plota em um gráfico, destacando o último preço real da ação como referência.


## Exemplo de Gráfico
O gráfico gerado pelo código apresentará 100 possíveis trajetórias do preço da ação, todas baseadas nos dados históricos e nas características estatísticas dos retornos da ação.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request para melhorias e novas funcionalidades.
