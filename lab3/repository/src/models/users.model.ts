import UserApiRepository from "../repositories/api/user.api.repository";
import UserRepositoryInterface from "../repositories/base/user.repository.interface";
import UserLocalRepository from "../repositories/local/user.local.repository";
import UserMysqlRepository from "../repositories/mysql/user.mysql.repository";

class UserModel {
  private userRepository: UserRepositoryInterface;

  constructor() {
    this.userRepository = new UserApiRepository();
  }

  async findAll() {
    const users = await this.userRepository.findAll();

    // ordenar por email alfabeticamente
    const orderedByEmail = users.sort((a, b) => {
      return a.email.localeCompare(b.email);
    });

    return orderedByEmail;
  }
}

export default UserModel;
