from django.shortcuts import render

def index(request):
    categorias = ["Todos", "Vestidos", "Blusas", "Pantalones", "Zapatos"]

    productos = [
        {"nombre": "Vestido elegante", "precio": "$50", "imagen": "img/Falda.jpeg", "categoria": "Vestidos"},
        {"nombre": "Blusa casual", "precio": "$30", "imagen": "img/Falda.jpeg", "categoria": "Blusas"},
        {"nombre": "Pantalón de moda", "precio": "$40", "imagen": "img/Falda.jpeg", "categoria": "Pantalones"},
        {"nombre": "Zapatos de tacón", "precio": "$60", "imagen": "img/Falda.jpeg", "categoria": "Zapatos"},
    ]
    
    return render(request, "store/index.html", {"productos": productos, "categorias": categorias})
