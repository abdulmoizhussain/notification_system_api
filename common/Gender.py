class Gender:
    Male = 0
    Female = 1

    @staticmethod
    def is_valid(gender_to_check: int):
        all_app_rolls = [getattr(Gender, attr) for attr in dir(Gender) if
                         not callable(getattr(Gender, attr)) and not attr.startswith("__")]
        return gender_to_check in all_app_rolls
