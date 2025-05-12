class Pokenea:
    def __init__(self, id, nombre, altura, habilidad, imagen_key, frase):
        self.id = id
        self.nombre = nombre
        self.altura = altura
        self.habilidad = habilidad
        self.imagen_key = imagen_key
        self.frase = frase

POKENEAS = [
    Pokenea(1, "Ñerazor", 1.62, "Combo de arepas invocadas", "Ñerazor.png", "La vida es como el reguetón: si no lo bailás, te lo perdés."),
    Pokenea(2, "TusaQueen", 1.70, "Curación emocional con Karol G", "TusaQueen.png", "Todo mal de amores se arregla con una rumba en Provenza."),
    Pokenea(3, "Guaraloco", 1.55, "Niebla embriagadora de guaro", "Guaraloco.png", "Si la vida te da guaro, ¡hacé parche!"),
    Pokenea(4, "Vallenamaster", 1.80, "Vallenato emocional paralizante", "Vallenamester.png", "En el fondo del alma, todos tenemos un Diomedes dormido."),
    Pokenea(5, "Neapower", 1.65, "Plataformas invisibles de energía paisa", "Neapower.png", "Con verraquera, hasta lo imposible se vuelve costumbre."),
    Pokenea(6, "Chancletón", 1.48, "Chancleta teledirigida", "Chancleton.png", "El respeto entra por donde cae la chancleta."),
    Pokenea(7, "Arepaluz", 1.60, "Arepas restauradoras de energía", "Arepaluz.png", "Sin arepa no hay pensamiento lúcido."),
    Pokenea(8, "Farrafox", 1.75, "Fiesta espontánea en zona neutra", "Farrafox.png", "Que la vida no se te pase esperando el viernes."),
    Pokenea(9, "Paisawitch", 1.68, "Hechizos de tinto cargado", "Paisawitch.png", "Una buena bruja no hechiza: simplemente ofrece un tinto."),
    Pokenea(10, "Parchadín", 1.73, "Zona de relajación instantánea", "Parchadin.png", "Parchar es un arte que pocos dominan bien."),
]