document.addEventListener("DOMContentLoaded", () => {

    const startBtn = document.getElementById("start-btn");
    const pauseBtn = document.getElementById("pause-btn");
    const cancelBtn = document.getElementById("cancel-btn");

    const countdown = document.getElementById("countdown");

    const duracaoInput = document.getElementById("duracao-input");
    const tipoSelect = document.getElementById("tipo-select");

    const form = document.getElementById("complete-form");

    let tempo = 0;
    let intervalo = null;
    let pausado = false;


    function atualizarTela() {

        let minutos = Math.floor(tempo / 60);
        let segundos = tempo % 60;

        countdown.textContent =
            String(minutos).padStart(2,"0") +
            ":" +
            String(segundos).padStart(2,"0");
    }


    startBtn.addEventListener("click", () => {

        if(intervalo) return;


        if(!pausado){

            tempo = Number(duracaoInput.value) * 60;

        }


        pausado = false;


        startBtn.style.display = "none";
        pauseBtn.style.display = "block";
        cancelBtn.style.display = "block";


        intervalo = setInterval(()=>{

            tempo--;

            atualizarTela();


            if(tempo <= 0){

                clearInterval(intervalo);
                intervalo = null;


                document.getElementById("form-tipo").value =
                    tipoSelect.value;


                document.getElementById("form-duracao").value =
                    duracaoInput.value;


                document.getElementById("form-concluida").value =
                    "sim";


                form.submit();

            }


        },1000);


    });



    pauseBtn.addEventListener("click",()=>{

        if(intervalo){

            clearInterval(intervalo);
            intervalo=null;

            pausado=true;

            pauseBtn.textContent="Continuar";

        }else{

            intervalo=setInterval(()=>{

                tempo--;

                atualizarTela();

                if(tempo<=0){
                    clearInterval(intervalo);
                    form.submit();
                }

            },1000);

            pauseBtn.textContent="Pausar";

        }

    });



    cancelBtn.addEventListener("click",()=>{

        clearInterval(intervalo);

        intervalo=null;

        tempo=0;

        atualizarTela();


        startBtn.style.display="block";
        pauseBtn.style.display="none";
        cancelBtn.style.display="none";


    });


});
