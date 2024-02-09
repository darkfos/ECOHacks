from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(url="postgresql+psycopg2://{name}:{pass}@localhost/sqlalchemy_tuts")
async_session_db = async_sessionmaker(engine)


class PostBase(DeclarativeBase, AsyncAttrs):
    """
    Декларативный класс, необходим для наследования дочерных классов - (таблиц БД)
    """
    pass


#Подключение к БД, создание таблиц
async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(PostBase.metadata.create_all)