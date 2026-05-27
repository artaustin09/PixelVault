class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, juego):
        id = str(juego.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "juego_id": juego.id,
                "nombre": juego.titulo,
                "precio": str(juego.precio),
                "cantidad": 1,
                "total": str(juego.precio),
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["total"] = str(float(self.carrito[id]["precio"]) * self.carrito[id]["cantidad"])
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, juego):
        id = str(juego.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True