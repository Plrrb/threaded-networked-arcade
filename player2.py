from game import MyGame
import arcade
import socket
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "threaded arcade player 2"


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    player2_ip = sys.argv[1]

    print("Trying to connect...")
    client_socket.connect((player2_ip, 5555))
    print("Connected!")

    game = MyGame(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        SCREEN_TITLE,
        client_socket,
        ":resources:images/topdown_tanks/tank_red.png",
        ":resources:images/topdown_tanks/tank_blue.png",
    )
    game.setup()
    arcade.run()
    game.leave()


if __name__ == "__main__":
    main()
