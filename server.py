
import asyncio
import websockets

import json
async def fetch_data():
    print('start fetching')
    await  asyncio.sleep(2)
    print('done fetching')
    return {'data':[1,2,3]}
async def print_numbers():
    l=[]
    for i in range(10):
        print(i)
        l.append(i)
        await asyncio.sleep(0.5)
    return {'numbers':l}

async def response(websocket, path):
	message = await websocket.recv()
	print(f"We got the message from the client: {message}")
	task1 = asyncio.create_task(fetch_data())
	task2 = asyncio.create_task(print_numbers())
	f1= await task1
	f2=await task2

	await websocket.send(json.dumps(f1))
	await websocket.send(json.dumps(f2))

start_server = websockets.serve(response, 'localhost', 1234)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()