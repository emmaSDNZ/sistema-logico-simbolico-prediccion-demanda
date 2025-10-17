from data_generator import DataGeneration
from logic_engine import LogicEngine

import pandas as pd

def main():
    print("Sistema Lógico de Stock – Iniciando motor lógico...")

    # 1. Generar datos
    gen =  DataGeneration(n=5)
    df = gen.generar_dataset()
    
    # 2. Aplicar motor lógico
    motor = LogicEngine()
    resultados = motor.clasificar_dataset(df)

    # 3. Guardar CSV
    resultados.to_csv("resultados.csv", index=False)
    print("✅ Archivo 'resultados.csv' generado con éxito.\n")
    print(resultados)

if __name__ == "__main__":
    main()