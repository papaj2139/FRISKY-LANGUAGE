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


class Graphics:
    def __init__(self, window):
        self.renderer = sdl2.ext.Renderer(window)
        self.objects = []  # Store the created objects

    def draw_rect(self, color, rect):
        sdl2.ext.fill(self.renderer, color, rect)

    def destroy_object(self, object):
        if object in self.objects:
            self.objects.remove(object)

    def create_rect(self, color, rect):
        obj = {"type": "rect", "color": color, "rect": rect}
        self.objects.append(obj)

    def update(self):
        sdl2.ext.fill(self.renderer, (0, 0, 0))  # Clear the screen

        for obj in self.objects:
            if obj["type"] == "rect":
                sdl2.ext.fill(self.renderer, obj["color"], obj["rect"])

        self.renderer.present()


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
            key_code = event.key.keysym.sym
            if key_code == sdl2.SDLK_a:
                return "a"
            elif key_code == sdl2.SDLK_b:
                return "b"
            elif key_code == sdl2.SDLK_c:
                return "c"
            elif key_code == sdl2.SDLK_w:
                return "w"
            elif key_code == sdl2.SDLK_s:
                return "s"
            elif key_code == sdl2.SDLK_d:
                return "d"
            elif key_code == sdl2.SDLK_UP:
                return "up"
            elif key_code == sdl2.SDLK_DOWN:
                return "down"
            elif key_code == sdl2.SDLK_LEFT:
                return "left"
            elif key_code == sdl2.SDLK_RIGHT:
                return "right"
            elif key_code == sdl2.SDLK_1:
                return "1"
            elif key_code == sdl2.SDLK_2:
                return "2"
            elif key_code == sdl2.SDLK_3:
                return "3"
            elif key_code == sdl2.SDLK_SPACE:
                return "space"
            elif key_code == sdl2.SDLK_RETURN:
                return "enter"
            elif key_code == sdl2.SDLK_LSHIFT or key_code == sdl2.SDLK_RSHIFT:
                return "shift"
            elif key_code == sdl2.SDLK_LCTRL or key_code == sdl2.SDLK_RCTRL:
                return "ctrl"
            elif key_code == sdl2.SDLK_LALT or key_code == sdl2.SDLK_RALT:
                return "alt"
            elif key_code == sdl2.SDLK_TAB:
                return "tab"
    return ""


def event_get_exit():
    event = sdl2.SDL_Event()
    if sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            return True
    return False


def event_get_click_position():
    event = sdl2.SDL_Event()
    if sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
            return event.button.x, event.button.y
    return None


def event_get_touch_position():
    event = sdl2.SDL_Event()
    if sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_FINGERDOWN:
            return event.tfinger.x, event.tfinger.y
    return None


def create_graphics(window):
    return Graphics(window)
