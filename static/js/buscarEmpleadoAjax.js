$(document).ready(function(){
    document.getElementById('identificacion').addEventListener('input', function(){
        document.getElementById('nuevo_empleado').innerHTML = ''
    })
    $('#get_cliente').submit(function(e){
        e.preventDefault();
        identificacion = document.getElementById('identificacion')
        campo = document.getElementById('nuevo_empleado')
        $.ajax({
            url: '/buscar-usuario',
            data: $('form').serialize(),
            type: 'POST',
            success: function(usuario){
                if(usuario!=null){
                    if(usuario[9] != 'administrador'){
                        nombres = usuario[2]+' '+usuario[3]
                        campo.innerHTML = '<form action="/mi-perfil" method="POST" id="regis_empleado" >'+
                                                '<div class="row">'+
                                                    '<input type="hidden" class="form-control" value = "'+usuario[0]+'" id="id_cliente" name="id_cliente">'+
                                                    '<div class="col-md-4 mb-3">'+
                                                        '<input type="text" class="form-control" value = "'+usuario[1]+'" placeholder="identificacion" id="identidad" disabled>'+
                                                    '</div>'+
                                                    '<div class="col-md-4 mb-3">'+
                                                        '<input type="text" class="form-control" value = "'+nombres+'"   placeholder="nombres" id="nombres" disabled>'+
                                                    '</div>'+
                                                    '<div class="col-md-4 mb-3">'+
                                                        '<input type="text" class="form-control" value = "'+usuario[9]+'" placeholder="rol" id="rol" disabled>'+
                                                    '</div>'+
                                                    '<div class="col-md-6 mb-3">'+
                                                        '<input type="text" class="form-control" placeholder="usuario" id="usuario" name="usuario">'+
                                                    '</div>'+
                                                    '<div class="col-md-6 mb-3">'+
                                                        '<input type="text" class="form-control" placeholder="password" id="password" name="password">'+
                                                    '</div>'+
                                                    '<div class="d-grid gap-2 col-6 mx-auto mb-3">'+
                                                        '<button type="submit" class="btn btn-dark cargar" >GUARDAR</button>'+
                                                    '</div>'
                                                '</div>'+
                                            '</form>'
                    }else{
                        campo.innerHTML = '<ul class="alert alert-danger">'+
                                            '<li style="padding-left: 10px; list-style: none;"><small>El administrador no puede cambiar su rol a empleado</li>'+
                                        '</ul>'
                    }
                }else{
                    campo.innerHTML = '<ul class="alert alert-danger">'+
                                            '<li style="padding-left: 10px; list-style: none;"><small>El cliente '+identificacion.value+' no se encuentra registrado, porfavor registrelo <a href="/crear-cliente" class="alert-link">Aquí</a></small></li>'+
                                        '</ul>'
                }
                identificacion.value = ''
            },error: function(error){console.log(error)}
        });
    });
});