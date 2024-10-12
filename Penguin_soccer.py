from hub import port
import runloop
import force_sensor
import motor

async def main():
    while True:
        motor.run_for_degrees(port.A, -180, 1000)

        await runloop.until(lambda: force_sensor.pressed(port.B))

        if force_sensor.pressed(port.B) == True:
            motor.run_for_degrees(port.A, 360, 1000)

runloop.run(main())
