import Queue
from task import Task

class Payload():
    def __init__(self, target, payload_filename, extensions = [""]):
        self.queue = Queue.Queue()
        self.payload = ""
        with open(payload_filename) as payload:
            self.payload = payload.readlines()
            self.len = len(self.payload)
        #
        # TODO support for multiple extensions via generators
        #
        for resource in self.payload:
            resource = resource.replace('/', '')
            if not target[-1] == '/':
                target = target + '/'
            self.queue.put(Task(payload_filename, target, resource, extensions[0]))
