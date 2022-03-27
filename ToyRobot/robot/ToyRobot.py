import robot.Robot


class ToyRobot(robot.Robot.Robot):

    async def start(self):
        print('Enter Commands (type stop to halt)')
        while self._is_alive:
            command = input()
            await self.processV2(command)
