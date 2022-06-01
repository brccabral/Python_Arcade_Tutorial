import arcade


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BLACK)

        self.circle_x = 100
        self.circle_y = 100
        self.x_speed = 300
        self.y_speed = 150

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(
            self.circle_x, self.circle_y, 50, arcade.color.GREEN, num_segments=10
        )

    def on_update(self, delta_time):
        self.circle_x += self.x_speed * delta_time
        self.circle_y += self.y_speed * delta_time


MyGameWindow(1280, 720, "My Game Window")
arcade.run()
