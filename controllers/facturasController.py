from models import getFacturasModel
def facturasController():
    facturas = getFacturasModel.getFacturas()
    data = []
    
    return data