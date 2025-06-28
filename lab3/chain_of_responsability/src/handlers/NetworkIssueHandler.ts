import { Request } from '../models/Request';
import { BaseHandler } from './BaseHandler';

// Handler concreto para problemas de red
export class NetworkIssueHandler extends BaseHandler {
    protected canHandle(request: Request): boolean {
        return request.type === 'NETWORK';
    }

    protected processRequest(request: Request): void {
        console.log(`NetworkIssueHandler: Resolviendo problema de red: ${request.description}`);
        // Lógica para resolver problemas de red
    }
}
