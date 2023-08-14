import arcade
from circles import get_circle
import circles

# Definición de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Circulos con bresenham"


class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size = 5
        self.xc = 30
        self.yc =60
        self.r = 20
        self.circle_color = arcade.color.RED_DEVIL
        self.speed = 25
        self.velocity = [self.speed, self.speed]

    def on_update(self, delta_time: float):
        self.xc += delta_time * self.velocity[0]
        self.yc += delta_time * self.velocity[1]
        self.r += delta_time * 5
        if self.xc > (SCREEN_WIDTH // self.pixel_size)-self.r or self.xc < self.r:
            self.velocity[0] = -1 * self.velocity[0]
            self.r = delta_time/3
        if self.yc > (SCREEN_HEIGHT // self.pixel_size)-self.r or self.yc < self.r:
            self.velocity[1] = -1 * self.velocity[1]
            self.r = delta_time/3

    def on_draw(self):
        arcade.start_render()
        points = get_circle(self.xc, self.yc, self.r)
        self.draw_grid()
        self.draw_circle_points(points, arcade.color.DARK_YELLOW)
        self.draw_scaled_circle(self.xc, self.yc, self.r)

    def draw_grid(self):
        # Lineas verticales
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l + self.pixel_size / 2,
                0,
                v_l + self.pixel_size / 2,
                SCREEN_HEIGHT,
                [20, 20, 20]
            )

        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0,
                h_l + self.pixel_size / 2,
                SCREEN_WIDTH,
                h_l + self.pixel_size / 2,
                [20, 20, 20]
            )

    def draw_circle_points(self, points, color):
        for p in points:
            x = p[0] * self.pixel_size  # Escalar la coordenada x
            y = p[1] * self.pixel_size  # Escalar la coordenada y
            arcade.draw_point(x, y, color, self.pixel_size)

    def draw_scaled_circle(self, xc, yc, r):
        x = xc * self.pixel_size  # Escalar la coordenada x del centro
        y = yc * self.pixel_size  # Escalar la coordenada y del centro
        radius = r * self.pixel_size  # Escalar el radio
        arcade.draw_circle_outline(
            x,
            y,
            radius,
            [100, 255, 40, 150],
            5
        )


if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()
