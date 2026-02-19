from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import Annotated
from fastapi import Depends
#
# task_db={
#     1 : 'Great_Stone',
#     2 : 'Yandex_box',
# }

engine = create_async_engine('sqlite+aiosqlite:///tasks.bd')

new_session= async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_session():
    async with new_session() as session:
        yield session


