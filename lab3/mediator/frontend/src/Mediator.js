class FormularioMediator {
  constructor() {
    this.componentes = {};
  }

  registrar(nombre, componente) {
    this.componentes[nombre] = componente;
  }

  notify(origen, evento) {
    if (origen === "nombre" && evento === "input") {
      const texto = this.componentes["nombre"].valor.trim();
      this.componentes["boton"].habilitar(texto !== "");
    }

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
  }
}

export default FormularioMediator;