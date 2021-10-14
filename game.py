import arcade


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
    def __init__(self, width, height, title, client_socket):
        super().__init__(width, height, title)
        self.client_socket = client_socket
        self.player1 = None
        self.player2 = None

    def setup(self):
        self.player1 = Player(":resources:images/topdown_tanks/tank_blue.png")
        self.player2 = arcade.Sprite(":resources:images/topdown_tanks/tank_red.png")

    def on_draw(self):
        arcade.start_render()

        self.player1.draw()
        self.player2.draw()

    def send_our_pos(self):
        data = f"({self.player1.center_x}, {self.player1.center_y})".encode("ascii")
        self.client_socket.send(data)

    def recv_move(self):
        while True:
            player_pos = self.client_socket.recv(1024)
            player_pos = player_pos.decode("ascii")

            player_pos = eval(player_pos)

            self.player2.center_x, self.player2.center_y = player_pos
            self.send_our_pos()

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
            self.player2.stop_y()

        if key == arcade.key.A or key == arcade.key.D:
            self.player2.stop_x()
