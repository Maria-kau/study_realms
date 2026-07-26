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



document.addEventListener("DOMContentLoaded", function () {
    const mapa = document.getElementById("mapa");
    const colunas = 19;
    const linhas = 19;

    function renderizarMapaEConstrucoes() {
        if (!mapa) return;

        const construcoes = Array.from(mapa.querySelectorAll(".building"));
        console.log("Total de construções encontradas no HTML:", construcoes.length);

        mapa.querySelectorAll(".tile").forEach(tile => tile.remove());

        const posicoesTiles = {};
        const estilosRoot = getComputedStyle(document.documentElement);
        const tileWidth = parseFloat(estilosRoot.getPropertyValue("--tile-w")) || 54;
        const tileHeight = parseFloat(estilosRoot.getPropertyValue("--tile-h")) || 27;

        // Cria o grid
        for (let x = 0; x < colunas; x++) {
            for (let y = 0; y < linhas; y++) {
                const posX = (x - y) * (tileWidth / 2);
                const posY = (x + y) * (tileHeight / 2);

                const tile = document.createElement("div");
                tile.classList.add("tile");
                tile.dataset.x = x;
                tile.dataset.y = y;
                tile.style.left = `${posX}px`;
                tile.style.top = `${posY}px`;

                mapa.appendChild(tile);
                posicoesTiles[`${x},${y}`] = {
                    left: posX + (tileWidth / 2),
                    top: posY + (tileHeight / 2)
                };
            }
        }

        // Posiciona cada construção
        construcoes.forEach(building => {
            const x = Number(building.dataset.x);
            const y = Number(building.dataset.y);
            const posicao = posicoesTiles[`${x},${y}`];

            if (!posicao) {
                console.warn(`ERRO: Construção com X:${x} e Y:${y} está fora do grid 19x19!`);
                return;
            }

            const imgUrl = building.dataset.img;
            if (imgUrl) {
                building.style.backgroundImage = `url("${imgUrl}")`;
                console.log(`Carregando imagem: ${imgUrl}`);
            } else {
                console.warn(`AVISO: Construção X:${x}, Y:${y} está sem o atributo data-img!`);
            }

            mapa.appendChild(building);

            // Força tamanhos padrão seguros caso o tipo venha vazio
            const tipo = building.dataset.tipo || "tree";
            let larguraReal = 40;
            let alturaReal = 60;

            if (tipo === "house") { larguraReal = 80; alturaReal = 80; }
            else if (tipo === "special") { larguraReal = 120; alturaReal = 120; }
            else if (tipo === "castle") { larguraReal = 180; alturaReal = 180; }
            else { larguraReal = 40; alturaReal = 60; } // Padrão para tree/outros

            building.style.width = `${larguraReal}px`;
            building.style.height = `${alturaReal}px`;
            building.style.position = "absolute";
            
            

            building.style.left = `${posicao.left - (larguraReal / 2)}px`;
            building.style.top = `${posicao.top - alturaReal + (tileHeight / 2)}px`;
            building.style.zIndex = x + y + 100;
        });
    }

    renderizarMapaEConstrucoes();
    window.addEventListener("resize", renderizarMapaEConstrucoes);
});
