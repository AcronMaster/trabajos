def captura_calificaciones():
    calificaciones = [0] * 5  # Crear una lista con 5 elementos inicializados en 0
    for i in range(5):
        calificaciones[i] = int(input(f"Captura la calificación {i+1}: "))
    print("Calificaciones capturadas:", calificaciones)

if __name__ == "__main__":
    captura_calificaciones()




def manipula_frutas():
    frutas = ["mango", "manzana", "banana", "uvas"]  # Crear una lista de frutas
    print("Frutas iniciales:", frutas)

    # Eliminar elementos por índice
    frutas.pop(0)  # Elimina "mango"
    frutas.pop(1) 
    frutas.pop(2) # Después de eliminar "mango", "banana" está en la posición 1
    # Agregar una nueva fruta
    frutas.append("sandía")  # Añadir "sandía" al final
    print("Frutas después de modificaciones:", frutas)

if __name__ == "__main__":
    manipula_frutas()