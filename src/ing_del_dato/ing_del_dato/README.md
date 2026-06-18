# Ingeniería del Dato — TFG

## Objetivo del proyecto

Este repositorio organiza la ingeniería del dato para el trabajo de fin de grado:

> “Comparativa del índice de confianza del consumidor con el análisis de sentimiento del discurso con tweets de Ministerio de Comercio en distintos momentos”.

El notebook se centra en la preparación, validación y exportación de los datos necesarios para comparar la evolución mensual del ICC con el discurso institucional en Twitter, sin incluir modelado ni predicción.

## Estructura del proyecto

- `data/raw/`
  - `tweets_gobierno_economia.csv`
  - `evolucion_de_la_confianza_del_consumidor_desde_2004.csv`
- `data/processed/`
  - `tweets_limpios_2020_2025_minecogob.csv`
  - `tweets_comercio_complementario_2020_2025.csv`
  - `icc_2020_2025_limpio.csv`
  - `dataset_mensual_tweets_icc.csv`
- `notebooks/`
  - `ingenieria_dato_tfg.ipynb`
- `outputs/figures/`
  - Gráficos descriptivos guardados en PNG
- `outputs/tables/`
  - Tablas de calidad y cobertura exportadas en CSV
- `src/utils.py`
  - Funciones reutilizables para limpieza y validación

## Fuentes de datos

- Tweets institucionales: `data/raw/tweets_gobierno_economia.csv`
- Índice de Confianza del Consumidor: `data/raw/evolucion_de_la_confianza_del_consumidor_desde_2004.csv`

## Cómo ejecutar

1. Activar el entorno virtual de Python.
2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Abrir y ejecutar el notebook:

```bash
cd ing_del_dato/notebooks
jupyter notebook
```

4. Ejecutar todas las celdas de `ingenieria_dato_tfg.ipynb` de arriba abajo.

## Outputs generados

- `data/processed/`:
  - Datasets limpios y listos para análisis posterior.
- `outputs/tables/`:
  - Resumen de nulos, calidad, outliers y cobertura mensual.
- `outputs/figures/`:
  - Gráficos descriptivos mínimos para el informe.

## Limitaciones de la ingeniería del dato

- Este notebook cubre exclusivamente la preparación de datos y la validación estructural.
- No incluye análisis de sentimiento final ni entrenamiento de modelos.
- No realiza imputación automática ni eliminación de outliers; los datos extremos se documentan para su evaluación.

## Aclaración

Este repositorio está diseñado para el proceso de ingeniería del dato. El modelado final y la predicción del ICC no forman parte de este notebook.
