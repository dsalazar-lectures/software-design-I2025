class FormularioMediator {
  constructor() {
    this.componentes = {};
  }

  // Método para registrar componentes en el mediador
  registrar(nombre, componente) {
    this.componentes[nombre] = componente;
  }

  // Método para notificar eventos a los componentes y coordinar la interacción entre ellos
  notify(origen, evento) {
    if (origen === "nombre" && evento === "input") {
      const texto = this.componentes["nombre"].valor.trim();
      this.componentes["boton"].habilitar(texto !== "");
    }
    
    // Si se hace clic en el botón, se envía la solicitud al servidor
    if (origen === "boton" && evento === "click") {
      this.componentes["mensaje"].mostrar("Enviando...");
      this.componentes["boton"].deshabilitar();

      fetch("http://localhost:5000/enviar", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ nombre: this.componentes["nombre"].valor })
      })
        .then(async res => {
          const data = await res.json();
          if (!res.ok) {
            throw new Error(data.error || "Error desconocido");
          }
          this.componentes["mensaje"].mostrar(data.mensaje);
        })
        .catch(err => {
          this.componentes["mensaje"].mostrar(err.message);
        });
    }

    // Ejemplo de extensión: Si se hace clic en el botón de limpiar, se limpia el formulario
    if (origen === "limpiar" && evento === "click") {
      this.componentes["limpiar"].limpiar();
    }

  }
}

export default FormularioMediator;