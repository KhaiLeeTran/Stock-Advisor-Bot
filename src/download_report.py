from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
import io

def create_pdf(text):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    width, height = A4

    elements = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#000000')
    )
    title = Paragraph("Stock Market Report", title_style)
    elements.append(title)
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['BodyText'],
        fontSize=12,
        leading=18
    )
    
    paragraphs = text.split('\n\n')
    for paragraph in paragraphs:
        elements.append(Paragraph(paragraph, body_style))
    
    doc.build(elements)
    buffer.seek(0) 
    return buffer