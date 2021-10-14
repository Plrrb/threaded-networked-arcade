import arcade
import socket
import threading

from game import MyGame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "threaded arcade player 2"


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
