import arcade
import socket
import threading

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "threaded arcade"


class Player(arcade.Sprite):
    def __init__(self, image):
        super().__init__(image)

    def up(self):
        self.change_y += 1

    def down(self):
        self.change_y -= 1

    def left(self):
        self.change_x -= 1

    def right(self):
        self.change_x += 1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, client_socket)
        self.client_socket = client_socket
        self.player2 = None
        self.player1 = None

    def setup(self):
        self.player2 = Player(":resources:images/topdown_tanks/tank_red.png")
        self.player1 = Player(":resources:images/topdown_tanks/tank_blue.png")

    def on_draw(self):
        arcade.start_render()

        self.player2.draw()
        self.player1.draw()

    def recv_move(self):
        player_pos = self.client_socket.recv(1024)
        player_pos.decode("ascii")

        player_pos = eval(player_pos)

        self.player1.center_x, self.player1.center_y = player_pos

    def on_update(self, delta_time: float):

        self.player2.update()

        data = f"({self.player2.center_x}, {self.player2.center_y})".encode("ascii")
        self.client_socket.send(data)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W:
            self.player2.up()

        if key == arcade.key.A:
            self.player2.left()

        if key == arcade.key.D:
            self.player2.right()

        if key == arcade.key.S:
            self.player2.down()


def main():
    """Main method"""

    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connection to hostname on the port.
    client_socket.connect(("162.196.90.150", 5555))

    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, client_socket)

    recv_thread = threading.Thread(target=game.recv_move, daemon=True)

    game.setup()
    recv_thread.start()
    arcade.run()


if __name__ == "__main__":
    main()
