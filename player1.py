from game import MyGame
import arcade
import socket

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "threaded arcade player 1"


def main():
    print(socket.gethostbyname(socket.gethostname()))

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((socket.gethostname(), 5555))
    server_socket.listen(1)

    print("Waiting for client connection...")
    client_socket, addr = server_socket.accept()
    print("Client connected from", addr)

    game = MyGame(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        SCREEN_TITLE,
        client_socket,
        ":resources:images/topdown_tanks/tank_blue.png",
        ":resources:images/topdown_tanks/tank_red.png",
    )
    game.setup()
    game.send_our_pos()
    arcade.run()
    game.leave()


if __name__ == "__main__":
    main()
