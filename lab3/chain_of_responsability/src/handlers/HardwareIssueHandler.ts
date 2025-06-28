import { Request } from '../models/Request';
import { BaseHandler } from './BaseHandler';

// Handler concreto para problemas de hardware
export class HardwareIssueHandler extends BaseHandler {
    protected canHandle(request: Request): boolean {
        return request.type === 'HARDWARE';
    }

    protected processRequest(request: Request): void {
        console.log(`HardwareIssueHandler: Resolviendo problema de hardware: ${request.description}`);
        // Lógica para resolver problemas de hardware
    }
}
