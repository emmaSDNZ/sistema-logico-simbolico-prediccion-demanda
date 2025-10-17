import pandas as pd
import random 

class DataGeneration:
    def __init__(self, n = 5, seed= 42):
        self.n = n
        random.seed(seed)
    
    def generar_fila(self):
        return {
            "EsFinDeSemana": random.choice([0, 1]),
            "ClimaLluvioso": random.choice([0, 1]),
            "DiaFestivo": random.choice([0, 1]),
            "EventoEspecial": random.choice([0, 1]),
            "UbicacionCentrica": random.choice([0, 1]),
            "FlujoClientesAlto": random.choice([0, 1]),
            "TendenciaHistoricaAlta": random.choice([0, 1]),
            "StockInicial_Bajo": random.choice([0, 1]),
            "TipoProducto_Pan": random.choice([1, 0]),
            "TipoProducto_Pasteleria": random.choice([1, 0]),
            "TipoProducto_Sandwich": random.choice([1, 0]),
            "TipoProducto_Bebida": random.choice([1, 0])
        }
        
    def generar_dataset(self):
        data = [self.generar_fila() for _ in range(self.n)]
        df = pd.DataFrame(data)
        return df