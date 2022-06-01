import arcade


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lines([(0, 0), (100, 100)], arcade.color.RED, 4)
        arcade.draw_point(150, 150, arcade.color.WHITE, 20)
        arcade.draw_circle_filled(250, 150, 50, arcade.color.GREEN, 50)
        arcade.draw_circle_outline(450, 200, 50, arcade.color.BLUE, 5, 50)
        arcade.draw_lrtb_rectangle_filled(500, 600, 600, 500, arcade.color.YELLOW)


MyGameWindow(1280, 720, "My Game Window")
arcade.run()
