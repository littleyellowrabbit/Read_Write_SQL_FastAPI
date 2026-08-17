from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession, AsyncEngine
from library.File.Config_Operate import read_sql_user_data
import library.SQL.Datasheet_Format as Df
from typing import Optional

local_session: Optional[async_sessionmaker] = None
engine: Optional[AsyncEngine] =None

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    global local_session
    async with local_session() as session:
        yield session

async def init_datasheet()-> None:
    global engine
    async with engine.connect() as conn:
        async with conn.begin():
            await conn.run_sync(Df.SQLBase.metadata.create_all)
    print("Init_datasheet OK")


async def init_sql_parameter():
    sql_user, sql_password, sql_host, sql_database = read_sql_user_data()
    sql_url = f"postgresql+asyncpg://{sql_user}:{sql_password}@{sql_host}/{sql_database}"
    global engine
    engine = create_async_engine(sql_url,pool_size=5,max_overflow=5,pool_timeout=3,pool_pre_ping=True,pool_recycle=300)
    global local_session
    local_session = async_sessionmaker(bind=engine)





"""#None Async
sql_user, sql_password, sql_host, sql_database = read_sql_user_data()
sql_url = f"postgresql+psycopg2://{sql_user}:{sql_password}@{sql_host}/{sql_database}"
engine = create_engine(sql_url,pool_size=5,max_overflow=5,pool_timeout=3,pool_pre_ping=True,pool_recycle=300)
local_session = sessionmaker(bind=engine)
Df.SQLBase.metadata.create_all(engine)
print("Initialize_Table_OK")
"""
