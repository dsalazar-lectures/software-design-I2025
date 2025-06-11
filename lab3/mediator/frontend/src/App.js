import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect, useRef } from "react";
import FormularioMediator from "./Mediator";

function App() {
    const [valor, setValor] = useState("");
  const [habilitado, setHabilitado] = useState(false);
  const [mensaje, setMensaje] = useState("");

  const mediator = useRef(new FormularioMediator());

  useEffect(() => {
    mediator.current.registrar("nombre", {
      valor,
    });

    mediator.current.registrar("boton", {
      habilitar: (val) => setHabilitado(val),
      deshabilitar: () => setHabilitado(false)
    });

    mediator.current.registrar("mensaje", {
      mostrar: setMensaje
    });

    mediator.current.registrar("api", {
      enviar: (nombre) =>
        fetch("http://localhost:5000/enviar", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ nombre })
        })
        .then(async res => {
          const data = await res.json();
          if (!res.ok) {
            throw new Error(data.error || "Error desconocido");
          }
          return data;
        })
        .catch(err => {
          this.componentes["mensaje"].mostrar(err.message);
        })
    });
  }, [valor]);

  const handleInput = (e) => {
    setValor(e.target.value);
    mediator.current.componentes["nombre"].valor = e.target.value;
    mediator.current.notify("nombre", "input");
  };

  const handleClick = () => {
    mediator.current.notify("boton", "click");
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h2>Formulario con Mediator (React + Flask)</h2>
      <input
        type="text"
        value={valor}
        onChange={handleInput}
        placeholder="Tu nombre"
      />
      <button onClick={handleClick} disabled={!habilitado}>Enviar</button>
      <p>{mensaje}</p>
    </div>
  );
}

export default App;
