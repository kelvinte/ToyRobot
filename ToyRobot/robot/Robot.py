from robot.action.impl.PlaceAction import PlaceAction
from robot.action.impl.MoveAction import MoveAction
from robot.action.impl.LeftAction import LeftAction
from robot.action.impl.RightAction import RightAction

class Robot():
    broadcaster = None

    _state = {
        'x': None,
        'y': None,
        'f': None,
    }

    instructions = []
    board = [5, 5]
    _is_alive = True

    def __init__(self, broadcaster):
        self.broadcaster = broadcaster
        if self.broadcaster is not None:
            self.broadcaster.board = self.board

    def get_state(self):
        return self._state

    async def processV2(self, instruction):

        instruct_arr = instruction.split(" ")
        action = instruct_arr[0]
        parameter = []
        parameter.extend(self.board)

        if len(instruct_arr) == 2:
            parameter.extend(instruct_arr[1].split(","))

        if action.lower() == 'stop':
            self._is_alive = False
            self.broadcaster.close()

        if action.lower() == 'place':
            place_action = PlaceAction()
            place_action.set_param(params=parameter)
            place_action.handle(state=self._state)

        if action.lower() == 'move':
            move_action = MoveAction()
            move_action.set_param(params=parameter)
            move_action.handle(state=self._state)


        if action.lower() == 'left':
            left_action = LeftAction()
            left_action.set_param(params=parameter)
            left_action.handle(state=self._state)


        if action.lower() == 'right':
            right_action = RightAction()
            right_action.set_param(params=parameter)
            right_action.handle(state=self._state)


        if action.lower() == 'report':
            if self._state['x'] is not None:
                result = str(self._state['x']) + ',' + str(self._state['y']) + ',' + str(self._state['f'].name)
                print(result)
                if self.broadcaster is not None:
                    await self.broadcaster.broadcast(result)

