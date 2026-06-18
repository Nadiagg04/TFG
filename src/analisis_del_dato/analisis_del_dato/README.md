# Análisis del dato — TFG Business Analytics

## Tema

“Comparativa del índice sentimiento del consumidor con el análisis de sentimiento del discurso con tweets de ministerio de comercio en distintos momentos”.

A efectos metodológicos, el índice de sentimiento/confianza del consumidor se operacionaliza mediante el Índice de Confianza del Consumidor (ICC), y el discurso institucional se analiza a partir de tweets de cuentas vinculadas al ámbito económico-comercial, con corpus principal en `@_minecogob`.

## Enfoque

Esta fase aplica un modelo preentrenado de análisis de sentimiento en español (`pysentimiento`) al corpus de tweets institucionales. No se entrena un modelo supervisado propio ni se predice el ICC. La comparación posterior entre el índice de tono institucional y el ICC es exploratoria y correlacional, no causal.

## Orden de ejecución

1. Instalar dependencias: `pip install -r requirements.txt`.
2. Ejecutar `notebooks/01_muestreo_etiquetado.ipynb` para generar la muestra de revisión cualitativa de 60 tweets.
3. Ejecutar `notebooks/02_modelos_sentimiento.ipynb` para clasificar los tweets con `pysentimiento`.
4. Ejecutar `notebooks/02b_clustering_tematico.ipynb` para analizar agrupaciones temáticas no supervisadas de tweets.
5. Ejecutar `notebooks/03_comparacion_icc_sentimiento.ipynb` para construir el ITIm y compararlo con el ICC.

## Outputs principales

- `data/processed/tweets_clasificados_sentimiento.csv`
- `data/processed/indice_tono_institucional_mensual.csv`
- `data/processed/dataset_icc_sentimiento_mensual.csv`
- `data/labels/muestra_revision_cualitativa.csv`
- `outputs/tables/distribucion_global_sentimiento.csv`
- `outputs/tables/distribucion_mensual_sentimiento.csv`
- `outputs/tables/metricas_descriptivas_modelo.csv`
- `outputs/tables/correlaciones_iti_icc.csv`
- `outputs/tables/resumen_interpretacion_resultados.csv`
- `outputs/tables/metricas_clustering.csv`
- `outputs/tables/clusters_terminos_principales.csv`
- `outputs/tables/ejemplos_clusters_tweets.csv`
- `outputs/figures/metricas_clustering_k.png`
- `outputs/figures/distribucion_clusters_tweets.png`
- `outputs/figures/evolucion_clusters_mensual.png`
- Figuras en `outputs/figures/`.

## Resultados técnicos resumidos

- Tweets clasificados: 4,590
- Cobertura de clasificación: 100.0%
- Confianza media del modelo: 0.6684
- Distribución global: 84.20% neutro, 13.75% positivo y 2.05% negativo.
- Meses comparables ITIm–ICC: 68
- Correlación contemporánea Spearman ITIm–ICC: 0.269 (p = 0.027)
- Correlación Spearman ITIm vs ICC del mes anterior: 0.308 (p = 0.011)

## Limitaciones

La ausencia de una muestra manual amplia impide calcular métricas supervisadas como accuracy, precision, recall o F1-score. En su lugar, se documentan medidas descriptivas, distribución de clases, cobertura, confianza media, correlaciones temporales y revisión cualitativa reducida. No se afirma causalidad ni se predice el ICC.
