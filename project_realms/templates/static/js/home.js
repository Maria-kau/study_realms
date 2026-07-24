document.addEventListener("DOMContentLoaded", () => {


    // =========================
    // BARRAS DE PROGRESSO
    // =========================

    document.querySelectorAll(".barra-preenchimento").forEach(barra => {

        const atual = Number(barra.dataset.progresso) || 0;
        const maximo = Number(barra.dataset.max) || 100;


        const porcentagem = (atual / maximo) * 100;


        barra.style.width = porcentagem + "%";

    });



    // =========================
    // GRÁFICO DOUGNUT
    // =========================


    const canvas = document.getElementById("graficoProgresso");


    if (!canvas){
        console.log("Canvas não encontrado");
        return;
    }



    let valor = canvas.getAttribute("data-progresso");


    console.log("Valor recebido:", valor);



    // remove %
    valor = valor.replace("%","");


    const progresso = parseFloat(valor) || 0;



    console.log("Valor convertido:", progresso);



    const restante = 100 - progresso;



    new Chart(canvas, {


        type:"doughnut",


        data:{


            datasets:[{

                data:[

                    progresso,

                    restante

                ],


                backgroundColor:[

                    "#00eaff",

                    "rgba(45,25,80,0.55)"

                ],


                borderColor:"transparent",


                borderWidth:0,


                borderRadius:20

            }]

        },



        options:{


            responsive:true,


            maintainAspectRatio:false,


            cutout:"75%",



            rotation:-90,


            circumference:360,



            animation:{


                animateRotate:true,


                duration:1800


            },



            plugins:{


                legend:{
                    display:false
                },


                tooltip:{
                    enabled:false
                }


            }


        }


    });


});