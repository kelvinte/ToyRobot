from robot.action.Action import Action
from constant.Face import Face

class RightAction(Action):
    def accept(self, state: dict):
        f = state['f']
        if f == Face.NORTH:
            state['f'] = Face.EAST
        if f == Face.SOUTH:
            state['f'] = Face.WEST
        if f == Face.EAST:
            state['f'] = Face.SOUTH
        if f == Face.WEST:
            state['f'] = Face.NORTH
