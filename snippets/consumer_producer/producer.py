from .task import Task


class ConnectionTask(Task):
    def run(self, username: str, password: str):
        print('connecting with credentials: (%s/%s)' % (username, password))


if __name__ == '__main__':
    task = ConnectionTask(username=truc, password=truc)

"""
------------------------
|      Producer        |
------------------------
- Send task data to broker (state=created)

------------------------
|      Consumer        |
------------------------
- Pick task data from broker (with previously generated ID)
- Instanciate task
- Run task
"""
