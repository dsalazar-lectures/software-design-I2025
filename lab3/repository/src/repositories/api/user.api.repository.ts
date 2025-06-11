import axios, { AxiosInstance } from "axios";
import { User } from "../../types/User";
import UserRepositoryInterface from "../base/user.repository.interface";

// DTOs
interface UserApiDTO {
  id: {
    value: string;
  };
  name: {
    first: string;
    last: string;
  };
  email: string;
  login: {
    password: string;
  };
}



class UserApiRepository extends UserRepositoryInterface {
  private db: AxiosInstance;
  
  constructor() {
    super();
    this.db = axios.create({
      baseURL: "https://randomuser.me/api/",
    });
  }

  private toUser(dto: UserApiDTO): User {
    return {
      id: dto.id.value,
      name: `${dto.name.first} ${dto.name.last}`,
      email: dto.email,
      password: dto.login.password
    };
  }

  async findAll(): Promise<User[]> {
    const response = await this.db.get<{ results: UserApiDTO[] }>("/");
    return response.data.results.map(this.toUser);
    // return response.data.results;
  }
}

export default UserApiRepository;
