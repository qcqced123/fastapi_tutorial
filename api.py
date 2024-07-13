from typing import Dict
from fastapi import FastAPI
from route_fn import router_fn

app = FastAPI()


# role of decorator is to bind the processing method to the route processing function
# in this case, the route processing function is set to "Get" method
@app.get("/")
async def welcome() -> Dict:
    """ function for Route processing """
    return {
        "message": "Hello, World!"
    }
app.include_router(router_fn)
