import sdl2.ext
import sdl2.sdlgfx
import sdl2.events
import ctypes


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = sdl2.ext.Window("Frisky Graphics", size=(width, height))
        self.window.show()

    def update(self):
        sdl2.ext.fill(self.window.get_surface(), (0, 0, 0))
        self.window.refresh()

    def load(self, image_path):
        surface = sdl2.ext.load_image(image_path)
        sdl2.sdlgfx.rotozoomSurface(surface, 0, 1, sdl2.sdlgfx.SMOOTHING_ON)
        self.window.get_surface().blit(surface, dest=(0, 0))
        sdl2.SDL_FreeSurface(surface)

    def exit(self):
        sdl2.ext.quit()


class Sound:
    def __init__(self, sound_path):
        self.sound = sdl2.ext.AudioStream.open(sound_path)

    def play(self):
        self.sound.play()


def screen_create(width, height):
    return Screen(width, height)


def sound_load(sound_path):
    return Sound(sound_path)


def text_render(font_path, text, size, x, y, r, g, b):
    font_manager = sdl2.ext.FontManager(font_path, size=size)
    font_surface = font_manager.render(text, fgcolor=(r, g, b))
    texture = sdl2.ext.Texture(sdl2.SDL_CreateTextureFromSurface(font_manager.renderer, font_surface))
    sdl2.SDL_FreeSurface(font_surface)
    sdl2.SDL_RenderCopy(font_manager.renderer, texture, None, sdl2.rect.SDL_Rect(x, y, 0, 0))
    sdl2.SDL_DestroyTexture(texture)


def event_get_type():
    event = sdl2.SDL_Event()
    if sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_KEYDOWN:
            return "key_down"
        elif event.type == sdl2.SDL_KEYUP:
            return "key_up"
        elif event.type == sdl2.SDL_QUIT:
            return "quit"
    return ""


def event_get_key():
    event = sdl2.SDL_Event()
    if sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_KEYDOWN or event.type == sdl2.SDL_KEYUP:
            return chr(event.key.keysym.sym)
    return ""


def event_get_exit():
    event = sdl2.SDL_Event()
    if sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            return True
    return False
