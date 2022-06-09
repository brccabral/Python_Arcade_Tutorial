import arcade


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BLACK)

        self.ground_list = None

        self.setup()

    def setup(self):
        my_map = arcade.load_tilemap()

    def on_draw(self):
        arcade.start_render()

    def on_update(self, delta_time: float):
        pass


MyGameWindow(1280, 720, "My Game Window")
arcade.run()
