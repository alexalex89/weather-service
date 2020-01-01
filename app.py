import json
import math

from aiohttp import web


async def handle(request):
    temperature = float(request.rel_url.query["temperature"])
    pressure = float(request.rel_url.query["pressure"])
    height = float(request.rel_url.query["height"])
    temperature_gradient = 0.0065
    temperature_kelvin = temperature + 273.15
    result = pressure / math.pow((1-temperature_gradient*height/temperature_kelvin), (0.03416/temperature_gradient))
    response_obj = {"pressure": result}
    return web.Response(text=json.dumps(response_obj))

app = web.Application()
app.router.add_get('/pressure', handle)

web.run_app(app)
