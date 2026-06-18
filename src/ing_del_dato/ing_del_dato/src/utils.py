from pathlib import Path
import re
import pandas as pd


def crear_directorios(lista_paths):
    """Crear directorios si no existen."""
    for ruta in lista_paths:
        Path(ruta).mkdir(parents=True, exist_ok=True)


def limpiar_texto(texto: str) -> str:
    """Limpieza básica de texto para tweets institucionales."""
    texto = str(texto)
    texto = re.sub(r"http\S+|www\.\S+", " ", texto)
    texto = re.sub(r"@\w+", " ", texto)
    texto = re.sub(r"#", "", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto.lower()


def normalizar_metricas(df: pd.DataFrame, columnas):
    """Normaliza métricas numéricas eliminando separadores y forzando enteros."""
    df = df.copy()
    for col in columnas:
        if col not in df.columns:
            raise ValueError(f"Columna requerida no encontrada: {col}")
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.strip()
            .replace("", "0")
            .pipe(pd.to_numeric, errors="coerce")
            .fillna(0)
            .astype(int)
        )
    return df


def resumen_nulos(df: pd.DataFrame) -> pd.DataFrame:
    """Genera un resumen de nulos por columna."""
    nulos = df.isnull().sum()
    resumen = pd.DataFrame({
        "nulos": nulos,
        "%_nulos": (nulos / len(df) * 100).round(2)
    })
    return resumen.sort_values("nulos", ascending=False)


def detectar_outliers_iqr(df: pd.DataFrame, columnas):
    """Detecta outliers por IQR en columnas numéricas y devuelve un resumen."""
    resumen = []
    for col in columnas:
        if col not in df.columns:
            raise ValueError(f"Columna requerida no encontrada: {col}")
        serie = pd.to_numeric(df[col], errors="coerce")
        q1 = serie.quantile(0.25)
        q3 = serie.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        mask_outliers = serie.lt(lower) | serie.gt(upper)
        resumen.append({
            "columna": col,
            "q1": q1,
            "q3": q3,
            "iqr": iqr,
            "limite_inferior": lower,
            "limite_superior": upper,
            "n_outliers": int(mask_outliers.sum()),
            "%_outliers": round(mask_outliers.mean() * 100, 2),
            "total": int(len(serie)),
        })
    return pd.DataFrame(resumen).set_index("columna")
