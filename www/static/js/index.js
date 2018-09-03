$(document).ready( () => {
    console.log("Doc ready!");
    start_sampling();
});


var timer;

function start_sampling() {
    timer = setInterval(get_samples, 1000);
}

function get_samples() {
    $.get("/", (data) => {
        console.log("samples", data);
    });
}