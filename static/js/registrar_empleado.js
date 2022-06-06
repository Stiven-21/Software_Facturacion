$(document).ready(function(){
    $('#nuevo_empleado').submit(function(event){
        event.preventDefault();
        id_cliente = document.getElementById('id_cliente')
        usuario = document.getElementById('usuario')
        password = document.getElementById('password')
        alerta = document.getElementById('alerta_empleado')
        if(usuario.value == ''){
            alerta.innerHTML = '<ul class="alert alert-danger">'+
                                    '<li style="padding-left: 10px; list-style: none;"><small>Debe llenar el campo usuario</li>'+
                                '</ul>'
            return
        }
        if(password.value == ''){
            alerta.innerHTML = '<ul class="alert alert-danger">'+
                                '<li style="padding-left: 10px; list-style: none;"><small>Debe llenar el campo password</li>'+
                            '</ul>'
            return
        }else{
            if(password.value.length < 8){
                alerta.innerHTML = '<ul class="alert alert-danger">'+
                                '<li style="padding-left: 10px; list-style: none;"><small>La password debe contener mas de 8 caracteres</li>'+
                            '</ul>'
                return
            }
        }
        $.ajax({
            url: '/cliente-usuario',
            data: $('form').serialize(),
            type: 'POST',
            success: function(valLogin){
                if(valLogin != null){
                    alerta.innerHTML = '<ul class="alert alert-danger">'+
                                '<li style="padding-left: 10px; list-style: none;"><small>Ya se encuentra registrado un cliente con este usuario</li>'+
                            '</ul>'
                    return
                }else{
                    alerta.innerHTML = ''
                    $.ajax({
                        url: '/guardar-login',
                        data: $('form').serialize(),
                        type: 'POST',
                        success: function(response){
                            document.getElementById('nuevo_empleado').innerHTML = ''
                            alerta.innerHTML = '<ul class="alert alert-success">'+
                                '<li style="padding-left: 10px; list-style: none;"><small>'+response+'</li>'+
                            '</ul>'
                    return
                        },error: function(error){console.log(error)}
                    })
                }
            },error: function(error){console.log(error)}
        })
    })
})