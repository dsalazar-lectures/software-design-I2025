import express, { Request, Response } from 'express';
import dotenv from 'dotenv';
import router from './router/router';
dotenv.config();

const app = express();
const port = process.env.PORT || 3000;

// Middleware
app.use(express.json());

// Routes
app.get('/', (req: Request, res: Response) => {
  res.json({ message: 'Welcome to Express + TypeScript API' });
});

app.use(router);

// Start server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
}); 