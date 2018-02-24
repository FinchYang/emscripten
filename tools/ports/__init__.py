from . import binaryen, bullet, cocos2d, freetype, harfbuzz, libpng, ogg, sdl, sdl_image, sdl_ttf, sdl_net, vorbis, zlib

# If port A depends on port B, then A should be _after_ B
ports = [zlib, libpng, sdl, sdl_image, ogg, vorbis, bullet, freetype, harfbuzz, sdl_ttf, sdl_net, binaryen, cocos2d]

ports_by_name = {}
for port in ports:
  name = port.__name__.split('.')[-1]
  ports_by_name[name] = port

