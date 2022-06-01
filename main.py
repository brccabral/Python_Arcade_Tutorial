import arcade


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()


MyGameWindow(1280, 720, "My Game Window")
arcade.run()
