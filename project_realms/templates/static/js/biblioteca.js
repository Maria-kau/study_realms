function atualizarBarrasDeProgresso(data) {

    const moduleProgress = data?.module_progress;
    const subjectProgress = data?.subject_progress;

    if (moduleProgress) {
        document.querySelectorAll('.barra-preenchimento[data-progress-key="module"]').forEach(barra => {
            const progresso = Number(moduleProgress.percentage) || 0;
            barra.style.width = `${Math.max(0, Math.min(100, progresso))}%`;
            barra.dataset.progresso = progresso;
        });

        document.querySelectorAll('[data-progress-label="module"]').forEach(el => {
            el.textContent = `${Math.round(Number(moduleProgress.percentage) || 0)}%`;
        });

        document.querySelectorAll('[data-progress-counter="module"]').forEach(el => {
            el.textContent = `${moduleProgress.completed}/${moduleProgress.total_contents} conteúdos concluídos`;
        });
    }

    if (subjectProgress) {
        document.querySelectorAll('.barra-preenchimento[data-progress-key="subject"]').forEach(barra => {
            const progresso = Number(subjectProgress.percentage) || 0;
            barra.style.width = `${Math.max(0, Math.min(100, progresso))}%`;
            barra.dataset.progresso = progresso;
        });

        document.querySelectorAll('[data-progress-label="subject"]').forEach(el => {
            el.textContent = `${Math.round(Number(subjectProgress.percentage) || 0)}%`;
        });

        document.querySelectorAll('[data-progress-counter="subject"]').forEach(el => {
            el.textContent = `${subjectProgress.completed}/${subjectProgress.total_contents} conteúdos concluídos`;
        });
    }
}


document.addEventListener("DOMContentLoaded", function(){


    const botoes = document.querySelectorAll(".btn-validacao");


    botoes.forEach(botao => {


        botao.addEventListener("click", function(){


            const url = this.dataset.url;


            fetch(url, {

                method: "POST",

                headers: {

                    "X-CSRFToken": getCookie("csrftoken"),

                }

            })


            .then(response => response.json())


            .then(data => {


                this.classList.add("concluido");


                this.innerHTML = "✓ Concluído";


                const status = this.nextElementSibling;


                status.innerHTML = "Conteúdo concluído!";

                atualizarBarrasDeProgresso(data);


            })


            .catch(error => {

                console.error(error);

            });


        });


    });


});





function getCookie(name) {


    let cookieValue = null;


    if(document.cookie && document.cookie !== ""){


        const cookies = document.cookie.split(";");


        for(let cookie of cookies){


            cookie = cookie.trim();


            if(cookie.startsWith(name + "=")){


                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );


                break;

            }

        }

    }


    return cookieValue;

}

document.addEventListener("DOMContentLoaded", () => {

    const barras = document.querySelectorAll(".barra-preenchimento");


    barras.forEach(barra => {

        const progresso = barra.dataset.progresso;


        barra.style.width = `${Math.max(0, Math.min(100, Number(progresso) || 0))}%`;

    });

});