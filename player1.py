from game import MyGame
import arcade
import socket
import threading

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "threaded arcade player 1"


def main():
    """Main method"""

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((socket.gethostname(), 5555))
    server_socket.listen(1)

    print("Waiting for client connection...")
    client_socket, addr = server_socket.accept()
    print("Client connected from", addr)

    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, client_socket, True)

    recv_thread = threading.Thread(target=game.recv_move, daemon=True)

    game.setup()
    game.send_our_pos()
    recv_thread.start()
    arcade.run()


if __name__ == "__main__":
    main()
