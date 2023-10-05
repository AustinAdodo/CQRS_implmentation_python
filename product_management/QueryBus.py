class QueryBus:
    def __init__(self):
        self.handlers = {}

    def register(self, query_type, handler):
        self.handlers[query_type] = handler

    def handle(self, query):
        handler = self.handlers[type(query)]
        return handler.handle(query)