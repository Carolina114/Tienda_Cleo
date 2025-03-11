// Asegurar que 'index' solo se declara una vez
if (typeof index === "undefined") {
    var index = 0;
}

function moverProductos(direccion) {
    const wrapper = document.querySelector(".products-wrapper");
    const carousel = document.querySelector(".products-carousel");

    if (!wrapper || !carousel) {
        console.error("No se encontró el contenedor del carrusel de productos.");
        return;
    }

    const totalProductos = document.querySelectorAll(".product-item").length;
    const productosVisibles = Math.floor(carousel.clientWidth / 250); // 250px = Ancho aprox de cada producto

    index += direccion;

    // Controlar los límites del desplazamiento
    if (index < 0) {
        index = totalProductos - productosVisibles;
    } else if (index >= totalProductos - productosVisibles + 1) {
        index = 0;
    }

    // Mover el carrusel
    let desplazamiento = -index * 270; // 250px producto + 20px gap
    wrapper.style.transform = `translateX(${desplazamiento}px)`;
}

// Agregar un console.log para verificar que el script se está cargando
console.log("✅ Script carrusel_productos.js cargado correctamente.");
