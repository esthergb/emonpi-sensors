import asyncio

import emonpi_sensors


def handle_sensors_update(message):
    print(message)

loop = asyncio.get_event_loop()
sensors = emonpi_sensors.EmonPiSensors('/dev/ttyAMA0', loop)
sensors.handler_sensors_update = handle_sensors_update
sensors.connect()
loop.run_forever()
loop.close()
