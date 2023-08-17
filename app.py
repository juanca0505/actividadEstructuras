#Crear una clase Student que tiene los siguientes atributos: name, age y grades (una lista de números)
#Crear un constructor que inicialice los atributos
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades


# Crear un método llamado add_grade que recibe un número como parámetro y lo agrega a la lista grades.
    def add_grade (self, grade):
        self.grades.append (grade)

#Crear otro método llamado average_grade que calcule y retorne la nota promedio de la lista de notas grandes
    def average_grade (self):
        if len (self.grades) == 0:
            return 0
        else:
            return sum(self.grades) / len (self.grades)

#Crear una lista de diccionarios donde cada diccionario contiene la información de un estudiante.

estudiantes = []

estudiante1 = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "edad": 20,
    "curso": "Programación"
}
estudiantes.append(estudiante1)
estudiante2 = {
    "nombre": "María",
    "apellido": "González",
    "edad": 22,
    "curso": "Matemáticas"
}
estudiantes.append(estudiante2)
print(estudiantes)