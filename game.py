import pygame
from const import *
from board import Board

class Game:
    def __init__(self, ultimate=False, max=False):
        self.ultimate = ultimate
        self.max = max
        self.board = Board(ultimate=ultimate, max=max)
        self.player = 1
        self.playing = True
        pygame.font.init()

    def render_board(self, surface):
        self.board.render(surface)

    def next_turn(self):
        self.player = 2 if self.player == 1 else 1

    def ultimate_winner(self, surface, winner):
        print('ULTIMATE WINNER! ->', winner)

        color = CROSS_COLOR if winner == 1 else CIRCLE_COLOR

        if winner == 1:
            iDesc = (WIDTH // 2 - 110, HEIGHT // 2 - 110)
            fDesc = (WIDTH // 2 + 110, HEIGHT // 2 + 110)
            iAsc = (WIDTH // 2 - 110, HEIGHT // 2 + 110)
            fAsc = (WIDTH // 2 + 110, HEIGHT // 2 - 110)
            pygame.draw.line(surface, color, iDesc, fDesc, 22)
            pygame.draw.line(surface, color, iAsc, fAsc, 22)
        else:
            center = (WIDTH // 2, HEIGHT // 2)
            pygame.draw.circle(surface, color, center, WIDTH // 4, 22)
        
        font = pygame.font.SysFont('monospace', 64)
        lbl = font.render('ULTIMATE WINNER!', True, color)
        surface.blit(lbl, (WIDTH // 2 - lbl.get_rect().width // 2, HEIGHT // 2 + 220))

        self.playing = False

    def restart(self):
        self.__init__(self.ultimate, self.max)
