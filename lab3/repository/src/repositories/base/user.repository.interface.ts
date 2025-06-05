import { User } from "../../types/User";

class UserRepositoryInterface {
    /**
     * Find all users
     * @returns Promise<User[]>
     */
    findAll(): Promise<User[]> {
        throw new Error("Method not implemented.");
    }


    // create(user: User): Promise<User> {
    //     throw new Error("Method not implemented.");
    // }
    
    // findById(id: string): Promise<User> {
    //     throw new Error("Method not implemented.");
    // }

    // update(user: User): Promise<User> {
    //     throw new Error("Method not implemented.");
    // }

    // delete(id: string): Promise<void> {
    //     throw new Error("Method not implemented.");
    // }

}

export default UserRepositoryInterface;
