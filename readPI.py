import gpiozero as g

reader = g.DigitalInputDevice(10)

print(reader.value())