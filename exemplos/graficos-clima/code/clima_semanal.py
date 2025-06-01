import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

caminho_path = "./exemplos/graficos-clima/graficos/semanal"

# Criar pasta de saída se não existir
os.makedirs(f"{caminho_path}", exist_ok=True)

# Carregar dados do JSON
with open("./exemplos/retorno-api-visualcrossing.json") as file:
    data = json.load(file)

dias = data["days"]

# Funções auxiliares
def hora_para_minutos(hora_str):
    h, m, s = map(int, hora_str.split(":"))
    return h * 60 + m + s / 60

def minutos_para_hora_str(minutos):
    h = int(minutos) // 60
    m = int(minutos) % 60
    return f"{h:02d}:{m:02d}"

def fase_lua_nome(valor):
    if valor < 0.1 or valor >= 0.9:
        return "Lua Nova"
    elif 0.1 <= valor < 0.4:
        return "Quarto Crescente"
    elif 0.4 <= valor < 0.6:
        return "Lua Cheia"
    elif 0.6 <= valor < 0.9:
        return "Quarto Minguante"

# Criar DataFrame com dados principais
df = pd.DataFrame([{
    "Data": dia["datetime"],
    "Temperatura (°C)": (dia["temp"] - 32) * 5 / 9,
    "Chance de Precipitação (%)": dia.get("precipprob", 0.0),
    "Velocidade do Vento (km/h)": dia.get("windspeed", 0.0),
    "Índice UV": dia.get("uvindex", 0.0),
    "Energia Solar (MJ/m²)": dia.get("solarenergy", 0.0),
    "Cobertura de Nuvens (%)": dia.get("cloudcover", 0.0),
    "Sensação Térmica (°C)": (dia["feelslike"] - 32) * 5 / 9,
    "Fase da Lua": dia["moonphase"],
    "Nascer do Sol": hora_para_minutos(dia["sunrise"]),
    "Pôr do Sol": hora_para_minutos(dia["sunset"]),
    "Neve (mm)":dia.get("snow", 0.0)
} for dia in dias])

# Plotador genérico de clima
def plot_variavel(nome_coluna, titulo, unidade, cor_max, cor_med, cor_min, cor_linha, nome_arquivo):
    resumo = df[nome_coluna].agg(['min', 'mean', 'max'])

    plt.figure(figsize=(8, 5))
    plt.plot(df["Data"], df[nome_coluna], marker='o', color=cor_linha, label=f'{nome_coluna} diário')
    plt.axhline(resumo["max"], linestyle='--', color=cor_max, label='Máximo')
    plt.axhline(resumo["mean"], linestyle='-', color=cor_med, label='Médio')
    plt.axhline(resumo["min"], linestyle='--', color=cor_min, label='Mínimo')

    plt.title(titulo)
    plt.xlabel("Data")
    plt.ylabel(unidade)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{caminho_path}/{nome_arquivo}")
    plt.close()

# Gráficos principais
plot_variavel("Temperatura (°C)", "Temperatura durante a semana - Criciúma, SC", "Temperatura (°C)", "#9d0208", "#d00000", "#dc2f02", "black", "grafico-temperatura.png")
plot_variavel("Velocidade do Vento (km/h)", "Velocidade do vento durante a semana - Criciúma, SC", "Velocidade do Vento (Km/h)", "#0077b6", "#00b4d8", "#90e0ef", "black", "grafico-velocidade-vento.png")
plot_variavel("Sensação Térmica (°C)", "Sensação térmica durante a semana - Criciúma, SC", "Sensação Térmica (°C)", "#f77f00", "#d62828", "#003049", "black", "grafico-sensacao-termica.png")
plot_variavel("Índice UV", "Índice UV durante a semana - Criciúma, SC", "Índice UV", "#ff0000", "#ffdd00", "#55a630", "black", "grafico-indice-uv.png")
plot_variavel("Energia Solar (MJ/m²)", "Energia solar gerada durante a semana - Criciúma, SC", "Energia Solar (MJ/m²)", "#421196", "#ffc719", "#ff193b", "black", "grafico-energia-solar.png")
plot_variavel("Cobertura de Nuvens (%)", "Chance de precipitação durante a semana - Criciúma, SC", "Cobertura de Nuvens (%)", "#b744b8", "#a379c9", "#adb9e3", "black", "grafico-cobertura-nuvens.png")
plot_variavel("Chance de Precipitação (%)", "Chance de precipitação durante a semana - Criciúma, SC", "Precipitação (%)", "#023e8a", "#00b4d8", "#48cae4", "black", "grafico-precipitacao.png")
plot_variavel("Neve (mm)","Neve prevista durante a semana - Criciúma, SC", "Neve (mm)", "#adb5bd", "#ced4da", "#dee2e6", "black","grafico-neve.png")

# Gráfico do sol
plt.figure(figsize=(10, 6))
plt.plot(df["Data"], df["Nascer do Sol"], marker='o', color='orange', label='Nascer do Sol')
plt.plot(df["Data"], df["Pôr do Sol"], marker='o', color='darkred', label='Pôr do Sol')

y_ticks = range(int(df["Nascer do Sol"].min()) - 15, int(df["Pôr do Sol"].max()) + 15, 30)
y_labels = [minutos_para_hora_str(m) for m in y_ticks]
plt.yticks(ticks=y_ticks, labels=y_labels)

plt.title("Horários de Nascer e Pôr do Sol - Criciúma (SC)")
plt.xlabel("Data")
plt.ylabel("Horário")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(f"{caminho_path}/grafico-sol.png")
plt.close()

# Gráfico da Lua
plt.figure(figsize=(10, 5))
plt.plot(df["Data"], df["Fase da Lua"], marker='o', color='purple')
plt.ylim(-0.1, 1.1)
plt.yticks([0.0, 0.25, 0.5, 0.75, 1.0],
           ["Lua Nova", "Quarto Crescente", "Lua Cheia", "Quarto Minguante", "Lua Nova"])
plt.grid(True)
plt.title("Fases da Lua - Criciúma (SC)")
plt.xlabel("Data")
plt.ylabel("Fase da Lua")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{caminho_path}/grafico-fase-lua.png")
plt.close()
