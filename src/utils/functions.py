"""
Funciones de limpieza de datos para el proyecto EDA Nomadismo Digital.
"""

import pandas as pd


def clean_currency_column(series: pd.Series) -> pd.Series:
    """
    Limpia una columna con valores monetarios en formato europeo.
    Elimina símbolos de moneda, comillas, y convierte formato EU a decimal.

    Formato EU: 1.059,00 → 1059.00

    Args:
        series: Columna de pandas con valores monetarios como strings

    Returns:
        Serie con valores numéricos (float64)
    """
    cleaned = series.astype(str)

    # 1. Eliminar comillas
    cleaned = cleaned.str.replace('"', '', regex=False)

    # 2. Eliminar símbolo de moneda mal encodeado (\x80 = € en latin-1) y espacios
    cleaned = cleaned.str.replace('\x80', '', regex=False)
    cleaned = cleaned.str.strip()

    # 3. Convertir formato europeo a decimal estándar
    # Si hay coma, asumimos formato EU (1.059,00 → 1059.00)
    # Quitamos puntos de miles y reemplazamos coma decimal por punto
    cleaned = cleaned.apply(lambda x: x.replace('.', '').replace(',', '.') if ',' in x else x)

    # 4. Convertir a float
    cleaned = pd.to_numeric(cleaned, errors='coerce')

    return cleaned


