from fastapi import APIRouter, HTTPException, Depends, status
import library.Router.Router_Format as Rf
import library.SQL.Initialize_Table as It
import library.SQL.Users_Datasheet_SQL_Function as Users_SQL_Func
#from typing import Optional



users = APIRouter(prefix = "/users",tags = ["Users_information"])



@users.post("/create",response_model=Rf.Users,status_code=status.HTTP_201_CREATED)
async def create_user(data: Rf.Users, async_session = Depends(It.get_db_session)) -> Rf.Users:
    try:
        result = await Users_SQL_Func.create_users(data,async_session)
        model_data = Rf.Users.model_validate(result)
        return model_data
    except Exception as e:
        raise HTTPException(status_code=400, detail= str(e))

@users.get("/search",response_model=Rf.Users,status_code=status.HTTP_200_OK)
async def search_user(search_name: str, async_session = Depends(It.get_db_session)) -> Rf.Users:
    try:
        result = await Users_SQL_Func.search_users(search_name,async_session)
        model_data = Rf.Users.model_validate(result)
        return model_data
    except Exception as e:
        raise HTTPException(status_code=404, detail= str(e))


""" # old version without depend
@users.post("")
def create_user(data: Rf.Users):
    try:
        Users_SQL_Func.create_users(data)
        return "Create Successfully"
    except Exception as e:
        raise HTTPException(status_code=400, detail= str(e))
"""