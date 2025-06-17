# Laboratorio 4: Pruebas Unitarias y CI/CD

## Funcionalidad Principal
**SousChef**: Servicio que ajusta automáticamente los tiempos de cocción basado en la cantidad de ingredientes.  
**Fórmula**: `tiempo_ajustado = tiempo_base * (1 + cantidad_ingredientes / 10)`

---

## Tests Implementados

### 1. `test_sous_chef_adjusts_time` (Test principal)
**Propósito**:  
Verifica que el `SousChef` ajuste correctamente el tiempo cuando hay ingredientes adicionales.

**Lógica verificada**:  
Con `tiempo_base = 10` y `1 ingrediente`, el tiempo ajustado debe ser `11.0 minutos` (10 * 1.1).

**Archivo**: `tests/test_sous_chef.py`
```python
def test_sous_chef_adjusts_time():
    fake_artifact = FakeArtifact()  # Simula un artefacto de cocina
    sous_chef = SousChef([fake_artifact])
    assert sous_chef.adjust_cooking_time(10, 1) == ["Cooked for 11.0 minutes"]
```

### 2. test_sous_chef_zero_ingredients (Test de borde)
**Propósito**:  
Valida que el `SousChef` mantenga el tiempo original cuando no hay ingredientes extra.

**Lógica verificada**:  
Con `tiempo_base = 10` y `0 ingredientes`, el tiempo debe permanecer en `10.0 minutos` (10 * 1.0).

**Archivo**: `tests/test_sous_chef_zero_ingredients.py`
```python
def test_sous_chef_zero_ingredients():
    artifact = FakeArtifact()
    sous_chef = SousChef([artifact])
    assert sous_chef.adjust_cooking_time(10, 0) == ["Cooked for 10.0 minutes"]
```

---

## Ejecución (desde directorio tests_example)
```bash
# Ejecutar todos los tests
pytest tests/ -v

# Ejecutar tests específicos
pytest tests/test_sous_chef.py -v
pytest tests/test_sous_chef_zero_ingredients.py -v
```