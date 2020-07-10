class NotificationType:
    AllStudents = 0
    SpecificDepartment = 1
    SpecificStudent = 2

    @staticmethod
    def is_valid(notification_type_to_check: int):
        all_app_rolls = [getattr(NotificationType, attr) for attr in dir(NotificationType) if
                         not callable(getattr(NotificationType, attr)) and not attr.startswith("__")]
        return notification_type_to_check in all_app_rolls
