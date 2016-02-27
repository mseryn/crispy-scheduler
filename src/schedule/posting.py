def posting():
    def __init__(self, resources = [], tasks = []):
        _resources = []
        _tasks = []

    def get_resources(self):
        return self._resources

    def get_tasks(self):
        return self._tasks

    def overwrite_resources(self, resources):
        self._resources = resources

    def overwrite_tasks(self, tasks):
        self._tasks = tasks

    def clear_resources(self):
        self._resources = []

    def clear_tasks(self):
        self._tasks = []

    def add_resources(self, resources):
        for resource in resources:
            self._resources.append(resource)

    def add_tasks(self, tasks):
        for task in tasks:
            self._tasks.append(task)
