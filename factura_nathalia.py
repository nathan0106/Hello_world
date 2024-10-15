from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import locale

# Configurar el locale para pesos colombianos
locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')

# ... código existente ...

def generar_factura(nombre_archivo, productos):
    doc = SimpleDocTemplate(nombre_archivo, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Crear título
    titulo = Paragraph("Factura de la Tienda de Nathalia", styles['Title'])
    
    # Preparar datos de la tabla
    datos = [['Producto', 'Cantidad', 'Precio Unitario', 'Total']]
    total_factura = 0
    nombre_cliente = productos[0][0]
    
    for producto in productos:
        _, nombre, cantidad, precio = producto
        total = cantidad * precio
        total_factura += total
        datos.append([
            nombre,
            str(cantidad),
            locale.currency(precio, symbol=True, grouping=True),
            locale.currency(total, symbol=True, grouping=True)
        ])
    
    # Agregar fila de total
    datos.append(['', '', 'Total:', locale.currency(total_factura, symbol=True, grouping=True)])
    
    # Crear tabla
    tabla = Table(datos, colWidths=[2.5*inch, 1*inch, 1.5*inch, 1.5*inch])
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (-1, 1), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    # Crear información del cliente
    info_cliente = Paragraph(f"<b>Cliente:</b> {nombre_cliente}", styles['Normal'])
    
    # Construir el documento
    elementos = [titulo, Spacer(1, 0.25*inch), info_cliente, Spacer(1, 0.25*inch), tabla]
    doc.build(elementos)

def ingresar_productos():
    productos = []
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    while True:
        nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break

        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio unitario: "))
        productos.append((nombre_cliente, nombre, cantidad, precio))
    return productos

if __name__ == "__main__":
    print("Bienvenido al generador de facturas de la Tienda de Nathalia")
    productos = ingresar_productos()
    generar_factura("factura_nathalia.pdf", productos)
    print("Factura generada con éxito en 'factura_nathalia.pdf'.")