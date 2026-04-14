tiny = (0.5, 2)
small = (1, 3)
medium = (2, 4)
large = (3, 5)
giant = (4, 6)

brown_dwarf = {
    "name": "brown_dwarf",
    "size": tiny,
    "color": ((112, 48, 6), (148, 71, 9)),
    "density": 0.5,
    "rarity": 0.8
}

red_dwarf = {
    "name": "red_dwarf",
    "size": small,
    "color": ((128, 5, 0), (176, 67, 5)),
    "density": 1,
    "rarity": 1
}

# Sun-like stars
sun = {
    "name": "sun",
    "size": medium,
    "color": ((240, 197, 5), (247, 245, 96)),
    "density": 2,
    "rarity": 0.6
}

blue_giant = {
    "name": "blue_giant",
    "size": large,
    "color": ((125, 212, 255), (184, 230, 255)),
    "density": 2,
    "rarity": 0.3,
    "special": "twinkle"
}

red_giant = {
    "name": "red_giant",
    "size": giant,
    "color": ((255, 0, 0), (255, 98, 0)),
    "density": 1,
    "rarity": 0.2
}

white_dwarf = {
    "name": "white_dwarf",
    "size": small,
    "color": ((143, 236, 255), (222, 255, 255)),
    "density": 4,
    "rarity": 0.25,
}

neutron_star = {
    "name": "neutron_star",
    "size": tiny,
    "color": ((199, 255, 255), (255, 255, 255)),
    "density": 8,
    "rarity": 0.1,
}

pulsar = {
    "name": "pulsar",
    "size": tiny,
    "color": ((199, 255, 255), (255, 255, 255)),
    "density": 8,
    "rarity": 0.05,
    "special": "rotation"
}

black_hole = {
    "name": "black_hole",
    "size": medium,
    "color": ((0, 0, 0), (24, 24, 24)),
    "density": 15,
    "rarity": 0.08,
}

quasar = {
    "name": "quasar",
    "size": large,
    "color": ((128, 236, 255), (209, 244, 255)),
    "density": 15,
    "rarity": 0.02,
}

# Cannot spawn naturally
galaxy_center = {
    "name": "galaxy_center",
    "size": giant,
    "color": ((0, 255, 0), (24, 24, 24)),
    "density": 100,
    "rarity": 0
}

ALL_BODIES = [brown_dwarf,red_dwarf,sun,blue_giant,red_giant,white_dwarf,neutron_star,pulsar,black_hole,quasar]
