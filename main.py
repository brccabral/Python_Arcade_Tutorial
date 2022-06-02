import arcade


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BLACK)

        self.player_list = None
        self.player = None

        self.right = False
        self.left = False
        self.up = False
        self.down = False

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

        self.player_list.append(self.player)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()

    def on_update(self, delta_time: float):
        self.player_list.update_animation()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.left:
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
