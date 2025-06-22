import { Request } from '../models/Request';
import { Handler } from '../handlers/Handler';

// Cliente que utiliza la cadena de handlers
export class Client {
    private handler: Handler;

    constructor(handler: Handler) {
        this.handler = handler;
    }

    // Método para enviar una solicitud a través de la cadena
    public sendRequest(request: Request): void {
        console.log(`\nCliente enviando solicitud: ${request.description} (Tipo: ${request.type})`);
        this.handler.handle(request);
    }
}
