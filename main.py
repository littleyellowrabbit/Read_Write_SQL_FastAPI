"""
Last Update Date:20260804
Python Version:3.14.5
Project Name:Read Write SQL.
Project Description:
    1.Try to simple project and learn simple FastAPI/Godot/postGreSQL function.
        1.FastAPI:Get/Post/ConfigParser/Async/APIRouter.
        2.SQL:SQLAlchemy/SQLAlchemy.Orm.
        3.Godot:Fundamental show result and button with action.
    2.Test to run in Linux by WSL Ubuntu and UI program in local.
    3.Deploy software using Docker.
"""
from fastapi import FastAPI
from contextlib import asynccontextmanager
from library.Router.Users import users as users_router
from library.SQL.Initialize_Table import engine,init_datasheet, init_sql_parameter
import uvicorn
import multiprocessing


@asynccontextmanager
async def lifespan(fastapi_app:FastAPI):
    print(fastapi_app)
    print("Start lifespan")
    print("Start init_sql_parameter")
    await init_sql_parameter()
    print("Start init_datasheet")
    await init_datasheet()
    yield
    if engine:
        await engine.dispose()


app = FastAPI(lifespan = lifespan)
print("Start")
app.include_router(users_router)

# use docker this would not execute.
if __name__ == "__main__":
    #Prevent Windows exe bug
    multiprocessing.freeze_support()

    uvicorn.run(app, host="0.0.0.0", port=8000)



















