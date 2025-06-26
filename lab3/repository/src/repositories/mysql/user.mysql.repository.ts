import mysql, { RowDataPacket } from 'mysql2/promise';
import { User } from "../../types/User";
import UserRepositoryInterface from "../base/user.repository.interface";
import dotenv from 'dotenv';

dotenv.config();

// DTOs
interface UserDTO extends RowDataPacket {
  id: string;
  name: string;
  mail: string;
  password: string;
}

interface CreateUserDTO {
  name: string;
  mail: string;
  password: string;
}

class UserMysqlRepository extends UserRepositoryInterface {
  private db?: mysql.Pool;

  constructor() {
    super();
    this.initializeConnection();
  }

  private async initializeConnection() {
    this.db = mysql.createPool(process.env.DATABASE_URL || "");
  }

  private toUser(dto: UserDTO): User {
    return {
      id: dto.id,
      name: dto.name,
      email: dto.mail,
      password: dto.password
    };
  }

  async findAll(): Promise<User[]> {
    if (!this.db) {
      throw new Error('Database connection not initialized');
    }
    try {
      const [rows] = await this.db.query<UserDTO[]>('SELECT name,id,mail,password FROM users');
      return rows.map(this.toUser);
      // return rows;
    } catch (error) {
      console.error('Error fetching users:', error);
      throw error;
    }
  }

}

export default UserMysqlRepository;
