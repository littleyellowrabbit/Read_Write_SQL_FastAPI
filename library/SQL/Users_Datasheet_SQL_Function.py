import library.SQL.Datasheet_Format as Df
import library.Router.Router_Format as Rf
from sqlalchemy import select


async def create_users(data: Rf.Users,async_session) -> Df.User:
    if data.name.isalnum():
        new_users = Df.User()
        new_users.name = data.name
        new_users.age = data.age
        async_session.add(new_users)
        await async_session.commit()
        print("add")
        exc = select(Df.User).where(Df.User.name == data.name)
        result = await async_session.execute(exc)
        print("search")
        sql_data = result.scalars().first()
        return sql_data

    else:
        raise ValueError("name error")

async def search_users(user_name:str,async_session) -> Df.User:
    if user_name.isalnum():
        exc = select(Df.User).where(Df.User.name == user_name)
        result = await async_session.execute(exc)
        print("search")
        sql_data = result.scalars().first()
        return sql_data
    else:
        raise ValueError("name error")




""" # old version without depend
def create_users(data: Rf.Users):
    if data.name.isalnum():
        new_users = Df.User()
        new_users.name = data.name
        new_users.age = data.age
        try:
            with local_session() as session:
                try:
                    session.add(new_users)
                    session.commit()
                    print("add")
                except Exception as e:
                    session.rollback()
                    raise e
        except Exception as conn_err:
            raise conn_err
    else:
        raise ValueError("name error")
"""