$(document).ready(function(){
    $('#regis_factura').submit(function(event){
        event.preventDefault();
        id_cliente = document.getElementById("id_cliente")
        console.log(id_cliente.value)

        producto = document.getElementById('producto')
        cantidad = document.getElementById('cantidad')
        precio = document.getElementById('precio')
        descuento = document.getElementById('descuento')
        total_producto = parseInt(precio.value) + ((parseInt(precio.value)*19)/100) - ((parseInt(precio.value)*descuento.value)/100)
        console.log(total_producto)

        if(id_cliente.value != ''){
            if(producto.value == ''){
                alert("Debe especificar el nombre del producto")
            }else if(cantidad.value == ''){
                alert("Debe especificar la cantidad de productos")
            }else if(precio.value == ''){
                alert("Debe especificar el precio del producto")
            }else if(precio.value == ''){
                alert("Debe especificar el descuento del producto")
            }

            //ENVIAR PRODUCTOS
            $.ajax({
                url: '/guardar-factura',
                data: $('form').serialize(),
                type: 'POST',
                success: function(response){
                    producto.value = ''
                    cantidad.value = ''
                    precio.value = ''
                    descuento.value = ''
                }
            })

        }else{
            alert("Ingrese el cliente dueño de la factura")
        }

        

    })
})