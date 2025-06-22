import { Request } from '../models/Request';
import { BaseHandler } from './BaseHandler';

// Handler concreto para problemas de software
export class SoftwareIssueHandler extends BaseHandler {
    protected canHandle(request: Request): boolean {
        return request.type === 'SOFTWARE';
    }

    protected processRequest(request: Request): void {
        console.log(`SoftwareIssueHandler: Resolviendo problema de software: ${request.description}`);
        // Lógica para resolver problemas de software
    }
}
