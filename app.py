import json
import math

from aiohttp import web


routes = web.RouteTableDef()


@routes.post("/pressure")
async def pressure(request):
    data = await request.json()
    temperature = float(data["temperature"])
    measured_pressure = float(data["pressure"])
    height = float(data["height"])
    temperature_gradient = 0.0065
    temperature_kelvin = temperature + 273.15
    result = measured_pressure / math.pow((1-temperature_gradient*height/temperature_kelvin), (0.03416/temperature_gradient))
    response_obj = {"pressure": result}
    return web.Response(text=json.dumps(response_obj))

app = web.Application()
app.router.add_routes(routes)

web.run_app(app)
