from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Annotated


class Users(BaseModel):
    id : Annotated[Optional[int],Field(ge=0)] = None
    name : Annotated[str,Field(min_length=1,max_length=20,pattern=r"^[a-zA-Z0-9]+$")] = None
    age : Annotated[int,Field(ge=0)]

    model_config = ConfigDict(from_attributes=True)
