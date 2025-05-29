from presencialTutoria import PresencialTutoria
from client import Client
from virtualTutoria import VirtualTutoria
def main():
    tutoriaPresencial = PresencialTutoria(
        title_tutoring="Álgebra Básica",
        tutor_id="T123",
        tutor="Ana González",
        subject="Matemática",
        date="2025-05-24",
        start_time="14:00",
        description="Clase de refuerzo sobre factorización",
        capacity=10
    )

    tutoriaVirtual = VirtualTutoria(
        title_tutoring="Cálculo Diferencial",
        tutor_id="T456",
        tutor="Luis Martínez",
        subject="Matemática Avanzada",
        date="2025-05-25",
        start_time="16:00",
        description="Sesión en línea sobre derivadas",
        capacity=20
    )




    cliente = Client(tutoriaPresencial)
    clonPresencial = cliente.create_tutoria()

    clonPresencial.tutor = "Carlos Pérez"
    clonPresencial.title_tutoring = "Álgebra Avanzada"

    cliente.setTutoria(tutoriaVirtual)
    clonVirtual = cliente.create_tutoria()
    clonVirtual.tutor = "María López"
    clonVirtual.title_tutoring = "Cálculo Integral"
    
    print("\ntutoriaVirtual:")
    print(tutoriaVirtual)
    
    print("\nclonVirtual:")
    print(clonVirtual)
    
    print("\ntutoriaVirtual después de clonVirtual:")
    print(tutoriaVirtual)


    
    print("\ntutoriaPresencial:")
    print(tutoriaPresencial)

    print("\nclonPresencial:")
    print(clonPresencial)

    print("\ntutoriaPresencial después de clonPresencialar:")
    print(tutoriaPresencial)

if __name__ == "__main__":
    main()
