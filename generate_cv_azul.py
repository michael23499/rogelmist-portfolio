# -*- coding: utf-8 -*-
"""
Script para generar CV en PDF - Diseño Azul Claro - VERSIÓN FINAL
Rogelmist Ferreira - Digital Marketing Strategist
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Paleta de colores azules
AZUL_OSCURO = HexColor("#1A365D")
AZUL_MEDIO = HexColor("#2C5282")
AZUL_CLARO = HexColor("#4299E1")
AZUL_MUY_CLARO = HexColor("#EBF8FF")
AZUL_SUAVE = HexColor("#BEE3F8")
TEXTO = HexColor("#2D3748")
GRIS = HexColor("#718096")
BLANCO = HexColor("#FFFFFF")

def create_cv():
    filename = "Rogelmist_Ferreira_CV_2025_FINAL.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    foto_path = "foto_perfil_personal.jpg"

    # ============= FONDO HEADER =============
    c.setFillColor(AZUL_MUY_CLARO)
    c.rect(0, height - 82*mm, width, 82*mm, fill=1, stroke=0)

    c.setFillColor(AZUL_CLARO)
    c.rect(0, height - 82*mm, width, 3*mm, fill=1, stroke=0)

    # ============= FOTO =============
    if os.path.exists(foto_path):
        c.saveState()
        c.setFillColor(BLANCO)
        c.circle(36*mm, height - 39*mm, 26*mm, fill=1, stroke=0)
        c.setStrokeColor(AZUL_CLARO)
        c.setLineWidth(3)
        c.circle(36*mm, height - 39*mm, 26*mm, fill=0, stroke=1)
        path = c.beginPath()
        path.circle(36*mm, height - 39*mm, 24*mm)
        c.clipPath(path, stroke=0)
        c.drawImage(foto_path, 12*mm, height - 63*mm, width=48*mm, height=48*mm, preserveAspectRatio=True, mask='auto')
        c.restoreState()

    # ============= NOMBRE Y TÍTULO =============
    x_info = 72*mm

    c.setFillColor(AZUL_OSCURO)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(x_info, height - 22*mm, "ROGELMIST FERREIRA")

    c.setFillColor(AZUL_CLARO)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x_info, height - 33*mm, "DIGITAL MARKETING STRATEGIST")

    c.setFillColor(GRIS)
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(x_info, height - 42*mm, "Content Creator | Social Media Expert | Brand Builder")

    c.setFillColor(AZUL_CLARO)
    c.rect(x_info, height - 47*mm, 75*mm, 1*mm, fill=1, stroke=0)

    c.setFillColor(AZUL_OSCURO)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(x_info, height - 55*mm, "Madrid, Spain  |  rogelmist@gmail.com")

    # LinkedIn con enlace clickeable
    c.setFillColor(AZUL_MEDIO)
    c.setFont("Helvetica", 8)
    linkedin_text = "linkedin.com/in/rogelmist-ferreira"
    linkedin_url = "https://www.linkedin.com/in/rogelmist-ferreira-95a570271/"
    c.drawString(x_info, height - 63*mm, linkedin_text)
    # Crear enlace clickeable
    link_width = c.stringWidth(linkedin_text, "Helvetica", 8)
    c.linkURL(linkedin_url, (x_info, height - 65*mm, x_info + link_width, height - 61*mm))

    # Web personal con enlace clickeable
    c.setFillColor(AZUL_CLARO)
    c.setFont("Helvetica-Bold", 8)
    web_text = "rogelmist-portfolio.vercel.app"
    web_url = "https://rogelmist-portfolio.vercel.app/"
    c.drawString(x_info, height - 70*mm, web_text)
    web_width = c.stringWidth(web_text, "Helvetica-Bold", 8)
    c.linkURL(web_url, (x_info, height - 72*mm, x_info + web_width, height - 68*mm))

    # ============= COLUMNAS =============
    col_izq = 10*mm
    col_der = 108*mm
    col_der_width = 90*mm

    y = height - 90*mm

    # ============= COLUMNA IZQUIERDA =============

    # --- PERFIL ---
    c.setFillColor(AZUL_OSCURO)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(col_izq, y, "PERFIL PROFESIONAL")
    c.setFillColor(AZUL_SUAVE)
    c.rect(col_izq, y - 2*mm, 38*mm, 1.5*mm, fill=1, stroke=0)

    y -= 10*mm
    c.setFillColor(TEXTO)
    c.setFont("Helvetica", 8)
    perfil = [
        "Publicista con +4 años de trayectoria internacional",
        "en marketing digital y gestión de contenidos.",
        "Experta en estrategias de RRSS con +50% engagement.",
        "Creatividad visual + análisis de datos."
    ]
    for line in perfil:
        c.drawString(col_izq, y, line)
        y -= 4*mm

    # --- EXPERIENCIA ---
    y -= 5*mm
    c.setFillColor(AZUL_OSCURO)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(col_izq, y, "EXPERIENCIA PROFESIONAL")
    c.setFillColor(AZUL_SUAVE)
    c.rect(col_izq, y - 2*mm, 45*mm, 1.5*mm, fill=1, stroke=0)

    experiencias = [
        {
            "empresa": "INSPIRA AGENCY MARKETING SL",
            "cargo": "Estratega de Contenido & Mkt Digital",
            "info": "Madrid | Dic 2024 - Abr 2025",
            "logros": [
                "Diseñar estrategias para +5 cuentas",
                "Planificar calendarios con +40% engagement",
                "Crear reels, carruseles y stories virales",
                "Gestionar comunidades con storytelling"
            ]
        },
        {
            "empresa": "LA MUNDIAL DE SEGUROS",
            "cargo": "Analista de Marketing Digital",
            "info": "Caracas | Ago 2023 - Nov 2024",
            "logros": [
                "Liderar transformación digital (+50% RRSS)",
                "Diseñar +150 piezas gráficas corporativas",
                "Coordinar campañas con influencers",
                "Ejecutar eventos y activaciones de marca"
            ]
        },
        {
            "empresa": "IMPULSO DIGITAL",
            "cargo": "Social Media Manager",
            "info": "Caracas | Abr 2022 - May 2023",
            "logros": [
                "Gestionar +6 cuentas con contenido adaptado",
                "Redactar copys con alta conversión",
                "Analizar y optimizar métricas en tiempo real"
            ]
        },
        {
            "empresa": "LION TECH",
            "cargo": "Community Manager & Copywriter",
            "info": "Caracas | Jul 2021 - Mar 2022",
            "logros": [
                "Desarrollar contenido creativo multiformato",
                "Gestionar crisis de reputación digital",
                "Crear copy para redes, blogs y ads"
            ]
        },
        {
            "empresa": "TRIANGLE SOLUTIONS ETT",
            "cargo": "Auxiliar de Catering - Aerolíneas",
            "info": "Madrid | Abr 2025 - Ene 2026",
            "logros": [
                "Coordinar logística de alta exigencia",
                "Demostrar trabajo bajo presión extrema"
            ]
        },
    ]

    y -= 8*mm
    for exp in experiencias:
        c.setFillColor(AZUL_MEDIO)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(col_izq, y, exp["empresa"])

        y -= 4*mm
        c.setFillColor(AZUL_CLARO)
        c.setFont("Helvetica-Oblique", 7)
        c.drawString(col_izq, y, exp["cargo"])
        c.setFillColor(GRIS)
        c.setFont("Helvetica", 7)
        c.drawString(col_izq + 52*mm, y, exp["info"])

        y -= 4*mm
        c.setFillColor(TEXTO)
        c.setFont("Helvetica", 7)
        for logro in exp["logros"]:
            c.setFillColor(AZUL_CLARO)
            c.drawString(col_izq + 1*mm, y, "●")
            c.setFillColor(TEXTO)
            c.drawString(col_izq + 4*mm, y, logro)
            y -= 3.5*mm

        y -= 2*mm

    # ============= COLUMNA DERECHA =============
    y_r = height - 90*mm

    # --- COMPETENCIAS DIGITALES ---
    c.setFillColor(AZUL_OSCURO)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(col_der, y_r, "COMPETENCIAS DIGITALES")
    c.setFillColor(AZUL_SUAVE)
    c.rect(col_der, y_r - 2*mm, 42*mm, 1.5*mm, fill=1, stroke=0)

    y_r -= 10*mm
    herramientas = [
        ("Canva Pro", 95), ("Adobe Photoshop", 88),
        ("Adobe Illustrator", 82), ("Meta Business Suite", 95),
        ("Google Analytics", 88), ("Microsoft Office", 92),
        ("CapCut / Premiere", 78)
    ]

    for tool, level in herramientas:
        c.setFillColor(TEXTO)
        c.setFont("Helvetica", 7)
        c.drawString(col_der, y_r, tool)
        bar_x = col_der + 32*mm
        bar_w = 53*mm
        c.setFillColor(AZUL_MUY_CLARO)
        c.roundRect(bar_x, y_r - 0.5*mm, bar_w, 3*mm, 1*mm, fill=1, stroke=0)
        c.setFillColor(AZUL_CLARO)
        c.roundRect(bar_x, y_r - 0.5*mm, bar_w * level/100, 3*mm, 1*mm, fill=1, stroke=0)
        y_r -= 6*mm

    # --- HABILIDADES PROFESIONALES ---
    y_r -= 5*mm
    c.setFillColor(AZUL_OSCURO)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(col_der, y_r, "HABILIDADES PROFESIONALES")
    c.setFillColor(AZUL_SUAVE)
    c.rect(col_der, y_r - 2*mm, 48*mm, 1.5*mm, fill=1, stroke=0)

    y_r -= 9*mm
    habilidades = [
        "Estrategia de contenido digital",
        "Copywriting persuasivo y SEO",
        "Gestión de comunidades online",
        "Análisis de métricas y KPIs",
        "Producción audiovisual creativa",
        "Branding y diseño digital",
        "Liderazgo de proyectos",
        "Pensamiento creativo e innovador",
        "Investigación de mercado",
        "Gestión de crisis reputacional"
    ]

    for hab in habilidades:
        c.setFillColor(AZUL_CLARO)
        c.setFont("Helvetica", 7)
        c.drawString(col_der, y_r, "▸")
        c.setFillColor(TEXTO)
        c.drawString(col_der + 4*mm, y_r, hab)
        y_r -= 5*mm

    # --- FORMACIÓN ---
    y_r -= 5*mm
    c.setFillColor(AZUL_OSCURO)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(col_der, y_r, "FORMACIÓN ACADÉMICA")
    c.setFillColor(AZUL_SUAVE)
    c.rect(col_der, y_r - 2*mm, 40*mm, 1.5*mm, fill=1, stroke=0)

    y_r -= 9*mm
    c.setFillColor(AZUL_MEDIO)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(col_der, y_r, "Instituto Universitario de Mercadotecnia")
    y_r -= 4*mm
    c.setFillColor(TEXTO)
    c.setFont("Helvetica", 7)
    c.drawString(col_der, y_r, "Publicista | 2023 - 2025 | Caracas, Venezuela")

    # --- IDIOMAS ---
    y_r -= 8*mm
    c.setFillColor(AZUL_OSCURO)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(col_der, y_r, "IDIOMAS")
    c.setFillColor(AZUL_SUAVE)
    c.rect(col_der, y_r - 2*mm, 18*mm, 1.5*mm, fill=1, stroke=0)

    y_r -= 8*mm
    c.setFillColor(TEXTO)
    c.setFont("Helvetica", 7)
    c.drawString(col_der, y_r, "Español: Nativo  |  Inglés: A2  |  Portugués: Básico")

    # --- PROPUESTA DE VALOR ---
    y_r -= 9*mm
    box_h = 40*mm
    c.setFillColor(AZUL_MUY_CLARO)
    c.roundRect(col_der - 2*mm, y_r - box_h + 5*mm, col_der_width, box_h, 3*mm, fill=1, stroke=0)
    c.setFillColor(AZUL_CLARO)
    c.rect(col_der - 2*mm, y_r + 3*mm, col_der_width, 2*mm, fill=1, stroke=0)

    c.setFillColor(AZUL_OSCURO)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(col_der, y_r, "LO QUE APORTO A TU EQUIPO")

    y_r -= 7*mm
    propuestas = [
        "Visión estratégica + ejecución creativa",
        "Transformar datos en decisiones de impacto",
        "Experiencia internacional multicultural",
        "Compromiso total con resultados medibles",
        "Adaptabilidad y aprendizaje continuo"
    ]

    for prop in propuestas:
        c.setFillColor(AZUL_CLARO)
        c.setFont("Helvetica", 7)
        c.drawString(col_der, y_r, "●")
        c.setFillColor(TEXTO)
        c.drawString(col_der + 4*mm, y_r, prop)
        y_r -= 5*mm

    # ============= FOOTER =============
    c.setFillColor(AZUL_CLARO)
    c.rect(0, 0, width, 7*mm, fill=1, stroke=0)
    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(width/2, 2.5*mm, '"Transformar ideas en conexiones digitales que generan resultados"')

    c.save()
    print(f"\n{'='*55}")
    print(f"CV PDF generado: {filename}")
    print(f"{'='*55}\n")
    return filename

if __name__ == "__main__":
    create_cv()
