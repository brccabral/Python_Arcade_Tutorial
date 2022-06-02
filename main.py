import arcade


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BLACK)

        self.player_x = 100
        self.player_y = 200
        self.player_speed = 250

        self.sprite1 = arcade.Sprite("ship1a.png", center_x=self.player_x, center_y=self.player_y)

        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def on_draw(self):
        arcade.start_render()
        self.sprite1.draw()

    def on_update(self, delta_time: float):
        if self.right:
            self.player_x += self.player_speed * delta_time
        if self.left:
            self.player_x -= self.player_speed * delta_time
        if self.up:
            self.player_y += self.player_speed * delta_time
        if self.down:
            self.player_y -= self.player_speed * delta_time

        self.sprite1.set_position(self.player_x, self.player_y)

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
