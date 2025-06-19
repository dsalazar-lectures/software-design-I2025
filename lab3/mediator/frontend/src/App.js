import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect, useRef } from "react";
import FormularioMediator from "./Mediator";

function App() {
  const [valor, setValor] = useState("");
  const [habilitado, setHabilitado] = useState(false);
  const [mensaje, setMensaje] = useState("");

  const mediator = useRef(new FormularioMediator());

  // Registra los componentes en el mediador al montar el componente
  useEffect(() => {
    // Registra el input para el nombre
    mediator.current.registrar("nombre", {
      valor,
    });

    // Registra el botón
    mediator.current.registrar("boton", {
      habilitar: (val) => setHabilitado(val),
      deshabilitar: () => setHabilitado(false)
    });

    // Registra el mensaje
    mediator.current.registrar("mensaje", {
      mostrar: setMensaje
    });

    // Ejemplo de extensión: registrar una función para limpiar el formulario
    mediator.current.registrar("limpiar", {
      limpiar: () => {
        setValor("");
        setHabilitado(false);
        setMensaje("");
      }
    });


    // Registra la función para enviar el nombre al servidor
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

  // Maneja el input del usuario y notifica al mediador
  const handleInput = (e) => {
    setValor(e.target.value);
    mediator.current.componentes["nombre"].valor = e.target.value;
    mediator.current.notify("nombre", "input");
  };

  // Maneja el clic en el botón y notifica al mediador
  const handleClick = () => {
    mediator.current.notify("boton", "click");
  };

  // Ejemplo de extensión: manejar el clic en el botón de limpiar
  const handleClickLimpiar = () => {
    mediator.current.notify("limpiar", "click");
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
      <button onClick={handleClickLimpiar}>Limpiar</button>
      <p>{mensaje}</p>
    </div>
  );
}

export default App;
