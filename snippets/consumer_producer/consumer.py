
class Consumer:
    ...


if __name__ == '__main__':
    consumer = Consumer()
    task = consumer.consume_tasks()
    task.start()
