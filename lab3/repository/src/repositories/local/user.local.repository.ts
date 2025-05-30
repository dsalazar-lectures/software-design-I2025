import { User } from "../../types/User";
import UserRepositoryInterface from "../base/user.repository.interface";

class UserLocalRepository extends UserRepositoryInterface {
  constructor() {
    super();
  }

  async findAll(): Promise<User[]> {
    return [
      {
        id: "1",
        name: "John Doe",
        email: "john.doe@example.com",
        password: "123456",
      },
    ];
  }
}

export default UserLocalRepository;
