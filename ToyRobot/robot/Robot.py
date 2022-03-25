from robot.action.impl.PlaceAction import PlaceAction
from robot.action.impl.MoveAction import MoveAction
from robot.action.impl.LeftAction import LeftAction
from robot.action.impl.RightAction import RightAction

class Robot():
    broadcaster = None

    state = {
        'x': None,
        'y': None,
        'f': None,
    }

    instructions = []
    board = [5, 5]
    _is_alive = True

    def __init__(self, broadcaster):
        self.broadcaster = broadcaster
        self.broadcaster.board = self.board

    async def _processV2(self, instruction):

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
            place_action.handle(state=self.state)

        if action.lower() == 'move':
            move_action = MoveAction()
            move_action.set_param(params=parameter)
            move_action.handle(state=self.state)


        if action.lower() == 'left':
            left_action = LeftAction()
            left_action.set_param(params=parameter)
            left_action.handle(state=self.state)


        if action.lower() == 'right':
            right_action = RightAction()
            right_action.set_param(params=parameter)
            right_action.handle(state=self.state)


        if action.lower() == 'report':
            if self.state['x'] is not None:
                result = str(self.state['x']) + ',' + str(self.state['y']) + ',' + str(self.state['f'].name)
                print(result)
                await self.broadcaster.broadcast(result)

