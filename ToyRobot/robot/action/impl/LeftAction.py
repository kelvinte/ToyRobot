from robot.action.Action import Action
from constant.Face import Face


class LeftAction(Action):
    def accept(self, state: dict):
        f = state['f']
        if f == Face.NORTH:
            state['f'] = Face.WEST
        if f == Face.SOUTH:
            state['f'] = Face.EAST
        if f == Face.EAST:
            state['f'] = Face.NORTH
        if f == Face.WEST:
            state['f'] = Face.SOUTH
