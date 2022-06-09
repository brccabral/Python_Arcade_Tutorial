import arcade

# physics
MOVEMENT_SPEED = 8
JUMP_SPEED = 28
GRAVITY = 1.1

# map
TILE_WIDTH = 64
HALF_TILE_WIDTH = TILE_WIDTH // 2
MAP_WIDTH = 60 * TILE_WIDTH
MAP_HEIGHT = 6 * TILE_WIDTH
MAX_PLAYER_POS_X = MAP_WIDTH - TILE_WIDTH // 2

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
        self.camera = arcade.Camera(self.width, self.height)
        # camera to draw HUD
        self.gui_camera = arcade.Camera(self.width, self.height)

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

        # activate camera to draw scene on it
        self.camera.use()

        self.scene.draw()

        # after gui_camera.use(), arcade will draw anything on this camera, not in the other camera
        #  otherwise the text will stay at the map start
        self.gui_camera.use()
        arcade.draw_text(
            f"Coins: {self.collected_coins}",
            10,
            WINDOW_HEIGHT - 50,
            arcade.color.GOLD,
            font_size=30,
        )

    def clamp(self, value, low, high):
        return max(min(value, high), low)

    def camera_position(self):
        # constrain player inside map boundaries
        self.player_sprite.center_x = self.clamp(
            self.player_sprite.center_x, HALF_TILE_WIDTH, MAX_PLAYER_POS_X
        )

        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0

        if MAP_WIDTH - self.player_sprite.center_x < self.camera.viewport_width / 2:
            screen_center_x = MAP_WIDTH - self.camera.viewport_width

        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def on_update(self, delta_time: float):
        self.physics_engine.update()
        self.camera_position()

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
