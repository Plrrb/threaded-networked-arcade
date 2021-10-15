import arcade
import threading


class Player(arcade.Sprite):
    def __init__(self, image):
        super().__init__(image)

    def up(self):
        self.change_y = 1

    def down(self):
        self.change_y = -1

    def left(self):
        self.change_x = -1

    def right(self):
        self.change_x = 1

    def stop_x(self):
        self.change_x = 0

    def stop_y(self):
        self.change_y = 0


class MyGame(arcade.Window):
    def __init__(
        self, width, height, title, client_socket, player1_image, player2_image
    ):
        super().__init__(width, height, title)
        self.client_socket = client_socket
        self.player1 = player1_image
        self.player2 = player2_image

    def setup(self):

        self.player1 = Player(self.player1)
        self.player2 = arcade.Sprite(self.player2)

        recv_thread = threading.Thread(target=self.recv_move, daemon=True)
        recv_thread.start()

    def on_draw(self):
        arcade.start_render()

        self.player2.draw()
        self.player1.draw()

    def send_our_pos(self):
        data = f"({self.player1.center_x}, {self.player1.center_y})".encode("ascii")
        self.client_socket.send(data)

    def recv_move(self):
        while True:
            try:
                player_pos = self.client_socket.recv(1024)
                player_pos = player_pos.decode("ascii")

                player_pos = eval(player_pos)

                self.player2.center_x, self.player2.center_y = player_pos
                self.send_our_pos()
            except:
                print("Other Player has left", "Exiting...")
                self.client_socket.close()
                arcade.exit()
                return

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

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player1.stop_y()

        if key == arcade.key.A or key == arcade.key.D:
            self.player1.stop_x()
