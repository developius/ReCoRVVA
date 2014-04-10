import dhtreader

type = 11
pin = 3

dhtreader.init()
print dhtreader.read(type, pin)
