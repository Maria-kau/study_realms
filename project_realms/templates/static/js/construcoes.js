document.addEventListener("DOMContentLoaded", function () {

    const mapa = document.getElementById("mapa");

    if (!mapa) return;

    const colunas = 19;
    const linhas = 19;


    function renderizarMapaEConstrucoes() {

        const construcoes = Array.from(
            mapa.querySelectorAll(".building")
        );

        console.log(
            "Total de construções encontradas no HTML:",
            construcoes.length
        );


        // Remove tiles antigos
        mapa.querySelectorAll(".tile").forEach(tile => {
            tile.remove();
        });


        const estilosRoot = getComputedStyle(
            document.documentElement
        );

        const tileWidth =
            parseFloat(
                estilosRoot.getPropertyValue("--tile-w")
            ) || 54;

        const tileHeight =
            parseFloat(
                estilosRoot.getPropertyValue("--tile-h")
            ) || 27;



        const posicoesTiles = {};



        // ============================
        // CRIA MAPA ISOMÉTRICO
        // ============================

        for (let x = 0; x < colunas; x++) {

            for (let y = 0; y < linhas; y++) {


                const posX =
                    (x - y) * (tileWidth / 2);

                const posY =
                    (x + y) * (tileHeight / 2);



                const tile = document.createElement("div");

                tile.classList.add("tile");


                tile.dataset.x = x;
                tile.dataset.y = y;


                tile.style.left = `${posX}px`;
                tile.style.top = `${posY}px`;


                mapa.appendChild(tile);



                posicoesTiles[`${x},${y}`] = {

                    left:
                        posX + (tileWidth / 2),

                    top:
                        posY + (tileHeight / 2)

                };

            }
        }



        // ============================
        // COLOCA CONSTRUÇÕES
        // ============================

        construcoes.forEach(building => {


            const x = Number(building.dataset.x);
            const y = Number(building.dataset.y);



            const posicao =
                posicoesTiles[`${x},${y}`];



            if (!posicao) {

                console.warn(
                    `Construção fora do mapa: ${x},${y}`
                );

                return;

            }



            const imgUrl =
                building.dataset.img;



            if (imgUrl) {

                building.style.backgroundImage =
                    `url("${imgUrl}")`;


                console.log(
                    "Carregando imagem:",
                    imgUrl
                );

            }



            const tipo =
                building.dataset.tipo || "tree";



            let largura = 40;
            let altura = 60;



            switch(tipo) {

                case "house":

                    largura = 80;
                    altura = 80;

                    break;


                case "special":

                    largura = 120;
                    altura = 120;

                    break;


                case "castle":

                    largura = 180;
                    altura = 180;

                    break;


                case "tree":

                default:

                    largura = 40;
                    altura = 60;

            }



            building.style.width =
                `${largura}px`;


            building.style.height =
                `${altura}px`;



            building.style.position =
                "absolute";


            building.style.backgroundRepeat =
                "no-repeat";


            building.style.backgroundSize =
                "contain";


            building.style.backgroundPosition =
                "center";



            building.style.left =
                `${posicao.left - largura / 2}px`;



            building.style.top =
                `${posicao.top - altura + tileHeight / 2}px`;



            building.style.zIndex =
                x + y + 100;



            mapa.appendChild(building);


        });


    }



    renderizarMapaEConstrucoes();


    window.addEventListener(
        "resize",
        renderizarMapaEConstrucoes
    );

});