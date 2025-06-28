# Importaciones para que ´pytest pueda encontrar las clases a probar
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app.build_house_with_doors_entry import BuildHouseWithDoorsEntry
from app.build_house_with_garage_entry import BuildHouseWithGarageEntry

# Test para el paso de contrucción de la entrada de la casa con puertas
def test_build_entry_doors():
    house = BuildHouseWithDoorsEntry()
    step = house.buildEntry()
    assert step == "Construyendo la entrada principal de la casa con puertas"

# Test para el paso de contrucción de la entrada de la casa con garaje
def test_build_entry_garage():
    house = BuildHouseWithGarageEntry()
    step = house.buildEntry()
    assert step == "Construyendo la entrada principal de la casa con garaje"

# Test para la construcción completa de la casa con puertas
def test_build_house_with_doors_entry():
    house = BuildHouseWithDoorsEntry()
    steps = house.buildHouse()
    assert steps == [
        "Construyendo las paredes lisas de la casa",
        "Construyendo la entrada principal de la casa con puertas",
        "Instalando las ventanas de la casa",
        "Construyendo el techo trianguar de la casa"
    ]

# Test para la construcción completa de la casa con garaje
def test_build_house_with_garage_entry():
    house = BuildHouseWithGarageEntry()
    steps = house.buildHouse()
    assert steps == [
        "Construyendo las paredes lisas de la casa",
        "Construyendo la entrada principal de la casa con garaje",
        "Instalando las ventanas de la casa",
        "Construyendo el techo trianguar de la casa"
    ]

