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

        if self.circle_x > self.width or self.circle_x < 0:
            self.x_speed *= -1
        if self.circle_y > self.height or self.circle_y < 0:
            self.y_speed *= -1


MyGameWindow(1280, 720, "My Game Window")
arcade.run()
