from presencialTutoria import PresencialTutoria
from client import Client

def main():
    original = PresencialTutoria(
        title_tutoring="Álgebra Básica",
        tutor_id="T123",
        tutor="Ana González",
        subject="Matemática",
        date="2025-05-24",
        start_time="14:00",
        description="Clase de refuerzo sobre factorización",
        capacity=10
    )

    print("Original:")
    print(original)

    cliente = Client(original)
    clon = cliente.create_tutoria()

    clon.tutor = "Carlos Pérez"
    clon.title_tutoring = "Álgebra Avanzada"

    print("\nClon:")
    print(clon)

    print("\nOriginal después de clonar:")
    print(original)

if __name__ == "__main__":
    main()
