let index = 0;

function moverCarrusel(direccion) {
    const carrusel = document.querySelector(".carousel");
    const totalSlides = document.querySelectorAll(".carousel-slide").length;

    index += direccion;

    if (index < 0) {
        index = totalSlides - 1;
    } else if (index >= totalSlides) {
        index = 0;
    }

    let desplazamiento = -index * 100; // Mover el carrusel horizontalmente
    carrusel.style.transform = `translateX(${desplazamiento}%)`;
}

// Cambio automático cada 4 segundos
setInterval(() => {
    moverCarrusel(1);
}, 4000);
