import time
import pygame as pg
import numpy as np

Color_bg = (10,10,10)
Color_gr = (40,40,40)
Color_dnx = (170,170,170)
Color_anx = (255,255,255)


def update(screen, cells, size, with_progress = False):
    updated_cells = np.zeros((cells.shape[0],cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2])-cells[row,col]
        color = Color_bg if cells[row,col] == 0 else Color_anx

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = Color_dnx
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = Color_anx
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = Color_anx

        pg.draw.rect(screen,color,(col * size, row * size,size-1,size-1))

    return updated_cells

def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    cells = np.zeros((60, 80))
    screen.fill(Color_gr)
    update(screen, cells,  10)

    pg.display.flip()
    pg.display.update()

    running = False

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pg.display.update()
                elif event.key == pg.K_r:
                    cells = np.zeros((60, 80))
                    running = False
                    update(screen, cells, 10)
                    pg.display.update()
            if pg.mouse.get_pressed()[0]:
                pos = pg.mouse.get_pos()
                if cells[pos[1] // 10, pos[0] // 10] == 1:
                    cells[pos[1] // 10, pos[0] // 10] = 0
                    update(screen, cells, 10)
                    pg.display.update()
                else:
                    cells[pos[1] // 10, pos[0] // 10] = 1
                    update(screen, cells, 10)
                    pg.display.update()
        screen.fill(Color_gr)

        if running:
            cells = update(screen, cells, 10, with_progress=True)
            pg.display.update()

        time.sleep(0.001)

if __name__ == '__main__':
    main()


