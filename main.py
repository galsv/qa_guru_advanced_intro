import uvicorn
from fastapi_server.server import app

uvicorn.run(app, host='127.0.0.1', port=8002)
