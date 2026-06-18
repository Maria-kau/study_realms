
function proximaEtapa(){

    document
        .getElementById("etapa1")
        .classList
        .remove("active")

    document
        .getElementById("etapa2")
        .classList
        .add("active")
}

function voltarEtapa(){

    document
        .getElementById("etapa2")
        .classList
        .remove("active")

    document
        .getElementById("etapa1")
        .classList
        .add("active")
}


/*_____________bolinhas brilhantes__________*/ 
const brilhos = document.querySelector(".brilhos");
for (let b=0;b<100;b++){
    const brilho = document.createElement("div");
    brilho.classList.add("brilho");
    /*tamanaho*/
    const tamanho = Math.random();
    brilho.style.width = tamanho + "px";
    brilho.style.height = tamanho + "px";
    /*posiçao*/
    brilho.style.left = Math.random() * window.innerWidth + "px";
    brilho.style.top = Math.random() * window.innerHeight + "px";
    /* velocidade */
    brilho.style.animationDuration = (Math.random() * 4+2) + "s";

    brilhos.appendChild(brilho)
}
/*__________________estrelas__________________*/
const estrelas = document.querySelector(".estrelas");
for(let i = 0; i < 100; i++) {

    const estrela =
        document.createElement("div");

    estrela.classList.add("estrela");


    /* TAMANHO ALEATÓRIO */

    const tamanho =
        Math.random() * 2+3;

    estrela.style.width =
        tamanho + "px";

    estrela.style.height =
        tamanho + "px";


    /* POSIÇÃO ALEATÓRIA */

    estrela.style.left =
        Math.random() * window.innerWidth + "px";

    estrela.style.top =
        Math.random() * window.innerHeight + "px";


    /* VELOCIDADE ALEATÓRIA */

    estrela.style.animationDuration =
        (Math.random() * 4 + 2) + "s";


    estrelas.appendChild(estrela);
}

