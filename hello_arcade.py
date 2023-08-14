import arcade

SCREEN_WIDTH = 1280
SCREEN_HIGHT = 800
SCREEN_TITLE = "Hola arcade"

def auto():
    arcade.draw_rectangle_filled(630, 0, 1280,300, arcade.color.DARK_GRAY  )
    arcade.draw_rectangle_filled(640, 320, 1000, 200, arcade.color.RED_DEVIL)
    arcade.draw_rectangle_filled(640, 470, 500, 100, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_outline(640, 470, 500, 100, arcade.color.RED_DEVIL)
    arcade.draw_rectangle_filled(640, 570, 500, 100, arcade.color.RED_DEVIL)
    arcade.draw_rectangle_filled(1120,350, 50,50, arcade.color.YELLOW_ORANGE)
    arcade.draw_circle_filled(960,200,100,arcade.color.BLACK_LEATHER_JACKET)
    arcade.draw_circle_filled(960, 200, 65, arcade.color.SPANISH_GRAY)
    arcade.draw_circle_filled(320,200,100,arcade.color.BLACK_LEATHER_JACKET)
    arcade.draw_circle_filled(320, 200, 65, arcade.color.SPANISH_GRAY)

if __name__ == "__main__":
    #Crear ventana
    arcade.open_window(SCREEN_WIDTH,SCREEN_HIGHT, SCREEN_TITLE)
    #Cambiar color de fondo
    arcade.set_background_color(arcade.color.LIGHT_BLUE)

    #Iniciar render
    arcade.start_render()
    #Funciones para dibujar
    auto()
    #finalizar render
    arcade.finish_render()

    #correr el programa
    arcade.run()


