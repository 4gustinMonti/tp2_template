$(document).ready( () => {
    console.log("Doc ready!");
    start_sampling();
    $('#sidebarCollapse').on('click', () => {
        $('#sidebar').toggleClass('active');
    });
    
});


var timer;

function start_sampling() {
    timer = setInterval(get_samples, 3000);
}

function get_samples() {
    $.get("/samples",  function (data) {
        console.log(data);})
        .fail( () => {
            alert('Upa, algo salio mal al obtener las muestras!');
        });
}

$(window).on("unload", (e) => {
    $.get('/shut-down',  (data) => { 
        console.log(data);
        })
        .fail( (failed) => {
            alert('Upa, algo salio mal al intentar apagar la estacion!');
        });
  })