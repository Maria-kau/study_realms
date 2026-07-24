document.addEventListener("DOMContentLoaded", function () {

    const mapa = document.getElementById("mapa");
    const colunas = 19;
    const linhas = 19;

    function renderizarMapaEConstrucoes() {
        if (!mapa) return;

        // Captura os elementos de construção existentes no HTML gerado pelo Django
        const elementosConstrucao = Array.from(mapa.querySelectorAll(".building"));
        
        // Mapeia os dados delas antes de limpar o DOM
        const dadosConstrucoes = elementosConstrucao.map(el => ({
            tipo: el.dataset.tipo,
            x: Number(el.dataset.x),
            y: Number(el.dataset.y),
            img: el.dataset.img
        }));

        // Limpa o mapa completamente para reconstruir a matriz limpa
        mapa.innerHTML = "";

        const posicoesTiles = {};
        const estilosRoot = getComputedStyle(document.documentElement);
        
        const tileWidth = parseFloat(estilosRoot.getPropertyValue("--tile-w")) || 60;
        const tileHeight = parseFloat(estilosRoot.getPropertyValue("--tile-h")) || 30;

        // ------------------------------------------
        // 1. CRIA A MATRIZ DE TILES
        // ------------------------------------------
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

                // Salva o ponto central exato do tile
                posicoesTiles[`${x},${y}`] = {
                    left: posX + (tileWidth / 2),
                    top: posY + (tileHeight / 2)
                };
            }
        }

        // ------------------------------------------
        // 2. INSERE AS CONSTRUÇÕES DENTRO DA MATRIZ
        // ------------------------------------------
        dadosConstrucoes.forEach(item => {
            const posicao = posicoesTiles[`${item.x},${item.y}`];

            if (!posicao) {
                console.warn(`Construção fora da matriz X:${item.x} Y:${item.y}`);
                return;
            }

            const building = document.createElement("div");
            building.classList.add("building");
            building.dataset.tipo = item.tipo;
            building.dataset.x = item.x;
            building.dataset.y = item.y;
            
            if (item.img) {
                building.style.backgroundImage = `url("${item.img}")`;
            }

            building.style.left = `${posicao.left}px`;
            building.style.top = `${posicao.top}px`;
            building.style.zIndex = item.x + item.y + 100;

            mapa.appendChild(building);
        });
    }

    renderizarMapaEConstrucoes();

    window.addEventListener("resize", renderizarMapaEConstrucoes);
});