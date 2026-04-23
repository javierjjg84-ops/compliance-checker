# Compliance-Checker
Construír un pipeline de compliance que integra Lynis y visor de eventos, parsea y normaliza los resultados, los mapea a controles de ISO 27001 y ENS, y genera scoring automatizado con reportes en PDF.

# Objetivo real:
Construir una herramienta que:

Escanea sistemas:

Linux → Lynis

Windows → Visor de Eventos

Hace parsing de resultados

Mapea hallazgos a controles:
ISO 27001
ENS

Calcula un score de seguridad

Genera reporte profesional (JSON + PDF)

# Flujo completo:
ESCANEO → PARSING → NORMALIZACIÓN → MAPEO → SCORING → REPORT

# Estructura:

```
comprobador-de-cumplimiento/
├── main.py
├── escáner/
│   ├── lynis.py
│   └── visor.py
├── analizador/
│   ├── lynis_parser.py
│   └── visor_parser.py
├── núcleo/
│   ├── normalizador.py
│   ├── mapeador.py
│   └── evaluador.py
├── informe/
│   ├── informe_json.py
│   └── informe_pdf.py
├── datos/
│   └── controls.json
└── salida/
```

# Raíz:
main.py: Es el punto de entrada que coordina todo el proceso: llama a los escáneres, procesa los datos y genera los informes.

# scanner/ (Recolección)
lynis.py: Ejecuta la herramienta Lynis para auditar la seguridad en sistemas Linux.

visor.py: Ejecuta comandos de PowerShell para extraer configuraciones de seguridad en Windows.

# parser/ (Traducción)
lynis_parser.py: Convierte la salida cruda de Lynis en una estructura de datos procesable por Python.

visor_parser.py: Convierte la salida (JSON/texto) de PowerShell en una estructura de datos procesable.

# core/ (Lógica)
normalizer.py: Estandariza los datos provenientes de distintos escáneres (Linux/Windows) a un formato único.

mapper.py: Asocia los hallazgos técnicos con marcos de control de seguridad (como NIST, ISO o CIS).

scorer.py: Calcula una nota o puntuación de cumplimiento basada en los controles mapeados.

# report/ (Presentación)
json_report.py: Genera un archivo con los resultados completos en formato JSON.

pdf_report.py: Crea un documento profesional y legible con los resultados de la auditoría en PDF.

# data/ (Configuración)
controls.json: Contiene la base de datos de los controles de seguridad y los criterios para evaluar el cumplimiento.

# output/
Directorio: Carpeta donde se almacenan automáticamente los logs, los resultados crudos y los informes generados.

# Requisitos:
La librería fpdf es el componente esencial instalado para que tu programa pueda generar y exportar los informes finales de auditoría en formato PDF.

En linux:
```
pip3 install fpdf --break-system-packages
```

En windows:
```
pip3 install fpdf
```
# Herraminetas necesarias:
Lynis: Es una herramienta externa de auditoría de seguridad para Linux que requiere instalación manual para analizar vulnerabilidades y configuraciones del sistema.
```
sudo apt update
sudo apt install lynis -y
```

Visor de Eventos: Es una utilidad nativa preinstalada en Windows que registra y gestiona todos los eventos de seguridad, aplicaciones y sistema del equipo.






