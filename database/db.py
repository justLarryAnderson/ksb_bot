import asyncio
import asyncpg

class Database:
    def __init__(self):
        self.database = None

    async def insert_user_value(self, name: str, university: str):
        self.database = await asyncpg.connect(
            user = 'postgres', #имя пользователя postgres
            password='postgres',#пароль пользователя postgres
            database='ksb_tgbot_db',#имя базы данных в которой будет хранятся таблицы ksb_tgbot_db
            host='localhost',# сдесь локалхост но птом нужно поменять на IP localhost
            port=5432# Указать порт 5432
        )
        await self.database.execute(
            '''
            insert into users(name, university) values($1, $2)
            ''', name, university
        )
        await self.database.close()
