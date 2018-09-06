$(document).ready( () => {
    console.log("Iniciando Estación!");
    start_sampling();
    $('#sidebarCollapse').on('click', () => {
        $('#sidebar').toggleClass('active');
    });
    $('#side-config').on('click', (data) => {
        var querystr = new URLSearchParams(document.location.search);
        var freq = querystr.get("frec")
        if (freq == null)
            freq = 2
        $('#side-config').attr('href', '/config?frec='+freq);
    });
    $('#side-home').on('click', (data) => {
        var querystr = new URLSearchParams(document.location.search);
        var freq = querystr.get("frec")
        if (freq == null)
            freq = 2
        $('#side-home').attr('href', '/home?frec='+freq);
    });
    $("#guardar-frec").on("click", toggleAlert);
    $('#bsalert').on('close.bs.alert', toggleAlert)
    
})


var timer;
function start_sampling() {
    var querystr = new URLSearchParams(document.location.search);

    var freq = querystr.get("frec")
    if (freq == null)
        freq = 2
    timer = setInterval(get_samples, freq*1000);
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
function checkValue(val) {
    if (val < 1 || val > 60)
        $('#guardar-frec').prop('disabled', true);
    else
    $('#guardar-frec').prop('disabled', false);
}

function toggleAlert(){
    $('#bsalert').toggleClass('in out'); 
    return false; // Keep close.bs.alert event from removing from DOM
}




/* $(window).on("unload", (e) => {
    $.get('/shut-down',  (result_code) => { 
        console.log("resultado de la finalizacion satisfactoria!", result_code);
        })
        .fail( (result_code) => {
            alert('Upa, algo salio mal al intentar apagar la estacion!', result_code);
        });
}) */