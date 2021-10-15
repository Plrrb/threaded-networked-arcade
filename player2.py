from game import MyGame
import arcade
import socket
import sys
import threading


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "threaded arcade player 2"


def main():
    """Main method"""

    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connection to hostname on the port.
    player2_ip = sys.argv[1]

    print("Trying to connect...")
    client_socket.connect((player2_ip, 5555))
    print("Connected!")

    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, client_socket, False)

    recv_thread = threading.Thread(target=game.recv_move, daemon=True)

    game.setup()
    recv_thread.start()
    arcade.run()


if __name__ == "__main__":
    main()
