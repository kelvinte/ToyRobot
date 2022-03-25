import asyncio
import threading
import websockets


class Broadcaster(threading.Thread):
    clients = []
    board = []
    server_alive = True
    server_task = None

    stop_event = threading.Event()

    def run(self)-> None:
        asyncio.run(self.start_server())

    async def start_server(self):
        stop = asyncio.get_event_loop().run_in_executor(None, self.stop_event.wait)

        async with websockets.serve(self.handler, "localhost", 8765):
            await stop



    def setBoard(self, board):
        self.board = board

    async def handler(self, websocket):
        self.clients.append(websocket)
        while self.server_alive:
            message = await websocket.recv()
            if not self.server_alive:
                raise Exception("Server is now close")
            if message == 'retrieveGrid':
                await websocket.send("GRID:"+','.join(str(i) for i in self.board))

        # async for message in websocket:
        #     await websocket.send(message)


    def close(self):
        self.server_alive = False
        self.stop_event.set()



    async def broadcast(self, state):
        for ws in self.clients:
            await ws.send("STATE:"+state)


