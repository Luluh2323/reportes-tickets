# Automatizador de Reportes de Tickets de Soporte TI

Script en Python que automatiza la generación de reportes de tickets de soporte técnico, transformando un registro plano (CSV) en un reporte Excel con estadísticas listas para análisis.

## Motivación

En mi trabajo actual como Operador de Soporte Técnico en Informática (Municipalidad Provincial de Casma - OTIC), doy soporte a un sistema interno de gestión de tickets. Muchos de los reportes de seguimiento (tickets por categoría, por técnico, tiempos de resolución) se hacen de forma manual.

Este proyecto es una versión personal, con **datos simulados**, que busca demostrar cómo se podría automatizar ese proceso usando Python y pandas — reduciendo un trabajo que normalmente toma tiempo manual a un solo comando.

## ¿Qué hace?

A partir de un CSV con el registro de tickets, el script genera automáticamente un archivo Excel con 5 hojas:

1. **Datos completos** — el registro original
2. **Por categoría** — cantidad de tickets y tiempo promedio de resolución (Hardware, Software, Red)
3. **Por prioridad** — cantidad y tiempo promedio según prioridad (Alta, Media, Baja)
4. **Por técnico** — tickets resueltos y horas totales invertidas por cada técnico
5. **Por semana** — cantidad de tickets agrupados por semana del año

Además, imprime un resumen rápido directamente en la terminal.

## Tecnologías

- Python 3
- pandas
- openpyxl

## Instalación

```bash
git clone https://github.com/TU-USUARIO/reportes-tickets.git
cd reportes-tickets
pip install -r requirements.txt
```

## Uso

```bash
python generar_reporte.py
```

Esto genera el archivo `reportes/reporte_tickets.xlsx` y muestra un resumen en consola.

## Estructura del proyecto

```
reportes-tickets/
├── data/
│   └── tickets.csv          # Datos de entrada (simulados)
├── reportes/
│   └── reporte_tickets.xlsx # Reporte generado (output)
├── generar_reporte.py        # Script principal
├── requirements.txt
└── README.md
```

## Ejemplo de salida en consola

```
==================================================
RESUMEN DE TICKETS DE SOPORTE TI
==================================================
Total de tickets: 30
Rango de fechas: 2026-06-01 a 2026-06-15

--- Tickets por categoría ---
categoria  cantidad_tickets  tiempo_promedio_horas
 Hardware                10                   1.95
      Red                 9                   1.89
 Software                11                   2.50
==================================================
```

## Nota sobre los datos

Los datos en `data/tickets.csv` son **simulados/inventados** para fines de demostración. No corresponden a información real de ninguna institución.

## Autor

**Lucio Llanos Sevillano**
Técnico en Diseño y Desarrollo de Software
[LinkedIn](#) · [GitHub](#)
