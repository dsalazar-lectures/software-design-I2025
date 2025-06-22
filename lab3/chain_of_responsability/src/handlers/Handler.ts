import { Request } from '../models/Request';

// Interfaz Handler que define los métodos que deben implementar todos los handlers
export interface Handler {
    setNext(handler: Handler): Handler;
    handle(request: Request): void;
}
