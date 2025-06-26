import { Request, Response } from "express";
import UserModel from "../models/users.model";

class UsersController {
  static async findAll(req: Request, res: Response) {  
    const userModel = new UserModel();  
    const users = await userModel.findAll();
    res.json(users);
  }
}

export default UsersController;
