$(document).ready( () => {
    console.log("Iniciando Estación!");
    start_sampling();
    $('#sidebarCollapse').on('click', () => {
        $('#sidebar').toggleClass('active');
    });
    
});


var timer;

function start_sampling() {
    timer = setInterval(get_samples, 5000);
}

function get_samples() {
    $.get("/samples",  
        (data) => {
            $('#temp_actual').html(data.temp_actual);
            $('#hum_actual').html(data.hum_actual);
            $('#pres_actual').html(data.pres_actual);
            $('#viento_actual').html(data.viento_actual);
            $('#temp_promedio').html(data.temp_promedio);
            $('#hum_promedio').html(data.hum_promedio);
            $('#pres_promedio').html(data.pres_promedio);
            $('#viento_promedio').html(data.viento_promedio);
            $('#frec-muestreo').html(data);
            console.log(data);
        })
        .fail( () => {
            alert('Upa, algo salio mal al obtener las muestras!');
        });
}

$(window).on("unload", (e) => {
    $.get('/shut-down',  (result_code) => { 
        console.log("resultado de la finalizacion satisfactoria!", result_code);
        })
        .fail( (result_code) => {
            alert('Upa, algo salio mal al intentar apagar la estacion!', result_code);
        });
  })