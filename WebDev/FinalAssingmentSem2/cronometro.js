let [milesimos, segundos, minutos, horas] = [0, 0, 0, 0];
let timerRef = document.querySelector('.cronometro')
let int;

document.getElementById('iniciar').addEventListener('click', ()=>{
    int = setInterval(discplayTimer,10);
    document.querySelector('.icone i').className = "fas fa-play-circle"
});

document.getElementById('pausar').addEventListener('click', ()=>{
    clearInterval(int);
    document.querySelector('.icone i').className = "fas fa-pause-circle"
});

document.getElementById('parar').addEventListener('click', ()=>{
    clearInterval(int);
    [milesimos, segundos, minutos, horas] = [0, 0, 0, 0];
    timerRef.innerHTML = '00 : 00 : 00 : 000 ';
    document.querySelector('.icone i').className = "fas fa-stop-circle"
})

document.getElementById('zerar').addEventListener('click', ()=>{
    [milesimos, segundos, minutos, horas] = [0, 0, 0, 0];
    timerRef.innerHTML = '00 : 00 : 00 : 000 ';
})

function discplayTimer(){
    milesimos += 10;
    if(milesimos == 1000){
        milesimos = 0;
        segundos++;
        if(segundos == 60){
            segundos = 0;
            minutos++;
            if(minutos == 60){
                minutos = 0;
                horas++;
            }
        }
    }
    let h = horas < 10 ? "0" + horas : horas;
    let m = minutos < 10 ? "0" + minutos : minutos;
    let s = segundos < 10 ? "0" + segundos : segundos;
    let ms = milesimos < 10 ? "00" + milesimos : milesimos < 100 ? "0" + milesimos : milesimos;

    timerRef.innerHTML = ` ${h} : ${m} : ${s} : ${ms}`
}

