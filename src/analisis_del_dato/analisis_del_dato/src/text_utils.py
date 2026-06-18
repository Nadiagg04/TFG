"""Utilidades de texto para el análisis del dato del TFG."""

import re
import pandas as pd


def limpiar_texto_suave(texto):
    """Limpieza mínima para mantener información útil para modelos preentrenados."""
    if pd.isna(texto):
        return ""
    texto = str(texto)
    texto = re.sub(r"http\S+|www\.\S+", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


def validar_columnas(df, columnas, nombre_df="dataframe"):
    faltantes = [c for c in columnas if c not in df.columns]
    if faltantes:
        raise ValueError(f"Faltan columnas en {nombre_df}: {faltantes}")
    return True
