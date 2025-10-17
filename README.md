
# Sistema Lógico-Simbólico para Planificación de Stock

### Proyecto Integrador — Ciencia de Datos e Inteligencia Artificial

**Autores:** 
Martin, Mauro Leonel
Isaias Emanuel Sudañez
Enrico Munighinim Antonella Stefania
Marovich, Mikael Davor
Villaruel,Tomas Adrian
Barrera Randazzo, Tomas Valentin

**Docente:** Charletti, Calor 

**Año:** 2025

**Tipo de Proyecto:** Tecnologico

---

## Descripción General

El presente proyecto desarrolla un **sistema lógico-simbólico inteligente** orientado a la **planificación de stock y producción** en entornos comerciales dinámicos, con aplicación específica en el sector de **panaderías y pastelerías**.

El sistema constituye un **prototipo de arquitectura simbólica explicable**, donde el conocimiento experto del negocio se formaliza mediante **reglas lógicas interpretables**, garantizando **transparencia, auditabilidad y trazabilidad** en las decisiones operativas.

Esta propuesta se ubica dentro de la **etapa de modelado y validación de conocimiento** del pipeline de Ciencia de Datos, previo al modelado estadístico o de aprendizaje automático. Su objetivo es **transformar conocimiento tácito en un modelo lógico funcional**, capaz de generar recomendaciones operativas basadas en evidencia y reglas claras.

---

##  Objetivo General: Data-Driven & Business-Oriented

> Desarrollar un sistema inteligente de planificación de stock que permita **anticipar la demanda, evitar faltantes y desperdicios, optimizar la producción y mejorar la eficiencia operativa**, generando decisiones **explicables, auditables y basadas en datos históricos y eventos externos**, con visión de escalabilidad hacia futuras integraciones predictivas.

---

## Objetivos Específicos: Orientados al valor del negocio

1. **Capturar conocimiento del negocio** mediante la formalización de reglas lógicas que describen comportamientos de demanda, reposición y eventos relevantes.
2. **Automatizar la toma de decisiones operativas** en base a condiciones observables (clima, tipo de producto, tendencias históricas, etc.), reduciendo incertidumbre y tiempos de planificación.
3. **Generar decisiones explicables y auditables**, donde cada recomendación de producción o reposición pueda justificarse a partir de la activación de reglas simbólicas específicas.
4. **Evaluar el impacto de las decisiones lógicas** sobre indicadores de negocio como reducción de faltantes, minimización de desperdicios y mejora en la eficiencia del stock.
5. **Proveer una base sólida para modelos de IA explicable (XAI)**, donde el sistema simbólico funcione como capa de validación y trazabilidad para futuros modelos predictivos.

---

## Arquitectura del Sistema

El sistema se estructura en tres módulos principales, diseñados bajo principios de **Programación Orientada a Objetos (POO)** y **modularidad funcional**:

| Módulo                     | Descripción                                                                                                                                  | Archivo             |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| **Generador de Datos**     | Simula escenarios operativos realistas con variables contextuales (clima, eventos, ubicación, stock, etc.).                                  | `data_generator.py` |
| **Motor Lógico-Simbólico** | Aplica reglas de decisión codificadas en lógica proposicional, determinando la recomendación de producción y su explicación correspondiente. | `logic_engine.py`   |
| **Ejecución y Validación** | Coordina el flujo completo: generación de datos, evaluación lógica, registro de resultados y exportación a CSV.                              | `main.py`           |

El resultado final se almacena en **`resultados.csv`**, que integra los valores de entrada junto a la **recomendación lógica (Alta, Media o Baja)** y la **justificación del razonamiento** que llevó a dicha decisión.

---

## Marco Conceptual

El sistema se inspira en los principios de la **IA simbólica** y la **explicabilidad computacional (XAI)**, donde la lógica formal actúa como medio para **hacer visible el razonamiento de la máquina**.

En contraposición a los modelos de caja negra, este enfoque busca **preservar la interpretabilidad**, permitiendo que el usuario comprenda **por qué** el sistema recomienda una acción determinada, fortaleciendo así la **confianza y validación operativa**.

Desde la perspectiva de Ciencia de Datos, el modelo constituye un **eslabón previo al Machine Learning**, enfocado en la **extracción, representación y validación del conocimiento experto**, siguiendo la estructura del **pipeline simbólico**:

**Adquisición → Formalización → Inferencia → Explicabilidad → Validación.**

---

## Resultados Esperados

* **Recomendaciones automáticas y justificadas** de niveles de producción (Alta, Media, Baja).
* **Identificación de condiciones críticas** (clima, eventos, stock, tendencia) que influyen en la demanda.
* **Generación de un registro trazable** (`resultados.csv`) para análisis posterior.
* **Base estructural para modelos híbridos** (simbólico + estadístico) orientados a predicción y optimización continua.

---

## Alcance Científico y Aplicativo

Este trabajo consolida una **metodología híbrida** entre lógica, programacion y las bases de inteligencia artificial aplicada, alineada con los principios de **IA responsable y explicable**.

El prototipo es escalable a **sistemas ERP, dashboards analíticos o pipelines de predicción**, y se configura como un **módulo de validación simbólica**, útil tanto para la **enseñanza de IA interpretable** como para su **implementación real en entornos empresariales**.

---

## Ejemplo de Salida (`resultados.csv`)

| EsFinDeSemana | ClimaLluvioso | DiaFestivo | EventoEspecial | Recomendacion | Razonamiento                                                     |
| ------------- | ------------- | ---------- | -------------- | ------------- | ---------------------------------------------------------------- |
| 1             | 0             | 0          | 0              | **Alta**      | Regla A: Demanda combinada (día especial + flujo/tendencia alta) |
| 0             | 1             | 0          | 0              | **Baja**      | Regla C: Clima adverso o tendencia baja                          |
| 0             | 0             | 1          | 0              | **Alta**      | Regla A: Día festivo con tendencia alta                          |

---

##  Perspectiva Futura

La siguiente etapa contempla la integración de modelos **predictivos basados en aprendizaje automático (ML)** y el uso de **frameworks de explicabilidad (LIME, SHAP)** para contrastar el **modelo simbólico** con **modelos estadísticos o neuronales**, consolidando un entorno de **IA híbrida, transparente y validable**.

---

## Referencias Conceptuales

* Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach.*
* Marcus, G. (2022). *The Next Decade in AI: Hybrid Models and Symbolic Reasoning.*
* European Commission
# sistema-logico-simbolico-prediccion-demanda
