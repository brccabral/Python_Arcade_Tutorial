import arcade


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BLACK)

        self.player_x = 100
        self.player_y = 200
        self.player_speed = 250

        self.sprite1 = arcade.Sprite(
            "ship1a.png", center_x=self.player_x, center_y=self.player_y
        )
        self.sprite2 = arcade.Sprite("smile.png", center_x=200, center_y=200)
        self.sprite3 = arcade.Sprite("ufo.png", center_x=300, center_y=300)

        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self.sprite1)
        self.sprite_list.append(self.sprite2)
        self.sprite_list.append(self.sprite3)

        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def on_draw(self):
        arcade.start_render()
        # self.sprite1.draw()
        # self.sprite2.draw()
        # self.sprite3.draw()
        self.sprite_list.draw()

    def on_update(self, delta_time: float):
        if self.right:
            self.sprite1.turn_right(2)
        if self.left:
            self.sprite1.turn_left(2)
        # strafe applies a force on the player direction
        #  player doesn't stop when the key is released
        if self.up:
            self.sprite1.strafe(0.1)
        if self.down:
            self.sprite1.strafe(-0.1)

        # when using strafe, must call update
        # self.sprite1.update()
        self.sprite_list.update()

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
