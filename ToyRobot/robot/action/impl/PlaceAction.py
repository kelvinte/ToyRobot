from constant.Face import Face
from robot.action.Action import Action


class PlaceAction(Action):
    def accept(self, state: dict):
        if (self._params[0] > int(self._params[2]) >= 0 and
                self._params[1] > int(self._params[3]) >= 0):
            state['x'] = int(self._params[2])
            state['y'] = int(self._params[3])
            state['f'] = Face[self._params[4].upper()]
