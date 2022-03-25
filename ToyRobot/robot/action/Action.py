from core.Broadcaster import Broadcaster

class Action:

    _params = []

    def set_param(self, params):
        self._params = params

    def handle(self, state: dict):
        self.accept(state=state)

    def accept(self, state: dict):
        pass
