$(document).ready(function(){
    $('#regis_factura').submit(function(event){
        event.preventDefault();

        producto = document.getElementById('producto')
        cantidad = document.getElementById('cantidad')
        precio = document.getElementById('precio')
        descuento = document.getElementById('descuento')
        impuesto = 19

        if(producto.value == ''){
            alert("Debe especificar un producto")
        }

    })
})