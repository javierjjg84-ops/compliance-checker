from fpdf import FPDF
import datetime

def generate_pdf(score, findings):
    pdf = FPDF()
    pdf.add_page()
    
    # Título
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Informe de Compliance Automatizado", ln=True, align='C')
    
    # Scoring con color (si es bajo, resalta)
    pdf.set_font("Arial", 'B', 12)
    pdf.ln(5)
    pdf.cell(0, 10, f"Puntuacion de Seguridad: {score}/100", ln=True)
    pdf.cell(0, 10, f"Fecha: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)
    pdf.ln(10)

    # Tabla de hallazgos
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(110, 8, "Hallazgo", 1)
    pdf.cell(30, 8, "ISO 27001", 1)
    pdf.cell(30, 8, "ENS", 1)
    pdf.cell(20, 8, "Svr", 1, ln=True)

    pdf.set_font("Arial", size=8)
    for f in findings:
        # Truncar descripción para que no rompa la tabla
        desc = (f['description'][:60] + '..') if len(f['description']) > 60 else f['description']
        
        pdf.cell(110, 8, desc, 1)
        pdf.cell(30, 8, str(f.get('iso', 'N/A')), 1)
        pdf.cell(30, 8, str(f.get('ens', 'N/A')), 1)
        pdf.cell(20, 8, f.get('severity', 'low').upper(), 1, ln=True)

    pdf.output("output/report.pdf")
