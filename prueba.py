from tkinter import Canvas, Tk, PhotoImage
from PIL import Image, ImageTk

class Aplicacion:
    def __init__(self, ventana, imagen_path):
        self.ventana = ventana
        self.ventana.title("Selección Automática")

        # Cargar la imagen
        self.imagen = Image.open(imagen_path)
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)

        # Crear el lienzo (canvas)
        self.canvas = Canvas(ventana, width=self.imagen.width, height=self.imagen.height)
        self.canvas.pack()

        # Mostrar la imagen en el canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagen_tk)

        # Configurar la función de clic en el canvas
        self.canvas.bind("<Button-1>", self.seleccion_automatica)

    def seleccion_automatica(self, evento):
        # Obtener las coordenadas del clic
        x, y = evento.x, evento.y

        # Implementar tu algoritmo de selección automática aquí
        # Puedes usar las coordenadas (x, y) para determinar la región seleccionada

        # Ejemplo: Dibujar un polígono alrededor del punto de clic
        self.canvas.create_polygon(x-10, y-10, x+10, y-10, x+10, y+10, x-10, y+10, fill="", outline="red")

if __name__ == "__main__":
    # Ruta de la imagen
    imagen_path = "Ejemplos/i.png"  # Reemplaza con la ruta de tu imagen

    # Crear la ventana de la aplicación
    root = Tk()
    app = Aplicacion(root, imagen_path)

    # Ejecutar el bucle principal de la interfaz gráfica
    root.mainloop()
