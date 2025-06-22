import { Request } from './models/Request';
import { SoftwareIssueHandler } from './handlers/SoftwareIssueHandler';
import { HardwareIssueHandler } from './handlers/HardwareIssueHandler';
import { NetworkIssueHandler } from './handlers/NetworkIssueHandler';
import { Client } from './client/Client';

// Función principal para demostrar el patrón Chain of Responsibility
function main() {
    console.log("Demostración del Patrón Chain of Responsibility");
    console.log("----------------------------------------------");

    // Crear instancias de los handlers concretos
    const softwareHandler = new SoftwareIssueHandler();
    const hardwareHandler = new HardwareIssueHandler();
    const networkHandler = new NetworkIssueHandler();

    // Configurar la cadena de responsabilidad
    softwareHandler.setNext(hardwareHandler).setNext(networkHandler);

    // Crear cliente con el primer handler de la cadena
    const client = new Client(softwareHandler);

    // Crear algunas solicitudes de ejemplo
    const requests: Request[] = [
        { type: 'SOFTWARE', description: 'La aplicación se cierra inesperadamente' },
        { type: 'HARDWARE', description: 'La impresora no enciende' },
        { type: 'NETWORK', description: 'No hay conexión a internet' },
        { type: 'DATABASE', description: 'Error en la base de datos' }, // Este no será manejado por ningún handler
    ];

    // Enviar cada solicitud a través de la cadena
    requests.forEach(request => {
        client.sendRequest(request);
    });
}

// Ejecutar la demostración
main();
