$(document).ready(function(){

    if(localStorage.getItem('referencia') == undefined ){
        aleatorio = Math.floor((Math.random() * (100000000 - 100000 + 1)) + 100000);
        document.getElementById('referencia').value = aleatorio
        localStorage.setItem('referencia', aleatorio)
    }else{
        document.getElementById('referencia').value = localStorage.getItem('referencia')
    }
    

    $('#search_cliente').submit(function(event){
        event.preventDefault();
        buscar = document.getElementById("identificacion_search")
        $.ajax({
            url: '/buscar-usuario',
            data: $('form').serialize(),
            type: 'POST',
            success: function(usuario){
                if(usuario!=null){
                    nombres = usuario[2]+' '+usuario[3]
                    document.getElementById('cliente').value = nombres
                    let date = new Date().toDateString();
                    document.getElementById('fecha_factura').value = date
                    buscar = ''
                }else{
                    document.getElementById('cliente').value = "EL CLIENTE NO EXISTE"
                    document.getElementById('fecha_factura').value = ''
                    
                }
            },error: function(error){console.log(error)}
        });
        console.log("buscar")
    })
})