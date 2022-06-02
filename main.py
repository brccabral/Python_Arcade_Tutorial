import arcade


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BLACK)

        self.player_list = None
        self.player = None
        self.player_animation_speed = 15

        self.setup()

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player = arcade.AnimatedWalkingSprite()

        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture("Run (1).png"))

        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(
            arcade.load_texture("Run (1).png", mirrored=True)
        )

        self.player.walk_right_textures = []
        for i in range(1, 9):
            self.player.walk_right_textures.append(
                arcade.load_texture(f"Run ({i}).png")
            )

        self.player.walk_left_textures = []
        for i in range(1, 9):
            self.player.walk_left_textures.append(
                arcade.load_texture(f"Run ({i}).png", mirrored=True)
            )

        self.player.center_x = self.width // 2
        self.player.center_y = self.height // 2

        self.player.scale = 0.5

        self.player_list.append(self.player)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()

    def on_update(self, delta_time: float):
        self.player_list.update()
        self.player_list.update_animation()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.player.change_x += self.player_animation_speed
        if symbol == arcade.key.LEFT:
            self.player.change_x -= self.player_animation_speed
        if symbol == arcade.key.UP:
            self.player.change_y += self.player_animation_speed
        if symbol == arcade.key.DOWN:
            self.player.change_y -= self.player_animation_speed

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.player.change_x -= self.player_animation_speed
        if symbol == arcade.key.LEFT:
            self.player.change_x += self.player_animation_speed
        if symbol == arcade.key.UP:
            self.player.change_y -= self.player_animation_speed
        if symbol == arcade.key.DOWN:
            self.player.change_y += self.player_animation_speed


MyGameWindow(1280, 720, "My Game Window")
arcade.run()
