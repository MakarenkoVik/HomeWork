from aiohttp import web

async def handle(request):
    name = request.query.get('name', None)
    number_one, oprtr, number_two = name.split()
    number_one, number_two = float(number_one), float(number_two)
    operations = {
            "+": lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '/': lambda x, y: x / y,
            '*': lambda x, y: x * y,
            '**': lambda x, y: x ** y,
            '//': lambda x, y: x // y,
            '%': lambda x, y: x % y,
        }
    name = operations[oprtr](number_one, number_two)
    text = "Send, " + str(name)
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                         web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app, port=8787)
