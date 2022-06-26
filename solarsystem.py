import pygame
from random import randint

import planetmodel as model
import planetview as view


def main():
    WINDOW_WIDTH = 900
    WINDOW_HEIGHT = 900
    RESOLUTION_COEFICIENT = 5
    planets = []
    run = True
    clock = pygame.time.Clock()
    pygame.init()
    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Solar System")
    planets_radiuses = [8, 10, 15, 30, 50, 60, 40, 30, 10]
    planets_orbit_radiuses = [30, 60, 90, 140, 180, 240, 310, 350, 420]
    planets_colors = ["yellow", "red", "green", "blue", "brown", "cyan",
                      "white", "pink", "maroon"]
    for planet_index in range(len(planets_radiuses)):
        planet_model = model.Planet(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2,
                                    planets_orbit_radiuses[planet_index],
                                    (planets_orbit_radiuses[planet_index] *
                                     RESOLUTION_COEFICIENT))
        planet_points = planet_model.points
        planets.append(view.Planet(planets_radiuses[planet_index],
                                   planets_colors[planet_index],
                                   surface, planet_points,
                                   randint(0, len(planet_points))))
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        surface.fill((0, 0, 0))
        for planet in planets:
            planet.draw()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()