$( document ).ready(function() {
    fecha = document.getElementById("fecha")
    const tiempoTranscurrido = Date.now();
    const hoy = new Date(tiempoTranscurrido);
    
    fecha.innerHTML = hoy.toDateString();
});