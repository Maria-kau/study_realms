/*____________criação de matrizes____________*/
const mapa = document.getElementById("mapa");

const tileWidth = 50;
const tileHeight = 25;

const linhas = 19;
const colunas = 19;

// Ajuste esses dois valores até o primeiro tile bater no topo da ilha
const offsetX = 940;   // Move o mapa para esquerda/direita
const offsetY = 190; // Move o mapa para cima/baixo

for (let y = 0; y < linhas; y++) {
  for (let x = 0; x < colunas; x++) {
    const tile = document.createElement("div");
    tile.classList.add("tile");

    // Cálculo com os offsets
    const left = (x - y) * (tileWidth / 2) + offsetX;
    const top  = (x + y) * (tileHeight / 2) + offsetY;

    tile.style.left = left + "px";
    tile.style.top = top + "px";
    tile.style.zIndex = x + y;

    mapa.appendChild(tile);

    /*_________________criaçao de arvores_________*/
  if (x===1 && y===10){
    const arvore = document.createElement("div");
    arvore.classList.add("arvore");

    arvore.style.left = (left - 9) + "px";
    arvore.style.top = (top - 50) + "px";
    arvore.style.zIndex = x + y;

    mapa.appendChild(arvore);
  }
  if (x===5 && y===10){
    const arvore = document.createElement("div");
    arvore.classList.add("arvore");

    arvore.style.left = (left - 9) + "px";
    arvore.style.top = (top - 50) + "px";
    arvore.style.zIndex = x + y;

    mapa.appendChild(arvore);
  }
  if (x===1 && y===1){
    
  }
  }
}
/*__________________estrelas__________________*/
const estrelas =
    document.querySelector(".estrelas");


for(let i = 0; i < 100; i++) {

    const estrela =
        document.createElement("div");

    estrela.classList.add("estrela");


    /* TAMANHO ALEATÓRIO */

    const tamanho =
        Math.random() * 4+2;

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

/*_____________bolinhas brilhantes__________*/ 
const brilhos = document.querySelector(".brilhos");
for (b=0;b<100;b++){
    const brilho = document.createElement("div");
    brilho.classList.add("brilho");
    /*tamanaho*/
    const tamanho = Math.random() * 1;
    brilho.style.width = tamanho + "px";
    brilho.style.height = tamanho + "px";
    /*posiçao*/
    brilho.style.left = Math.random() * window.innerWidth + "px";
    brilho.style.top = Math.random() * window.innerHeight + "px";
    /* velocidade */
    brilho.style.animationDuration = (Math.random() * 2+2) + "s";

    brilhos.appendChild(brilho)
}