import sdl2
import sdl2.ext


class GUI:
    def __init__(self):
        # Setup GUI
        sdl2.ext.init()
        self.window = sdl2.ext.Window("Sensor", size=(1920, 1080), flags=sdl2.SDL_WINDOW_FULLSCREEN)
        self.font_manager = sdl2.ext.FontManager(font_path='fonts/OpenSans-Regular.ttf', size=90)
        self.renderer = sdl2.ext.Renderer(self.window)
        self.factory = sdl2.ext.SpriteFactory(renderer=self.renderer)
        self.window.show()
        sdl2.SDL_ShowCursor(0)

    def render_string(self, output, x_pos=0, y_pos=0):
        self.renderer.clear(sdl2.ext.Color(0, 0, 0))
        text = self.factory.from_text(output, fontmanager=self.font_manager)
        self.renderer.copy(text, dstrect=(x_pos, y_pos, text.size[0], text.size[1]))
        self.renderer.present()
