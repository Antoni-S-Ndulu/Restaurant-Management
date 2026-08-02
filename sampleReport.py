from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
import datetime
import pymysql as p


def get_current_date():
    # Get the current date
    now = datetime.datetime.now()
    # Format the date as "DD/MM/YYYY"
    formatted_date = now.strftime("%d_%m_%Y")
    return formatted_date

def create_transaction_report(filename,token,quantity, foodname, 
                              price, total_price, balance_remaining,
                                customer_name, date = get_current_date()):
    c = canvas.Canvas(filename)
   
    
    # 1. Prepare the content
    content = [
        "BLESSED HO RESTAURANT",
        "TRANSACTION REPORT",
        "DATE: 02/08/2026",
        f"FOOD BOUGHT: {foodname}",
        f"QUANTITY: {quantity}",
        f"PRICE: {price}",
        f"TOTAL PRICE: {total_price}",
        f"BALANCE REMAINING: {balance_remaining}"
    ]
    
    # 2. Draw the text lines
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, content[0]) # Header
    
    c.setFont("Helvetica", 12)
    y_position = 720
    for line in content[1:]:
        c.drawString(100, y_position, line)
        y_position -= 20 # Move down for the next line
        
    # 3. Add the QR Code
    #getting content (authentication token) from database

    qr_code = qr.QrCodeWidget(token)#secret token from qrcodeModule.py
    d = Drawing(100, 100)
    d.add(qr_code)
    # Draw the QR code on the canvas
    from reportlab.graphics import renderPDF
    renderPDF.draw(d, c, 100, y_position - 120)
    
    # 4. Add the final message[cite: 1]
    c.drawString(100, y_position - 140, f"Welcome again: {customer_name.title()}")
    
    c.save()

