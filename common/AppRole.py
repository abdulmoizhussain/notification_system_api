class AppRole:
    Admin = 0
    Teacher = 1
    Student = 2

    @staticmethod
    def is_valid(user_roll_to_check: int):
        all_app_rolls = [getattr(AppRole, attr) for attr in dir(AppRole) if
                         not callable(getattr(AppRole, attr)) and not attr.startswith("__")]
        return user_roll_to_check in all_app_rolls
