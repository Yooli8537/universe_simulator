# Game Config
WINDOW_SIZE = 1000
WINDOW_HEIGHT = 800
FPS = 60
MODE = "GALAXY" # GALAXY, UNIVERSE, SYSTEM
GAME_SPEED = 1 # Multiplies physics calculations to increase game speed

# Physics Constants
GRAVITY_CONSTANT = 5 # aka Gravity Strength
SOFTENING = 5 # prevents infinite acceleration when two bodies get too close.
SPIN_ACTIVE = False

# Bodies
MAX_BODIES = 200
ACTIVE_BODIES = ["brown_dwarf", "red_dwarf", "sun", "blue_giant", "red_giant", "white_dwarf", "neutron_star", "pulsar", "black_hole", "quasar"]

# Galaxy Simulation
GALAXY_CENTER_X = WINDOW_SIZE * 0.5
GALAXY_CENTER_Y = WINDOW_HEIGHT * 0.5