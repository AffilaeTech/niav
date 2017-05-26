from niav.utils import Utils


class ApiHello(object):

    def __init__(self, name="Anonymous"):
        self.name = name

    def hello(self):
        message = {
            "message": "Hello %s" % self.name,
            "name": self.name
        }
        return Utils.json_dump(message)
