import asyncio

from core.Broadcaster import Broadcaster
from robot.ToyRobot import ToyRobot

if __name__ == '__main__':
    broadcaster = Broadcaster()
    broadcaster.start()

    main = ToyRobot(broadcaster)
    asyncio.run(main.start())