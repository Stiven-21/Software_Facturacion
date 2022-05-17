from datetime import datetime,date
from models import getFacturasModel
def facturasController():
    facturas = getFacturasModel.getFacturas()
    data = []
    for fila in facturas:
        fecha = fila[3].strftime('%m/%d/%Y %I:%M:%S%p')
        data.append({
            'id_factura': fila[0],
            'referencia': fila[1],
            'fecha': fecha,
            'cantidad': int(fila[5]),
            'precio': int(fila[6]),
            'observacion': fila[10],
            'estado': fila[12],
            'user_id': fila[14],
            'user': fila[15]+' '+ fila[16],
            'telefono': fila[17],
            'rol': fila[21],
        })
       
    return data