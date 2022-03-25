from constant.Face import Face
from robot.action.Action import Action


class MoveAction(Action):
    def accept(self, state: dict):
        f = state['f']
        if f == Face.NORTH and self._params[1] > state['y'] + 1:
            state['y'] = state['y'] + 1
        if f == Face.SOUTH and state['y']-1 >= 0:
            state['y'] = state['y'] - 1
        if f == Face.EAST and self._params[0] > state['x'] + 1:
            state['x'] = state['x'] + 1
        if f == Face.WEST and state['x']-1 >=0:
            state['x'] = state['x'] - 1
