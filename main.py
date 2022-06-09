import arcade

# window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 896
WINDOW_HALF_WIDTH = WINDOW_WIDTH // 2


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BLACK)

        self.setup()

    def setup(self):
        my_map = arcade.TileMap("my-map.tmx")
        self.scene = arcade.Scene.from_tilemap(my_map)

    def on_draw(self):
        arcade.start_render()
        self.scene.draw()

    def on_update(self, delta_time: float):
        pass


MyGameWindow(WINDOW_WIDTH, WINDOW_HEIGHT, "My Game Window")
arcade.run()
