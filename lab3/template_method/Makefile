# Makefile para construir y testear la aplicación Template Method

# Comando por defecto
all: run

# Ejecutar el programa principal
run:
	python app/main.py

# Ejecutar los tests con pytest
test:
	pytest tests/test_build_house.py

# Limpiar archivos .pyc y __pycache__
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -r {} +

.PHONY: all run test clean
