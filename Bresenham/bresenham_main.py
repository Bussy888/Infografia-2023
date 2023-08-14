import arcade

from Bresenham.bresenham import get_line

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bresenham Line Drawing"

class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size = 20

    def on_draw(self):
        arcade.start_render()

        points = get_line(5, 5, 30, 15)
        self.draw_grid()
        self.draw_line_points(points, arcade.color.DARK_YELLOW)
        self.draw_scaled_line(30, 15, 5, 5)

    def draw_grid(self):
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l + self.pixel_size / 2,
                0,
                v_l + self.pixel_size / 2,
                SCREEN_HEIGHT,
                arcade.color.DARK_GRAY
            )

        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0,
                h_l + self.pixel_size / 2,
                SCREEN_WIDTH,
                h_l + self.pixel_size / 2,
                arcade.color.LIGHT_GRAY
            )

    def draw_line_points(self, points, color):
        for p in points:
            arcade.draw_point(p[0] * self.pixel_size, p[1] * self.pixel_size, color, self.pixel_size)

    def draw_scaled_line(self, x0, y0, x1, y1):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        while x0 != x1 or y0 != y1:
            arcade.draw_point(x0 * self.pixel_size, y0 * self.pixel_size, arcade.color.RED, self.pixel_size)
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

            # Draw the final point
            arcade.draw_point(x0 * self.pixel_size, y0 * self.pixel_size, arcade.color.RED, self.pixel_size)

if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()