import pandas as pd

class LogicEngine:
    def __init__(self):
        self.prioridad = ["Alta", " "]

    def evaluar_reglas(self, fila):
        F = fila["EsFinDeSemana"]
        L = fila["ClimaLluvioso"]
        X = fila["DiaFestivo"]
        E = fila["EventoEspecial"]
        U = fila["UbicacionCentrica"]
        C = fila["FlujoClientesAlto"]
        T = fila["TendenciaHistoricaAlta"]
        S = fila["StockInicial_Bajo"]

        reglas_activadas = []
        recomendacion = None


        # --- Regla A: Alta Producción ---
        if ((F or X or E) and (C or T)) or (U and C):
            recomendacion = "Alta"
            reglas_activadas.append("Regla A: Demanda combinada (día especial + flujo/tendencia alta)")
        
        # --- Regla B: Producción Media ---
        elif S and not (C or (F or X or E)):
            recomendacion = "Media"
            reglas_activadas.append("Regla B: Stock bajo sin alta demanda")
        
        # --- Regla C: Producción Baja ---
        elif (L and not (F or X or E)) or not T:
            recomendacion = "Baja"
            reglas_activadas.append("Regla C: Clima adverso o tendencia baja")

        else:
            recomendacion = "Baja"
            reglas_activadas.append("Sin condiciones especiales — baja por defecto")

        return recomendacion, " | ".join(reglas_activadas)
    
    def clasificar_dataset(self, df):
        resultados = []
        for _, fila in df.iterrows():
            rec, razon = self.evaluar_reglas(fila)
            resultados.append({"Recomendacion": rec, "Razonamiento": razon})
        resultados_df = pd.DataFrame(resultados)
        return pd.concat([df, resultados_df], axis=1)