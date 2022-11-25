from datetime import datetime,date
from models import getFacturasModel
def facturasController():
    facturas = getFacturasModel.getFacturas()
    print("-----------------------")
    print(facturas)
    data = []
    for fila in facturas:
        fecha = fila[3].strftime('%m/%d/%Y %I:%M:%S%p')
        data.append({
            'referencia': fila[1],
            'fecha': fecha,
            'estado': fila[11],
            'user_id': fila[13],
            'user': fila[14]+' '+ fila[15],
        })
       
    return data