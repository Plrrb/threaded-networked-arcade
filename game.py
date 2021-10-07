import arcade

from player1 import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "threaded arcade"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.player1 = None
        self.player2 = None

    def setup(self):
        self.player1 = Player(":resources:images/topdown_tanks/tank_blue.png")
        self.player2 = Player(":resources:images/topdown_tanks/tank_green.png")

    def on_draw(self):
        self.player1.draw()
        self.player2.draw()

    def on_update(self, delta_time: float):
        self.player1.update()
        self.player2.update()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W:
            self.player1.up()


def main():
    """Main method"""
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
