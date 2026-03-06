#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert GUIA_IAFX_PRIME_V8.html to PDF
Uses built-in fpdf library - no external dependencies
"""

import os
import sys

# Try to use reportlab, fall back to pdfkit or manual PDF creation
try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
    
    print("✓ reportlab encontrado, gerando PDF...")
    
    # Criar documento
    pdf_path = "GUIA_IAFX_PRIME_V8.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4, topMargin=0.5*inch, bottomMargin=0.5*inch)
    
    # Estilos
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=10,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=10,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
        leading=14
    )
    
    # Conteúdo
    content = []
    
    # Título
    content.append(Paragraph("📊 IAFX Prime v8", title_style))
    content.append(Paragraph("Guia Completo do Usuário", styles['Normal']))
    content.append(Spacer(1, 0.3*inch))
    
    # Seção 1
    content.append(Paragraph("🎯 O Que é o IAFX Prime v8?", heading_style))
    content.append(Paragraph(
        "O <b>IAFX Prime v8</b> é a versão 2.0 do Expert Advisor inteligente para MetaTrader 5. "
        "Mantém toda a robustez da v7 e <b>adiciona uma nova estratégia de negociação: FIMATHE</b> "
        "(estratégia de canais e rompimentos).",
        body_style
    ))
    content.append(Paragraph(
        "Agora você tem <b>2 estratégias independentes</b> para gerar o primeiro sinal:",
        body_style
    ))
    content.append(Spacer(1, 0.2*inch))
    
    # Seção 2
    content.append(Paragraph("🚀 Estratégia FIMATHE (Novo!)", heading_style))
    content.append(Paragraph(
        "Sistema de identificação de canais de consolidação que opera com base em rompimentos de preço.",
        body_style
    ))
    
    content.append(Spacer(1, 0.1*inch))
    content.append(Paragraph("<b>Como funciona:</b>", styles['Normal']))
    
    content.append(Paragraph(
        "1. Mede o <b>topo</b> (highest high) dos últimas N barras<br/>"
        "2. Mede o <b>fundo</b> (lowest low) dos últimas N barras<br/>"
        "3. Calcula <b>zona neutra</b> = 50% do canal<br/>"
        "4. Calcula <b>zona de rompimento</b> = % configurável do canal<br/>"
        "5. Gera sinal:<br/>"
        "&nbsp;&nbsp;• <b>\"C\" (Compra)</b>: quando preço rompe ABAIXO<br/>"
        "&nbsp;&nbsp;• <b>\"V\" (Venda)</b>: quando preço rompe ACIMA<br/>"
        "&nbsp;&nbsp;• <b>\"X\" (Neutro)</b>: fora das zonas",
        body_style
    ))
    
    content.append(Spacer(1, 0.2*inch))
    content.append(Paragraph("⚙️ Parâmetros FIMATHE", heading_style))
    
    content.append(Paragraph(
        "<b>fimathe_barras</b> (Padrão: 50)<br/>"
        "Número de barras para calcular o canal.<br/>"
        "• 30-50 para M5/M15 (mais sensível)<br/>"
        "• 50-100 para M30/H1 (balanceado)<br/>"
        "• 100+ para H4/D1 (confiável)",
        body_style
    ))
    
    content.append(Spacer(1, 0.1*inch))
    content.append(Paragraph(
        "<b>fimathe_percentual_ruptura</b> (Padrão: 0.5)<br/>"
        "Percentual da zona de rompimento.<br/>"
        "• 0.3 = Mais aberta → Mais sinais<br/>"
        "• 0.5 = Balanceado (recomendado)<br/>"
        "• 0.7 = Mais restritiva → Menos sinais",
        body_style
    ))
    
    content.append(Spacer(1, 0.2*inch))
    content.append(Paragraph("🔄 Lógica de Entrada Dual", heading_style))
    
    content.append(Paragraph(
        "Quando ambas as estratégias estão habilitadas, o primeiro sinal a aparecer abre a ordem:",
        body_style
    ))
    
    content.append(Paragraph(
        "1. Avalia <b>IAFX primeiro</b> (confluência de indicadores)<br/>"
        "2. Se IAFX não sinalar → avalia <b>FIMATHE</b> (canais)<br/>"
        "3. <b>Primeira a sinalizar abre a ordem</b><br/>"
        "4. Depois, grid, trailing stop e breakeven funcionam igual à v7",
        body_style
    ))
    
    content.append(Spacer(1, 0.3*inch))
    content.append(Paragraph("📋 Configurações Possíveis", heading_style))
    
    # Tabela
    data = [
        ['Config', 'Comportamento'],
        ['usar_IAFX=true, usar_FIMATHE=false', 'Apenas IAFX (como v7)'],
        ['usar_IAFX=false, usar_FIMATHE=true', 'Apenas FIMATHE (novo)'],
        ['usar_IAFX=true, usar_FIMATHE=true', 'Dual: IAFX → FIMATHE']
    ]
    
    t = Table(data, colWidths=[2.5*inch, 3.5*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')])
    ]))
    content.append(t)
    
    content.append(Spacer(1, 0.3*inch))
    
    # Página 2
    content.append(PageBreak())
    
    content.append(Paragraph("⚡ Sistema de Defesa (Idêntico à v7)", heading_style))
    content.append(Paragraph(
        "Todos os mecanismos de proteção funcionam igual à v7:",
        body_style
    ))
    
    content.append(Spacer(1, 0.1*inch))
    content.append(Paragraph("<b>🟡 Alerta A - Grid Adaptativo</b>", styles['Normal']))
    content.append(Paragraph(
        "Ativado por: DD% ≥ 10% OU VIX ≥ 21.0<br/>"
        "Ação: Grid aumenta 1.5x",
        body_style
    ))
    
    content.append(Spacer(1, 0.1*inch))
    content.append(Paragraph("<b>🟠 Alerta B - Mudança de Timeframe</b>", styles['Normal']))
    content.append(Paragraph(
        "Ativado por: DD% ≥ 20% OU VIX ≥ 24.0<br/>"
        "Ação: Todos os indicadores mudam para M15",
        body_style
    ))
    
    content.append(Spacer(1, 0.1*inch))
    content.append(Paragraph("<b>🔴 Alerta C - Modo Emergência</b>", styles['Normal']))
    content.append(Paragraph(
        "Ativado por: DD% ≥ 30%<br/>"
        "Ação: Reduz lote pela metade",
        body_style
    ))
    
    content.append(Spacer(1, 0.3*inch))
    content.append(Paragraph("🚀 Primeiros Passos com v8", heading_style))
    
    content.append(Paragraph("<b>1. Teste Inicial (Demo)</b>", styles['Normal']))
    content.append(Paragraph(
        "usar_IAFX = true<br/>"
        "usar_FIMATHE = true<br/>"
        "fimathe_barras = 50<br/>"
        "fimathe_percentual_ruptura = 0.5<br/>"
        "Grid Médio: 150 pontos<br/>"
        "Grid Super: 75 pontos<br/>"
        "Lote base: 0.01<br/>"
        "Meta diária: 1%",
        body_style
    ))
    
    content.append(Spacer(1, 0.2*inch))
    content.append(Paragraph("<b>2. Migração da v7</b>", styles['Normal']))
    content.append(Paragraph(
        "1. Baixe IAFX Prime v8.ex5<br/>"
        "2. Copie para pasta de Experts do MT5<br/>"
        "3. Configure: usar_IAFX=true, usar_FIMATHE=false<br/>"
        "4. Teste em demo 1-2 semanas<br/>"
        "5. Depois ative FIMATHE se desejar",
        body_style
    ))
    
    content.append(Spacer(1, 0.3*inch))
    content.append(Paragraph("⚠️ Avisos Importantes", heading_style))
    
    content.append(Paragraph(
        "🔴 <b>Risco Alto:</b> Trading com EA envolve risco elevado. Você pode perder mais que investiu. "
        "Sempre teste em DEMO primeiro. Use apenas 40-60% do capital em risco.<br/><br/>"
        "🟡 <b>Recomendações:</b> Monitore o robô nas primeiras semanas. Acompanhe DD% diariamente. "
        "Respeite os Alertas A/B/C. Revise configurações semanalmente.<br/><br/>"
        "🟢 <b>Melhores Práticas:</b> Comece com FIMATHE desativado. Aumente risco gradualmente. "
        "Use meta diária para ganhos consistentes. Registre resultados por semana.",
        body_style
    ))
    
    content.append(Spacer(1, 0.3*inch))
    
    # Footer
    content.append(Spacer(1, 0.2*inch))
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.grey,
        alignment=TA_CENTER
    )
    content.append(Paragraph("Documento criado para IAFX Prime v8 - Versão 1.0 - Março 2026", footer_style))
    content.append(Paragraph("Para mais detalhes, consulte GUIA_IAFX_PRIME_V8.md", footer_style))
    
    # Gerar PDF
    doc.build(content)
    print(f"✅ PDF criado com sucesso: {pdf_path}")
    sys.exit(0)

except ImportError:
    print("❌ reportlab não encontrado")
    print("Tentando alternativa...")
    
    # Fallback: usar HTML2PDF ou markdown2pdf
    try:
        from markdown2pdf import convert
        convert("GUIA_IAFX_PRIME_V8.md", "GUIA_IAFX_PRIME_V8.pdf")
        print("✅ PDF criado com markdown2pdf")
        sys.exit(0)
    except ImportError:
        print("❌ Nenhuma biblioteca de PDF encontrada")
        print("\nInstalando reportlab...")
        os.system("pip install reportlab -q")
        print("Tente novamente: python gerar_pdf_v8.py")
        sys.exit(1)
