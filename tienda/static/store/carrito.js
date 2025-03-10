let carrito = [];

function agregarAlCarrito(nombre, precio) {
    carrito.push({ nombre, precio });
    actualizarCarrito();
}

function actualizarCarrito() {
    let cartCountElement = document.getElementById("cart-count");

    if (cartCountElement) {
        cartCountElement.innerText = carrito.length;  // Actualizar el número del carrito
    } else {
        console.error("Elemento #cart-count no encontrado.");
    }
}
