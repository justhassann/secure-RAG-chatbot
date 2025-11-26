import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import HexColor

def convert_txt_to_pdf(txt_path, pdf_path):
    """Convert a text file to a formatted PDF"""
    
    # Read the text file
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create PDF
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=HexColor('#1e40af'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Custom heading style
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=HexColor('#1e40af'),
        spaceAfter=12,
        spaceBefore=16,
        fontName='Helvetica-Bold'
    )
    
    # Custom body style
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        leading=16,
        spaceAfter=12,
        alignment=TA_LEFT,
        fontName='Helvetica'
    )
    
    # Build the document
    story = []
    
    # Split content into lines
    lines = content.split('\n')
    
    first_line = True
    for line in lines:
        line = line.strip()
        
        if not line:
            # Empty line - add small spacer
            story.append(Spacer(1, 0.1*inch))
            continue
        
        # First non-empty line is the title
        if first_line and line:
            story.append(Paragraph(line, title_style))
            story.append(Spacer(1, 0.2*inch))
            first_line = False
        # Lines that look like headings (short, no punctuation at end)
        elif len(line) < 80 and not line.endswith('.') and not line.endswith(','):
            story.append(Paragraph(line, heading_style))
        # Regular body text
        else:
            story.append(Paragraph(line, body_style))
    
    # Build PDF
    doc.build(story)

def convert_all_txt_to_pdf():
    """Convert all txt files in knowledge_base to PDFs"""
    base_dir = "knowledge_base"
    
    if not os.path.exists(base_dir):
        print(f"Error: {base_dir} directory not found!")
        return
    
    # Track conversions
    converted = 0
    
    # Walk through all subdirectories
    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            if filename.endswith('.txt'):
                txt_path = os.path.join(root, filename)
                pdf_path = txt_path.replace('.txt', '.pdf')
                
                try:
                    convert_txt_to_pdf(txt_path, pdf_path)
                    print(f"✓ Converted: {os.path.relpath(txt_path, base_dir)} -> {os.path.basename(pdf_path)}")
                    converted += 1
                except Exception as e:
                    print(f"✗ Failed to convert {txt_path}: {e}")
    
    print(f"\n✅ Successfully converted {converted} documents to PDF!")
    print("PDF files created alongside text files in knowledge_base/")

if __name__ == "__main__":
    convert_all_txt_to_pdf()
