

/*__________________estrelas__________________*/
const estrelas = document.querySelector(".estrelas");

for(let i = 0; i < 100; i++) {
    const estrela = document.createElement("div");
    estrela.classList.add("estrela");

    /* TAMANHO ALEATÓRIO */
    const tamanho = Math.random() * 4 + 2;
    estrela.style.width = tamanho + "px";
    estrela.style.height = tamanho + "px";

    /* POSIÇÃO ALEATÓRIA */
    estrela.style.left = Math.random() * window.innerWidth + "px";
    estrela.style.top = Math.random() * window.innerHeight + "px";

    /* VELOCIDADE ALEATÓRIA */
    estrela.style.animationDuration = (Math.random() * 4 + 2) + "s";

    estrelas.appendChild(estrela);
}

/*_____________bolinhas brilhantes__________*/ 
const brilhos = document.querySelector(".brilhos");

for (let b = 0; b < 100; b++) {
    const brilho = document.createElement("div");
    brilho.classList.add("brilho");

    /* tamanho */
    const tamanho = Math.random() * 1;
    brilho.style.width = tamanho + "px";
    brilho.style.height = tamanho + "px";

    /* posição */
    brilho.style.left = Math.random() * window.innerWidth + "px";
    brilho.style.top = Math.random() * window.innerHeight + "px";

    /* velocidade */
    brilho.style.animationDuration = (Math.random() * 2 + 2) + "s";

    brilhos.appendChild(brilho);
}





