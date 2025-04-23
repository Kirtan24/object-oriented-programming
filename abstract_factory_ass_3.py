from abc import ABC, abstractmethod

class Behaviour(ABC):
    @abstractmethod
    def permission(self):
        pass

class AdminBehaviour(Behaviour):
    def permission(self):
        return "Admin: has all permissions"

class ManagerBehaviour(Behaviour):
    def permission(self):
        return "Manager: has some permissions"

class EmployeeBehaviour(Behaviour):
    def permission(self):
        return "Employee: has limited permissions"

class User(ABC):
    def __init__(self, behavior: Behaviour):
        self._behavior = behavior

    def set_behavior(self, behavior:Behaviour):
        self._behavior = behavior

    def get_permissions(self):
        return self._behavior.permission()


class Admin(User):
    def __init__(self):
        super().__init__(AdminBehaviour())

class Manager(User):
    def __init__(self):
        super().__init__(ManagerBehaviour())

class Employee(User):
    def __init__(self):
        super().__init__(EmployeeBehaviour())

class UserFactory(ABC):
    @staticmethod
    def create_user(user_type):
        if user_type == "admin":
            return Admin()
        elif user_type == "manager":
            return Manager()
        elif user_type == "employee":
            return Employee()
        else:
            return None

def main():
    print("-----------Admin-----------")
    user1 = UserFactory.create_user("admin")
    print(user1.get_permissions())
    print("-----------Admin-----------")

    print()
    print()

    print("-----------Manager-----------")
    user2 = UserFactory.create_user("manager")
    print(user2.get_permissions())
    print("Promotting Manager to Admin")
    user2.set_behavior(AdminBehaviour())
    print(user2.get_permissions())
    print("-----------Manager-----------")

    print()
    print()

    print("-----------Employee-----------")
    user3 = UserFactory.create_user("employee")
    print(user3.get_permissions())
    print("-----------Employee-----------")

if __name__ == "__main__":
    main()