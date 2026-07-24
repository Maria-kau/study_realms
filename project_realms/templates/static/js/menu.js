const btnMenu = document.getElementById("btn-menu");
const menuLateral = document.getElementById("menu");

if (btnMenu && menuLateral) {
    btnMenu.addEventListener("click", () => {
        menuLateral.classList.toggle("abrir-menu");
    });
}