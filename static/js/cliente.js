$(document).ready(function(){

    function crearReferencia(){ return Math.floor((Math.random() * (100000000 - 100000 + 1)) + 100000); }

    if(localStorage.getItem('referencia') == undefined ){
        ref = crearReferencia()
    }else{
        ref = localStorage.getItem('referencia')
    }
    document.getElementById('referencia').value = ref
    validarReferenciaExistente(ref)

    function validarReferenciaExistente(referencia){
        $.ajax({
            url: '/buscar-referencia',
            data: $('form').serialize(),
            type: 'POST',
            success: function(factura){
                if(factura == null){
                    document.getElementById('referencia').value = referencia
                    localStorage.setItem('referencia', referencia)
                }else{
                    ref = crearReferencia()
                    validarReferenciaExistente(ref)
                }
            }
        })
    }
    
    document.getElementById('identificacion_search').addEventListener('input', function(){
        event.preventDefault();
        buscar = document.getElementById("identificacion_search")
        $.ajax({
            url: '/buscar-usuario',
            data: $('form').serialize(),
            type: 'POST',
            success: function(usuario){
                if(usuario!=null){
                    document.getElementById('id_cliente').value = usuario[0]
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
    })
})