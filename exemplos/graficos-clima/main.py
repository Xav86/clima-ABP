import subprocess

# Executar o script de gráficos diários
print("Executando clima_diario.py...")
subprocess.run(["python3", "./exemplos/graficos-clima/code/clima_diario.py"], check=True)

# Executar o script de gráficos semanais
print("Executando clima_semanal.py...")
subprocess.run(["python3", "./exemplos/graficos-clima/code/clima_semanal.py"], check=True)

print("Todos os gráficos foram gerados com sucesso!")
