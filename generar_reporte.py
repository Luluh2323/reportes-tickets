"""
Automatizador de Reportes de Tickets de Soporte TI
----------------------------------------------------
Este script lee un registro de tickets de soporte técnico (CSV) y genera
automáticamente un reporte resumen en Excel, con estadísticas por categoría,
prioridad y técnico.

Autor: Lucio Llanos Sevillano
Contexto: Proyecto personal inspirado en el sistema de gestión de tickets
que utilizo en mi trabajo actual de soporte TI, con el objetivo de practicar
automatización de reportes con Python y pandas.

Nota: los datos usados (data/tickets.csv) son simulados/inventados,
no corresponden a datos reales de ninguna institución.
"""

import pandas as pd
from datetime import datetime
import os


RUTA_ENTRADA = "data/tickets.csv"
RUTA_SALIDA = "reportes/reporte_tickets.xlsx"


def cargar_datos(ruta_csv):
    """Lee el archivo CSV de tickets y lo devuelve como DataFrame."""
    if not os.path.exists(ruta_csv):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_csv}")

    df = pd.read_csv(ruta_csv, parse_dates=["fecha"])
    return df


def resumen_por_categoria(df):
    """Cantidad de tickets y tiempo promedio de resolución por categoría."""
    resumen = df.groupby("categoria").agg(
        cantidad_tickets=("id_ticket", "count"),
        tiempo_promedio_horas=("tiempo_resolucion_horas", "mean")
    ).round(2).reset_index()
    return resumen


def resumen_por_prioridad(df):
    """Cantidad de tickets por nivel de prioridad."""
    resumen = df.groupby("prioridad").agg(
        cantidad_tickets=("id_ticket", "count"),
        tiempo_promedio_horas=("tiempo_resolucion_horas", "mean")
    ).round(2).reset_index()
    return resumen


def resumen_por_tecnico(df):
    """Cantidad de tickets resueltos y tiempo total invertido por técnico."""
    resumen = df.groupby("tecnico").agg(
        tickets_resueltos=("id_ticket", "count"),
        horas_totales=("tiempo_resolucion_horas", "sum")
    ).round(2).reset_index()
    return resumen


def resumen_semanal(df):
    """Cantidad de tickets agrupados por semana."""
    df_temp = df.copy()
    df_temp["semana"] = df_temp["fecha"].dt.isocalendar().week
    resumen = df_temp.groupby("semana").agg(
        cantidad_tickets=("id_ticket", "count")
    ).reset_index()
    return resumen


def generar_reporte_excel(df, ruta_salida):
    """Genera un archivo Excel con varias hojas de resumen."""
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

    with pd.ExcelWriter(ruta_salida, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Datos completos", index=False)
        resumen_por_categoria(df).to_excel(writer, sheet_name="Por categoria", index=False)
        resumen_por_prioridad(df).to_excel(writer, sheet_name="Por prioridad", index=False)
        resumen_por_tecnico(df).to_excel(writer, sheet_name="Por tecnico", index=False)
        resumen_semanal(df).to_excel(writer, sheet_name="Por semana", index=False)

    print(f"Reporte generado correctamente en: {ruta_salida}")


def mostrar_resumen_consola(df):
    """Imprime un resumen rápido en la terminal."""
    print("=" * 50)
    print("RESUMEN DE TICKETS DE SOPORTE TI")
    print("=" * 50)
    print(f"Total de tickets: {len(df)}")
    print(f"Rango de fechas: {df['fecha'].min().date()} a {df['fecha'].max().date()}")
    print("\n--- Tickets por categoría ---")
    print(resumen_por_categoria(df).to_string(index=False))
    print("\n--- Tickets por prioridad ---")
    print(resumen_por_prioridad(df).to_string(index=False))
    print("\n--- Tickets por técnico ---")
    print(resumen_por_tecnico(df).to_string(index=False))
    print("=" * 50)


def main():
    df = cargar_datos(RUTA_ENTRADA)
    mostrar_resumen_consola(df)
    generar_reporte_excel(df, RUTA_SALIDA)


if __name__ == "__main__":
    main()
