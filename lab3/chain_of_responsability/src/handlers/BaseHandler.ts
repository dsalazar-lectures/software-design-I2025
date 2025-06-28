import { Request } from '../models/Request';
import { Handler } from './Handler';

// Clase base abstracta que implementa la interfaz Handler y proporciona funcionalidad común
export abstract class BaseHandler implements Handler {
    private nextHandler: Handler | null = null;

    // Establece el siguiente handler en la cadena y devuelve ese handler
    public setNext(handler: Handler): Handler {
        this.nextHandler = handler;
        return handler;
    }

    // Método para manejar la solicitud, implementa el template method pattern
    public handle(request: Request): void {
        // Si este handler puede manejar la solicitud, lo hace
        if (this.canHandle(request)) {
            this.processRequest(request);
        } 
        // Si no puede manejar la solicitud y hay un siguiente handler, pasa la solicitud
        else if (this.nextHandler !== null) {
            console.log(`Pasando la solicitud al siguiente handler...`);
            this.nextHandler.handle(request);
        } 
        // Si no hay siguiente handler, la solicitud no puede ser manejada
        else {
            console.log(`No se pudo manejar la solicitud: ${request.description}`);
        }
    }

    // Método abstracto que determina si este handler puede manejar la solicitud
    protected abstract canHandle(request: Request): boolean;

    // Método abstracto para procesar la solicitud
    protected abstract processRequest(request: Request): void;
}
