def Printing(self):

    printer = QPrinter()
    dlg = QPrintDialog(printer, self)
    if dlg.exec() == QDialog.Accepted:
        #create Printer
        qp = QPainter()
        qp.begin(printer)

        #Margin setting
        wgap = printer.pageRect().width()*0.1
        hgap = printer.pageRect().height()*0.1

        # Widget setting
        xscale = (printer.pageRect().width()-wgap)/self.table.width()
        yscale = (printer.pageRect().height()-hgap)/self.table.height()
        scale = xscale if xscale < yscale else yscale
        qp.translate(printer.paperRect().x() + printer.pageRect().width()/2, printer.paperRect().y() + printer.pageRect().height()/2)
        qp.scale(scale, scale);
        qp.translate(-self.table.width()/2, -self.table.height()/2);

        # Print
        self.table.render(qp)

        qp.end()
