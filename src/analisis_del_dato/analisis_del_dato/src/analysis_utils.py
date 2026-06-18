"""Utilidades para construir el ITI mensual y compararlo con el ICC."""

import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr


def construir_indice_tono(tweets):
    """Agrega sentimientos por mes y calcula ITI = (positivos - negativos) / total."""
    df = tweets.copy()
    df["mes"] = pd.to_datetime(df["mes"])
    tabla = (
        df.pivot_table(index="mes", columns="sentimiento_modelo", values="id", aggfunc="count", fill_value=0)
        .reset_index()
    )
    for col in ["positivo", "negativo", "neutro"]:
        if col not in tabla.columns:
            tabla[col] = 0
    tabla = tabla.rename(columns={"positivo": "n_positivo", "negativo": "n_negativo", "neutro": "n_neutro"})
    tabla["total_tweets"] = tabla[["n_positivo", "n_negativo", "n_neutro"]].sum(axis=1)
    tabla["pct_positivo"] = np.where(tabla["total_tweets"] > 0, tabla["n_positivo"] / tabla["total_tweets"], np.nan)
    tabla["pct_negativo"] = np.where(tabla["total_tweets"] > 0, tabla["n_negativo"] / tabla["total_tweets"], np.nan)
    tabla["pct_neutro"] = np.where(tabla["total_tweets"] > 0, tabla["n_neutro"] / tabla["total_tweets"], np.nan)
    tabla["ITI"] = np.where(tabla["total_tweets"] > 0, (tabla["n_positivo"] - tabla["n_negativo"]) / tabla["total_tweets"], np.nan)
    return tabla.sort_values("mes")


def calcular_correlacion_segura(df, x, y, metodo="pearson"):
    tmp = df[[x, y]].dropna()
    if len(tmp) < 3 or tmp[x].nunique() < 2 or tmp[y].nunique() < 2:
        return {"metodo": metodo, "n": len(tmp), "correlacion": np.nan, "p_value": np.nan}
    if metodo == "pearson":
        corr, p = pearsonr(tmp[x], tmp[y])
    elif metodo == "spearman":
        corr, p = spearmanr(tmp[x], tmp[y])
    else:
        raise ValueError("metodo debe ser pearson o spearman")
    return {"metodo": metodo, "n": len(tmp), "correlacion": corr, "p_value": p}


def tabla_correlaciones_desfases(df, iti_col="ITI", icc_col="ICC"):
    """Correlaciones en niveles y diferencias con desfases -1, 0, +1."""
    base = df.copy().sort_values("mes")
    resultados = []
    for lag in [-1, 0, 1]:
        temp = base.copy()
        temp["ICC_lag"] = temp[icc_col].shift(-lag)
        etiqueta = f"ITI_m vs ICC_m{lag:+d}" if lag else "ITI_m vs ICC_m"
        for metodo in ["pearson", "spearman"]:
            r = calcular_correlacion_segura(temp, iti_col, "ICC_lag", metodo)
            r.update({"tipo": "niveles", "desfase": lag, "comparacion": etiqueta})
            resultados.append(r)

        temp["d_ITI"] = temp[iti_col].diff()
        temp["d_ICC_lag"] = temp["ICC_lag"].diff()
        for metodo in ["pearson", "spearman"]:
            r = calcular_correlacion_segura(temp, "d_ITI", "d_ICC_lag", metodo)
            r.update({"tipo": "diferencias_intermensuales", "desfase": lag, "comparacion": etiqueta})
            resultados.append(r)
    return pd.DataFrame(resultados)
