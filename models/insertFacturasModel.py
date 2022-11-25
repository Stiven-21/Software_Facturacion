from config.database import db
cursor = db.cursor()

def CrearFactura(id_cliente, referencia, descripcion, cantidad, precio_unitario, descuento, impuesto):
    id_estado = 2
    try:
        cursor.execute("INSERT INTO facturas(referencia, id_user, descripcion, cantidad, precio, descuento, impuesto, id_estado) values(%s,%s,%s,%s,%s,%s,%s,%s)", (
            referencia, 
            id_cliente, 
            descripcion,
            cantidad, 
            precio_unitario,
            descuento,
            impuesto,
            id_estado
        ))
        db.commit()
    except:
        print("Ha ocurrido un error en el model CrearFactura")