import board,busio
from time import sleep
from adafruit_st7735r import ST7735R
import displayio

mosi_pin = board.GP11
clk_pin = board.GP10
reset_pin = board.GP17
cs_pin = board.GP18
dc_pin = board.GP16

displayio.release_displays()
spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)
display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)
display = ST7735R(display_bus, width=128, height=160, bgr = True)

Nixie_0 = displayio.OnDiskBitmap("/b00.bmp")
Nixie_1 = displayio.OnDiskBitmap("/b01.bmp")
Nixie_2 = displayio.OnDiskBitmap("/b02.bmp")
Nixie_3 = displayio.OnDiskBitmap("/b03.bmp")
Nixie_4 = displayio.OnDiskBitmap("/b04.bmp")
Nixie_5 = displayio.OnDiskBitmap("/b05.bmp")
Nixie_6 = displayio.OnDiskBitmap("/b06.bmp")
Nixie_7 = displayio.OnDiskBitmap("/b07.bmp")
Nixie_8 = displayio.OnDiskBitmap("/b08.bmp")
Nixie_9 = displayio.OnDiskBitmap("/b09.bmp")

group = displayio.Group()
display.show(group)

while True:
    #tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
    tile_grid = displayio.TileGrid(Nixie_0, pixel_shader=Nixie_0.pixel_shader)
    group.append(tile_grid)
    display.show(group)
    sleep(3)
    group.remove(tile_grid)
    sleep(.1)
    
    tile_grid = displayio.TileGrid(Nixie_1, pixel_shader=Nixie_0.pixel_shader)
    group.append(tile_grid)
    display.show(group)
    sleep(3)
    group.remove(tile_grid)
    sleep(.1)

    tile_grid = displayio.TileGrid(Nixie_2, pixel_shader=Nixie_0.pixel_shader)
    group.append(tile_grid)
    display.show(group)
    sleep(3)
    group.remove(tile_grid)
    sleep(.1)    

    tile_grid = displayio.TileGrid(Nixie_3, pixel_shader=Nixie_0.pixel_shader)
    group.append(tile_grid)
    display.show(group)
    sleep(3)
    group.remove(tile_grid)
    sleep(.1)
    
    tile_grid = displayio.TileGrid(Nixie_4, pixel_shader=Nixie_0.pixel_shader)
    group.append(tile_grid)
    display.show(group)
    sleep(3)
    group.remove(tile_grid)
    sleep(.1)
    
    tile_grid = displayio.TileGrid(Nixie_5, pixel_shader=Nixie_0.pixel_shader)
    group.append(tile_grid)
    display.show(group)
    sleep(3)
    group.remove(tile_grid)
    sleep(.1)
    
    tile_grid = displayio.TileGrid(Nixie_6, pixel_shader=Nixie_0.pixel_shader)
    group.append(tile_grid)
    display.show(group)
    sleep(3)
    group.remove(tile_grid)
    sleep(.1)
    
    tile_grid = displayio.TileGrid(Nixie_7, pixel_shader=Nixie_0.pixel_shader)
    group.append(tile_grid)
    display.show(group)
    sleep(3)
    group.remove(tile_grid)
    sleep(.1)
    
    tile_grid = displayio.TileGrid(Nixie_8, pixel_shader=Nixie_0.pixel_shader)
    group.append(tile_grid)
    display.show(group)
    sleep(3)
    group.remove(tile_grid)
    sleep(.1)
    
    tile_grid = displayio.TileGrid(Nixie_9, pixel_shader=Nixie_0.pixel_shader)
    group.append(tile_grid)
    display.show(group)
    sleep(3)
    group.remove(tile_grid)
    sleep(.1)       