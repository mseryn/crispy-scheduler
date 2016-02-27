def person():
    def __init__(self, name = "default person name", tasks = []):
        _name = name
        _tasks = tasks

    def get_name(self):
        return self._name

    def get_tasks(self):
        return self._tasks

    def set_name(self, name):
        self._name = name

    def overwrite_tasks(self, tasks):
        self._tasks = tasks

    def clear_tasks(self):
        self._tasks = []

    def add_tasks(self, tasks):
        for task in tasks:
            self._tasks.append(task)
