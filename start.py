from towel import server

class Signal(object):

    def __init__(self, identifier, handler):
        self.identifier = identifier
        self.handler = handler
        self.callbacks = []

    def attach(self, func):
        self.callbacks.append(func)
    
    def __call__(self, *args, **kwargs):
        print "Calling func with", args, kwargs

class LineAdded(Signal):
    pass

def lineAdded(handler, line):
    handler.all('lineAdded', line)


server.add_application("test")
server.add_server("lineAdded", LineAdded)
#server.add_application("chat")
#server.add_application("json_test")
server.start_server();
