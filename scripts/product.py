class Product:
    def __init__(self, barcode):
        self.barcode = barcode

    def is_valid(self):
        barcode = self.barcode
        if len(barcode) < 10:
            return False
        else:
            return True