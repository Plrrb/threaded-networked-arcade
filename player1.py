import arcade
import socket
import threading
import time

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
    def __init__(self, width, height, title, client_socket):
        super().__init__(width, height, title)
        self.client_socket = client_socket
        self.player1 = None
        self.player2 = None

    def setup(self):
        self.player1 = Player(":resources:images/topdown_tanks/tank_blue.png")
        self.player2 = Player(":resources:images/topdown_tanks/tank_red.png")

    def on_draw(self):
        arcade.start_render()

        self.player1.draw()
        self.player2.draw()

    def recv_move(self):
        while True:
            time.sleep(1 / 60)
            player_pos = self.client_socket.recv(1024)
            player_pos = player_pos.decode("ascii")

            print(player_pos)

            player_pos = eval(player_pos)
            print(player_pos)

            self.player2.center_x, self.player2.center_y = player_pos

            data = f"({self.player1.center_x}, {self.player1.center_y})".encode("ascii")
            self.client_socket.send(data)

    def on_update(self, delta_time: float):
        self.player1.update()
        self.player2.update()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W:
            self.player1.up()

        if key == arcade.key.A:
            self.player1.left()

        if key == arcade.key.D:
            self.player1.right()

        if key == arcade.key.S:
            self.player1.down()


def main():
    """Main method"""

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((socket.gethostname(), 5555))
    server_socket.listen(1)

    print("waiting for client connection")
    client_socket, addr = server_socket.accept()
    print("client connected from", addr)

    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, client_socket)

    recv_thread = threading.Thread(target=game.recv_move, daemon=True)

    game.setup()
    recv_thread.start()
    arcade.run()


if __name__ == "__main__":
    main()
