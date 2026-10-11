import math
import struct
import pygame
from .player import Player
from .platform import Platform
from .hazard import Hazard

WHITE = (255, 255, 255)
BROWN = (150, 100, 60)
RED = (220, 60, 60)
GREEN = (0, 200, 0)
DARK = (20, 28, 45)
YELLOW = (255, 215, 80)
CYAN = (100, 230, 240)


class SoundEffects:
    """Create short tones at runtime so no external sound files are required."""
    def __init__(self):
        self.sounds = {}
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=512)
            sample_rate = pygame.mixer.get_init()[0]
            self.sounds = {
                "jump": self._tone(sample_rate, 660, 0.09),
                "goal": self._tone(sample_rate, 880, 0.18),
                "die": self._tone(sample_rate, 180, 0.28),
            }
        except (pygame.error, TypeError):
            # The game remains playable on systems without audio support.
            self.sounds = {}

    @staticmethod
    def _tone(sample_rate, frequency, duration):
        count = int(sample_rate * duration)
        amplitude = 7000
        frames = bytearray()
        for i in range(count):
            fade = 1.0 - i / max(1, count)
            sample = int(amplitude * fade * math.sin(2 * math.pi * frequency * i / sample_rate))
            frames.extend(struct.pack("<h", sample))
        return pygame.mixer.Sound(buffer=bytes(frames))

    def play(self, name):
        sound = self.sounds.get(name)
        if sound is not None:
            try:
                sound.play()
            except pygame.error:
                pass


class GameEngine:
    DIFFICULTIES = {
        "Easy": {"gravity": 0.45, "jump": -11.0},
        "Medium": {"gravity": 0.60, "jump": -12.0},
        "Hard": {"gravity": 0.82, "jump": -13.5},
    }

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont("Arial", 30)
        self.title_font = pygame.font.SysFont("Arial", 44, bold=True)
        self.small_font = pygame.font.SysFont("Arial", 21)
        self.sfx = SoundEffects()
        self.difficulty = "Medium"
        self.started = False
        self._build_level()

    def _build_level(self):
        settings = self.DIFFICULTIES[self.difficulty]
        self.gravity = settings["gravity"]
        self.start_x, self.start_y = 40, self.height - 120
        self.player = Player(self.start_x, self.start_y)
        self.player.jump_strength = settings["jump"]

        ground_y = self.height - 40
        self.platforms = [
            Platform(0, ground_y, 160),
            Platform(220, ground_y, 140),
            Platform(420, ground_y - 60, 120),
            Platform(600, ground_y, 180),
        ]
        self.hazards = [Hazard(240, ground_y - 14, 100)]
        self.goal_x = 740
        self.score = 0
        self.game_over = False
        self._game_over_reason = ""

    def _select_difficulty(self, key):
        if key in (pygame.K_1, pygame.K_KP1):
            self.difficulty = "Easy"
        elif key in (pygame.K_2, pygame.K_KP2):
            self.difficulty = "Medium"
        elif key in (pygame.K_3, pygame.K_KP3):
            self.difficulty = "Hard"
        else:
            return False
        return True

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_ESCAPE:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            return

        # Difficulty can be selected on the opening screen and after Game Over.
        if not self.started or self.game_over:
            if self._select_difficulty(event.key):
                return
            if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                self._build_level()
                self.started = True
            return

        if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
            if self.player.on_ground:
                self.player.jump()
                self.sfx.play("jump")

    def handle_input(self):
        if not self.started or self.game_over:
            self.player.vx = 0
            return
        keys = pygame.key.get_pressed()
        self.player.vx = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.vx = -self.player.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.vx = self.player.speed

    def _end_game(self, reason):
        if not self.game_over:
            self.game_over = True
            self._game_over_reason = reason
            self.sfx.play("die")

    def update(self):
        if not self.started or self.game_over:
            return

        # Save the previous bottom edge so a fast fall cannot skip a platform.
        previous_rect = self.player.rect()
        previous_bottom = previous_rect.bottom
        self.player.vy = min(self.player.vy + self.gravity, 14)
        self.player.x = max(0, min(self.width - self.player.width,
                                   self.player.x + self.player.vx))
        self.player.y += self.player.vy
        current_rect = self.player.rect()
        self.player.on_ground = False

        if self.player.vy >= 0:
            for platform in self.platforms:
                platform_rect = platform.rect()
                crossed_top = previous_bottom <= platform_rect.top and current_rect.bottom >= platform_rect.top
                overlaps_horizontally = current_rect.right > platform_rect.left and current_rect.left < platform_rect.right
                if crossed_top and overlaps_horizontally:
                    self.player.y = platform_rect.top - self.player.height
                    self.player.vy = 0
                    self.player.on_ground = True
                    current_rect = self.player.rect()
                    break

        for hazard in self.hazards:
            if self.player.rect().colliderect(hazard.rect()):
                self._end_game("You hit a hazard!")
                return

        if self.player.y > self.height:
            self._end_game("You fell off the level!")
            return

        if self.player.x >= self.goal_x:
            self.score += 1
            self.sfx.play("goal")
            self.player.x, self.player.y = self.start_x, self.start_y
            self.player.vx = 0
            self.player.vy = 0
            self.player.on_ground = False

    def _draw_centered(self, screen, text, font, color, y):
        surface = font.render(text, True, color)
        screen.blit(surface, surface.get_rect(center=(self.width // 2, y)))

    def _draw_difficulty_options(self, screen, start_y):
        options = [
            f"1 - Easy  (gravity {self.DIFFICULTIES['Easy']['gravity']})",
            f"2 - Medium  (gravity {self.DIFFICULTIES['Medium']['gravity']})",
            f"3 - Hard  (gravity {self.DIFFICULTIES['Hard']['gravity']})",
        ]
        for i, option in enumerate(options):
            selected = option.split(" - ")[1].split()[0]
            color = YELLOW if self.difficulty == selected else WHITE
            self._draw_centered(screen, option, self.small_font, color, start_y + i * 30)

    def render(self, screen):
        for platform in self.platforms:
            pygame.draw.rect(screen, BROWN, platform.rect(), border_radius=3)
        for hazard in self.hazards:
            pygame.draw.rect(screen, RED, hazard.rect(), border_radius=3)

        goal_rect = pygame.Rect(self.goal_x, 0, 6, self.height)
        pygame.draw.rect(screen, GREEN, goal_rect)
        pygame.draw.rect(screen, WHITE, self.player.rect())

        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        diff_text = self.small_font.render(f"Difficulty: {self.difficulty}", True, WHITE)
        screen.blit(diff_text, (10, 44))

        if not self.started or self.game_over:
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill((8, 12, 24, 225))
            screen.blit(overlay, (0, 0))
            if not self.started:
                self._draw_centered(screen, "SIMPLE PLATFORMER", self.title_font, CYAN, 105)
                self._draw_centered(screen, "Choose difficulty to start", self.font, WHITE, 165)
                self._draw_difficulty_options(screen, 225)
                self._draw_centered(screen, "ENTER / SPACE: Start", self.small_font, YELLOW, 350)
                self._draw_centered(screen, "Move: A/D or arrows   Jump: W/UP/SPACE   ESC: Exit", self.small_font, WHITE, 405)
            else:
                self._draw_centered(screen, "GAME OVER", self.title_font, RED, 105)
                self._draw_centered(screen, self._game_over_reason, self.font, WHITE, 158)
                self._draw_centered(screen, f"Final score: {self.score}", self.font, YELLOW, 205)
                self._draw_centered(screen, "Choose difficulty:", self.small_font, CYAN, 255)
                self._draw_difficulty_options(screen, 285)
                self._draw_centered(screen, "ENTER / SPACE: Play again     ESC: Exit", self.small_font, WHITE, 405)
