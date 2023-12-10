from fastapi import FastAPI, Response, Path, Query, Body, Header
from fastapi.responses import HTMLResponse
from users.users import users_router
app = FastAPI()

app.include_router(users_router)

@app.get('/', response_class=HTMLResponse)
def f_str():
    return "<b> Hello, User! </b>"








