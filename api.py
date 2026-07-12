import asyncio
import aiohttp


class Rick_And_Morty:

    URL = "https://rickandmortyapi.com/api"

    async def fetch_data(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.URL, ssl=False) as response:
                if response.status == 200:
                    data = await response.json()
                    return f"Полученные данные: {data}"
                else:
                    return f"Ошибка: {response.status}"

    async def get_character(self, id_character: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.URL}/character/{id_character}", ssl=False) as response:
                if response.status == 200:
                    data = await response.json()
                    return f"Имя: {data['info']['name']}\n"
                else:
                    return f"Ошибка: {response.status}"

    async def get_random_character(self):
        import random
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.URL}/character/", ssl=False) as response_total_character:
                if response_total_character.status == 200:
                    data = await response_total_character.json()
                    total = data["info"]["count"]
                    async with session.get(f"{self.URL}/character/{random.randint(1, total)}", ssl=False) as response:
                        if response.status == 200:
                            data = await response.json()
                            return data
                        else:
                            return f"Ошибка: {response.status}"
                else:
                    return f"Ошибка: {response_total_character.status}"

    async def search_by_name(self, name: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.URL}/character/?name={name}", ssl=False) as response:
                if response.status == 200:
                    data = await response.json()
                    return f"Полученные данные, {data}"
                else:
                    return f"Ошибка: {response.status}"

    async def search_by_status(self, status: str):

        valid_statuses = {"alive", "dead", "unknown"}
        staus_lower = status.lower()

        if staus_lower not in valid_statuses:
            return f"Неверный статус. Допустимые: {', '.join(valid_statuses)}"

        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.URL}/character/?status={staus_lower}", ssl=False) as response:
                if response.status == 200:
                    data = await response.json()
                    return f"Полученные данные, {data}"
                else:
                    return f"Ошибка: {response.status}"

