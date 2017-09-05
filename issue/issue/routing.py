from example.consumers import ExampleConsumer
from channels.staticfiles import StaticFilesConsumer
from channels.routing import route


routes = [
    route('http.request', StaticFilesConsumer()),
    ExampleConsumer.as_route(path=r'^/example/stream/$'),
]
