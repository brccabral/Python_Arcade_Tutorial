import arcade

# physics
MOVEMENT_SPEED = 8
JUMP_SPEED = 28
GRAVITY = 1.1

# map
TILE_WIDTH = 64
MAP_WIDTH = 60 * TILE_WIDTH
MAP_HEIGHT = 6 * TILE_WIDTH

# window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 896
WINDOW_HALF_WIDTH = WINDOW_WIDTH // 2


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BLACK)

        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("character.png")
        self.player_sprite.center_x = TILE_WIDTH // 2
        self.player_sprite.center_y = TILE_WIDTH * 2
        self.player_list.append(self.player_sprite)
        self.physics_engine = None
        self.camera = None

        self.collected_coins = 0

        self.setup()

    def setup(self):
        my_map = arcade.TileMap("my-map.tmx")
        self.scene = arcade.Scene.from_tilemap(my_map)
        self.scene.add_sprite("Player", self.player_sprite)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.scene["ground"], gravity_constant=GRAVITY
        )

    def on_draw(self):
        self.clear()
        self.scene.draw()
        arcade.draw_text(
            f"Coins: {self.collected_coins}",
            arcade.get_viewport()[0] + 10,
            arcade.get_viewport()[2] + WINDOW_HEIGHT - 50,
            arcade.color.GOLD,
            font_size=30,
        )

    def on_update(self, delta_time: float):
        self.physics_engine.update()
        # self.camera_position()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x -= MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x += MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x += MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x -= MOVEMENT_SPEED


MyGameWindow(WINDOW_WIDTH, WINDOW_HEIGHT, "My Game Window")
arcade.run()
