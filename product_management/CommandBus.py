class CommandBus:
    def __init__(self):
        self.handlers = {}

    def register(self, command_type, handler):
        self.handlers[command_type] = handler

    def handle(self, command):
        handler = self.handlers[type(command)]
        handler.handle(command)
