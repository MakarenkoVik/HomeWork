#!/usr/bin/python3
import aiohttp
import asyncio
import time

async def main():
    async with aiohttp.ClientSession() as session:
        while session:
            data = input("Type an operation of two numbers and an operator between them: ")
            data_url = f'http://127.0.0.1:8787'
            async with session.get(data_url, params={'name': data}) as resp:
                data1 = await resp.text()
                print(data1)

asyncio.run(main())
