# Lab 3 - Josué Badilla
# Singleton software design pattern example.

class logger:
    __instance = None  # Static instance of the class logger.

    # Private constructor:
    def __init__(self):
        self.logs = []

    @staticmethod
    def get_instance():
        if logger.__instance is None:
            logger.__instance = logger()  # Call private constructor.

        else:
            print("Singleton class, just 1 instance can be created.\n")  # TEST

        return logger.__instance

    def log_event(self, message):
        self.logs.append(f"EVENT: {message}")
        print(f"EVENT: {message}\n")  # TEST


# Example:
if __name__ == "__main__":
    print("Loggger 1 creating instance:");
    logger_1 = logger.get_instance()
    logger_1.log_event("User 'chiki_69' started a new session.")

    # Try to create another new log class instance:
    print("Loggger 2 creating instance:");
    logger_2 = logger.get_instance()

    # Compare instances:
    print("Loggger 3 creating instance:");
    logger_3 = logger.get_instance()
    print("¿Same instance?", logger_1 is logger_3)  # TEST
