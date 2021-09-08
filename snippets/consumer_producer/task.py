class Task:
    @classmethod
    def schedule(cls, **kwargs):
        """
        Run task with specified parameters
        """

    def run(self, **kwargs):
        """
        Method that defines processing that happens when Task.start() is called.
        """
        raise NotImplementedError("Your task must override Task.run() method.")

    def start(self):
        """
        Boilerplate to run tasks with error handling, logging, etc...
        """
        self.run()
