from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
#I"ll be generating code39 barcodes, others are available
from reportlab.graphics.barcode import code39
import os

# generate a canvas (A4 in this case, size doesn"t really matter)
pagesize = (50*mm, 25*mm)
c=canvas.Canvas("barcode_example1.pdf",pagesize=pagesize)
# create a barcode object
# (is not displayed yet)
# The encode text is "123456789"
# barHeight encodes how high the bars will be
# barWidth encodes how wide the "narrowest" barcode unit is
Manufacture = "OPTILAB"
barcodetext = "B6P755464454"
pn = "IML-1550-PM-V"
barcode=code39.Extended39(barcodetext,barWidth=0.15*mm,barHeight=5*mm)
# drawOn puts the barcode on the canvas at the specified coordinates

text = c.beginText(1*mm, 20*mm)
text.setFont("Courier", 9)
text.textLine("MANUFACTURE : {m}".format(m= Manufacture))
c.drawText(text)

text0 = c.beginText(1*mm, 15*mm)
text0.setFont("Courier", 9)
text0.textLine("PN : {pn}".format(pn= pn))
c.drawText(text0)

barcode.drawOn(c,1*mm,8*mm)

text1 = c.beginText(13*mm, 5*mm)
text1.setFont("Courier", 9)
text1.textLine(barcodetext)
c.drawText(text1)






# now create the actual PDF
c.showPage()
c.save()
os.startfile("barcode_example1.pdf", "print")
