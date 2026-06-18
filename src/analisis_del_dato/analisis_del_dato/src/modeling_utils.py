"""Utilidades de modelado para aplicar un modelo preentrenado de sentimiento."""

import pandas as pd

MAP_PYSENTIMIENTO = {
    "POS": "positivo",
    "NEG": "negativo",
    "NEU": "neutro",
    "positivo": "positivo",
    "negativo": "negativo",
    "neutro": "neutro",
}


def cargar_analizador_pysentimiento():
    """Carga pysentimiento. Si no está instalado, detiene con instrucciones claras."""
    try:
        from pysentimiento import create_analyzer
    except ImportError as exc:
        raise ImportError(
            "No está instalado pysentimiento. Instálalo con: pip install pysentimiento\n"
            "Después vuelve a ejecutar este notebook. No se generan etiquetas automáticas alternativas."
        ) from exc
    return create_analyzer(task="sentiment", lang="es")


def predecir_sentimiento(analyzer, texto):
    """Predice sentimiento y devuelve etiqueta normalizada, confianza y probabilidades."""
    texto = "" if pd.isna(texto) else str(texto)
    pred = analyzer.predict(texto)
    etiqueta_raw = getattr(pred, "output", pred.output if hasattr(pred, "output") else None)
    etiqueta = MAP_PYSENTIMIENTO.get(etiqueta_raw, str(etiqueta_raw).lower())
    probs = getattr(pred, "probas", {}) or {}
    confianza = None
    if probs:
        try:
            confianza = float(max(probs.values()))
        except Exception:
            confianza = None
    return {
        "sentimiento_modelo": etiqueta,
        "confianza_modelo": confianza,
        "prob_pos": float(probs.get("POS", probs.get("positivo", 0))) if probs else None,
        "prob_neg": float(probs.get("NEG", probs.get("negativo", 0))) if probs else None,
        "prob_neu": float(probs.get("NEU", probs.get("neutro", 0))) if probs else None,
    }


def resumen_distribucion(df, col="sentimiento_modelo"):
    """Tabla de distribución global de clases."""
    out = df[col].value_counts(dropna=False).rename_axis(col).reset_index(name="n")
    out["porcentaje"] = (out["n"] / out["n"].sum() * 100).round(2)
    return out
