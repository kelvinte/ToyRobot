from core.impl.StdinUserInputProcessor import StdinUserInputProcessor
import robot.Robot
from core.Broadcaster import Broadcaster
import asyncio


class Main(robot.Robot.Robot):

    inputProcessor = StdinUserInputProcessor()

    async def start(self):
        # print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
        # contents = self.inputProcessor.get_input()
        # # contents = ['PLACE 1,1,NORTH', 'MOVE', 'MOVE','MOVE', 'REPORT']
        # await self._process(contents)
        print('Enter Commands (type stop to halt)')
        while self._is_alive:
            command = input()
            await self._processV2(command)

if __name__ == '__main__':
    broadcaster = Broadcaster()
    broadcaster.start()

    main = Main(broadcaster)
    asyncio.run(main.start())