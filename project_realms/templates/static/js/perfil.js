

document.addEventListener("DOMContentLoaded", () => {

    document.querySelectorAll(".barra-preenchimento").forEach(barra => {

        const atual = Number(barra.dataset.progresso);
        const maximo = Number(barra.dataset.max);

        let porcentagem = 0;

        if (maximo > 0) {
            porcentagem = (atual / maximo) * 100;
        }

        barra.style.width = porcentagem + "%";
    });

});