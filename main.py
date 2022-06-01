import arcade


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BLACK)

        self.green_x = 100
        self.green_y = 100

        self.blue_x = 300
        self.blue_y = 300

        self.yellow_x = 500
        self.yellow_y = 500

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(
            self.green_x,
            self.green_y,
            50,
            arcade.color.GREEN,
            num_segments=20,
        )
        arcade.draw_circle_filled(
            self.blue_x,
            self.blue_y,
            50,
            arcade.color.BLUE,
            num_segments=20,
        )
        arcade.draw_circle_outline(
            self.yellow_x, self.yellow_y, 50, arcade.color.YELLOW, 2, num_segments=20
        )

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.green_x = x
            self.green_y = y
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.blue_x = x
            self.blue_y = y

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.yellow_x = x
        self.yellow_y = y


MyGameWindow(1280, 720, "My Game Window")
arcade.run()
