function filtrarCategoria(categoria) {
    let productos = document.querySelectorAll(".producto");

    productos.forEach(producto => {
        let categoriaProducto = producto.getAttribute("data-categoria");

        if (categoria === "Todos" || categoriaProducto === categoria) {
            producto.style.display = "block";
        } else {
            producto.style.display = "none";
        }
    });
}