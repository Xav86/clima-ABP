import json
import matplotlib.pyplot as plt
from datetime import datetime
import os

caminho_path = "./exemplos/graficos-clima/graficos/diario"

# Criar diretório de saída se não existir
os.makedirs(f"{caminho_path}", exist_ok=True)

# Caminho do arquivo JSON
file_path = "./exemplos/retorno-api-visualcrossing.json"

# Carregar dados
with open(file_path, "r") as file:
    data = json.load(file)

# Selecionar dados do dia 05/05/2025
day_data = next(day for day in data["days"] if day["datetime"] == "2025-05-05")
hourly_data = day_data["hours"]

# Extrair hora formatada
horas = [datetime.strptime(hour["datetime"], "%H:%M:%S").strftime("%H:%M") for hour in hourly_data]

# Extrair variáveis convertidas
solarenergy = [hour["solarenergy"] for hour in hourly_data]
uvindex = [hour["uvindex"] for hour in hourly_data]
cloudcover = [hour["cloudcover"] for hour in hourly_data]
snow = [hour["snow"] for hour in hourly_data]
windspeed = [(hour["windspeed"]) for hour in hourly_data]  # já está em km/h
precipprob = [hour["precipprob"] for hour in hourly_data]
feelslike_c = [(hour["feelslike"] - 32) * 5 / 9 for hour in hourly_data]
temperaturas_c = [(hour["temp"] - 32) * 5 / 9 for hour in hourly_data]

# Função para criar gráfico simples
def criar_grafico(x, y, titulo, ylabel, cor, nome_arquivo):
    plt.figure(figsize=(8.7, 3.5))
    plt.plot(x, y, marker='o', color=cor)
    plt.title(titulo)
    plt.xlabel("Hora do dia")
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{caminho_path}/{nome_arquivo}")
    plt.close()

# Criar gráficos
criar_grafico(horas, temperaturas_c, "Temperatura ao longo do dia - 05/05/2025 (Criciúma, SC)",
              "Temperatura (°C)", "#d00000", "grafico-temperatura.png")

criar_grafico(horas, feelslike_c, "Sensação térmica ao longo do dia - 05/05/2025 (Criciúma, SC)",
              "Sensação térmica (°C)", "#f77f00", "grafico-sensacao-termica.png")

criar_grafico(horas, windspeed, "Velocidade do vento ao longo do dia - 05/05/2025 (Criciúma, SC)",
              "Velocidade do vento (km/h)", "#0077b6", "grafico-velocidade-vento.png")

criar_grafico(horas, precipprob, "Chance de precipitação ao longo do dia - 05/05/2025 (Criciúma, SC)",
              "Probabilidade de precipitação (%)", "#023e8a", "grafico-precipitacao.png")

criar_grafico(horas, cloudcover, "Cobertura de nuvens ao longo do dia - 05/05/2025 (Criciúma, SC)",
              "Cobertura de nuvens (%)", "#b744b8", "grafico-cobertura-nuvens.png")

criar_grafico(horas, uvindex, "Índice UV ao longo do dia - 05/05/2025 (Criciúma, SC)",
              "Índice UV", "#ff0000", "grafico-indice-uv.png")

criar_grafico(horas, solarenergy, "Energia solar ao longo do dia - 05/05/2025 (Criciúma, SC)",
              "Energia solar (MJ/m²)", "#ef476f", "grafico-energia-solar.png")

criar_grafico(horas, snow, "Neve acumulada ao longo do dia - 05/05/2025 (Criciúma, SC)",
              "Neve (mm)", "#adb9e3", "grafico-neve.png")
