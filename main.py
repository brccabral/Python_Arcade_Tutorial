import arcade


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BLACK)

        self.player_list = None
        self.player = None
        self.player_animation_speed = 120

        self.setup()

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player = arcade.AnimatedTimeBasedSprite()

        for r in range(4):
            for c in range(2):
                texture = arcade.load_texture(
                    "monster.png", x=c * 68, y=r * 64, width=68, height=64
                )
                self.player.append_texture(texture)
                a = arcade.AnimationKeyframe(
                    r * c, self.player_animation_speed, texture
                )
                self.player.frames.append(a)

        self.player.center_x = self.width // 2
        self.player.center_y = self.height // 2

        self.player_list.append(self.player)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()

    def on_update(self, delta_time: float):
        self.player_list.update_animation()


MyGameWindow(1280, 720, "My Game Window")
arcade.run()
