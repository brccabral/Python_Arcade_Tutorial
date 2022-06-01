import arcade


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BLACK)

        self.circle_x = 100
        self.circle_y = 100
        self.circle_r = 50
        self.x_speed = 300
        self.y_speed = 150

        self.player_x = 100
        self.player_y = 200
        self.player_speed = 250
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(
            self.circle_x,
            self.circle_y,
            self.circle_r,
            arcade.color.GREEN,
            num_segments=10,
        )
        arcade.draw_circle_outline(
            self.player_x, self.player_y, 50, arcade.color.BLUE, 2, num_segments=20
        )

    def on_update(self, delta_time):
        self.circle_x += self.x_speed * delta_time
        self.circle_y += self.y_speed * delta_time

        if (
            self.circle_x > self.width - self.circle_r
            or self.circle_x < 0 + self.circle_r
        ):
            self.x_speed *= -1
        if (
            self.circle_y > self.height - self.circle_r
            or self.circle_y < 0 + self.circle_r
        ):
            self.y_speed *= -1

        if self.right:
            self.player_x += self.player_speed * delta_time
        if self.left:
            self.player_x -= self.player_speed * delta_time
        if self.up:
            self.player_y += self.player_speed * delta_time
        if self.down:
            self.player_y -= self.player_speed * delta_time

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.right = True
        if symbol == arcade.key.LEFT:
            self.left = True
        if symbol == arcade.key.UP:
            self.up = True
        if symbol == arcade.key.DOWN:
            self.down = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.right = False
        if symbol == arcade.key.LEFT:
            self.left = False
        if symbol == arcade.key.UP:
            self.up = False
        if symbol == arcade.key.DOWN:
            self.down = False


MyGameWindow(1280, 720, "My Game Window")
arcade.run()
