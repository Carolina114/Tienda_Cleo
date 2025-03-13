document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("modalCompra");
    const closeModal = document.querySelector(".close-modal");

    const modalImg = document.getElementById("modal-img");
    const modalTitle = document.getElementById("modal-title");
    const modalPrice = document.getElementById("modal-price");
    const modalProveedor = document.getElementById("modal-proveedor");
    const modalDescripcion = document.getElementById("modal-descripcion");
    const modalTallas = document.getElementById("modal-tallas");
    const cantidadInput = document.getElementById("cantidadInput");
    const btnSumar = document.getElementById("sumarCantidad");
    const btnRestar = document.getElementById("restarCantidad");
    const btnAgregarCarrito = document.querySelector(".modal-add-cart");
    const carritoContador = document.getElementById("cart-count");

    let productoSeleccionado = {};

    // ✅ Evento para abrir la modal al hacer clic en "COMPRAR"
    document.querySelectorAll(".buy-now").forEach(button => {
        button.addEventListener("click", function () {
            const imagen = this.getAttribute("data-imagen");
            const nombre = this.getAttribute("data-nombre");
            const precio = this.getAttribute("data-precio");
            const descripcion = this.getAttribute("data-descripcion");

            // Asignar los valores en la modal
            modalImg.src = imagen;
            modalTitle.textContent = nombre;
            modalPrice.textContent = `${precio} COP`;
            modalProveedor.textContent = "Navissi Clothing";
            modalDescripcion.textContent = descripcion;

            // Limpiar y agregar botones de talla
            modalTallas.innerHTML = "";
            ["XS", "S", "M", "L"].forEach(talla => {
                let btnTalla = document.createElement("button");
                btnTalla.textContent = talla;
                btnTalla.classList.add("btn-talla");
                btnTalla.addEventListener("click", function () {
                    document.querySelectorAll(".btn-talla").forEach(btn => btn.style.border = "1px solid #ccc");
                    this.style.border = "2px solid black";
                    productoSeleccionado.talla = this.textContent;
                });
                modalTallas.appendChild(btnTalla);
            });

            cantidadInput.value = 1;
            productoSeleccionado = { imagen, nombre, precio, descripcion, cantidad: 1, talla: "S" };

            modal.style.display = "flex";
        });
    });

    // ✅ Botones de cantidad
    btnSumar.addEventListener("click", () => cantidadInput.value = parseInt(cantidadInput.value) + 1);
    btnRestar.addEventListener("click", () => {
        if (cantidadInput.value > 1) cantidadInput.value = parseInt(cantidadInput.value) - 1;
    });

    // ✅ Función para agregar al carrito
    btnAgregarCarrito.addEventListener("click", function () {
        let carrito = JSON.parse(localStorage.getItem("carrito")) || [];

        let nuevoProducto = {
            imagen: modalImg.src,
            nombre: modalTitle.textContent,
            precio: modalPrice.textContent.replace(" COP", ""),
            cantidad: parseInt(cantidadInput.value),
            talla: productoSeleccionado.talla || "S"
        };

        // Verificar si el producto ya está en el carrito
        let productoExistente = carrito.find(p => p.nombre === nuevoProducto.nombre && p.talla === nuevoProducto.talla);
        if (productoExistente) {
            productoExistente.cantidad += nuevoProducto.cantidad;
        } else {
            carrito.push(nuevoProducto);
        }

        localStorage.setItem("carrito", JSON.stringify(carrito));

        // ✅ Actualizar icono del carrito en la barra de navegación
        actualizarCarritoIcono();

        // ✅ Notificación elegante con SweetAlert2
        Swal.fire({
            title: "¡Producto agregado!",
            text: "Tu producto ha sido agregado al carrito.",
            icon: "success",
            confirmButtonText: "OK",
            confirmButtonColor: "#6D28D9", // Color morado
            backdrop: `
                rgba(0,0,0,0.6)
                url("https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif")
                left top
                no-repeat
            `
        });

        modal.style.display = "none";
    });

    // ✅ Función para actualizar el número de productos en el icono del carrito
    function actualizarCarritoIcono() {
        let carrito = JSON.parse(localStorage.getItem("carrito")) || [];
        let totalProductos = carrito.reduce((total, p) => total + p.cantidad, 0);
        carritoContador.textContent = totalProductos;
    }

    // ✅ Cargar número de productos en el carrito al iniciar
    actualizarCarritoIcono();

    // ✅ Cerrar la modal
    closeModal.addEventListener("click", () => modal.style.display = "none");
});
