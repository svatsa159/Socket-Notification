from aiohttp import web
import socketio
import aiohttp_cors
import time
import redis
import pickle
r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    db=2
    )

# creates a new Async Socket IO Server
sio = socketio.AsyncServer()
# Creates a new Aiohttp Web Application
app = web.Application()
# Binds our Socket.IO server to our Web App
cors = aiohttp_cors.setup(app)

# instance
sio.attach(app)
sids=[]
# we can define aiohttp endpoints just as we normally
# would with no change
async def index(request):
    with open('index.html') as f:
        
        return web.Response(text=f.read(), content_type='text/html')
async def send_message(request):
    data = await request.json()
    
    message="Hey There"
    # side = r.get(data["user"])
    userid=data["user"]
    if(userid=="9999"):
        await sio.emit('message',data["message"])
    # print()
    else:
        side=pickle.loads(r.get(userid))
        await sio.emit('message',data["message"],room = side)
    return web.Response(text="Sent?")
@sio.on('connect')
async def connected(sid,env):
    print("open", sid)


@sio.on('message')
async def print_message(sid, message):

    print("Socket ID: " , sid)
    
    sids.append(sid)
    print(message)
@sio.on('user')
async def reg_user(sid,userid):
    print(type(sid))
    sids.append(sid)

    r.set(int(userid),pickle.dumps(sid))
@sio.on('disconnect')
async def closed(sid):
    print("closed", sid)
# We bind our aiohttp endpoint to our app
# router
app.router.add_get('/', index)
cors.add(app.router.add_post("/send_data",send_message), {
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers=("X-Custom-Server-Header",),
            allow_headers=("X-Requested-With", "Content-Type"),
            max_age=3600,
        )
    })

# app.router.add_get('/send_data', send_message)
app.router.add_static('/static/',path="./static/")

# We kick off our server
if __name__ == '__main__':
    r.flushdb()
    web.run_app(app)
