function cerrarModal() {
    var modal = document.getElementById("registroModal");
    if (modal) {
        modal.style.display = "none";
        window.location.href = "{% url 'login' %}";  // Redirige al login
    }
}

// Si la modal está visible, se cierra automáticamente en 3 segundos
document.addEventListener("DOMContentLoaded", function () {
    var modal = document.getElementById("registroModal");
    if (modal) {
        setTimeout(cerrarModal, 3000);
    }
});