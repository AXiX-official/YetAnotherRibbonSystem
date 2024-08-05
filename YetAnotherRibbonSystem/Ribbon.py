

class Ribbon:

    __slots__ = ('_type','file_name', 'score')

    RIBBON_UNKNOWN = "UNKNOWN"

    RIBBON_MAIN_CALIBER = "RIBBON_MAIN_CALIBER"
    RIBBON_TORPEDO = "RIBBON_TORPEDO"
    RIBBON_BOMB = "RIBBON_BOMB"
    RIBBON_PLANE = "RIBBON_PLANE"
    RIBBON_CRIT = "RIBBON_CRIT"
    RIBBON_FRAG = "RIBBON_FRAG"
    RIBBON_BURN = "RIBBON_BURN"
    RIBBON_FLOOD = "RIBBON_FLOOD"
    RIBBON_CITADEL = "RIBBON_CITADEL"
    RIBBON_BASE_DEFENSE = "RIBBON_BASE_DEFENSE"
    RIBBON_BASE_CAPTURE = "RIBBON_BASE_CAPTURE"
    RIBBON_BASE_CAPTURE_ASSIST = "RIBBON_BASE_CAPTURE_ASSIST"
    RIBBON_SUPPRESSED = "RIBBON_SUPPRESSED"
    RIBBON_SECONDARY_CALIBER = "RIBBON_SECONDARY_CALIBER"
    RIBBON_MAIN_CALIBER_OVER_PENETRATION = "RIBBON_MAIN_CALIBER_OVER_PENETRATION"
    RIBBON_MAIN_CALIBER_PENETRATION = "RIBBON_MAIN_CALIBER_PENETRATION"
    RIBBON_MAIN_CALIBER_NO_PENETRATION = "RIBBON_MAIN_CALIBER_NO_PENETRATION"
    RIBBON_MAIN_CALIBER_RICOCHET = "RIBBON_MAIN_CALIBER_RICOCHET"
    RIBBON_BUILDING_KILL = "RIBBON_BUILDING_KILL"
    RIBBON_BOMB_OVER_PENETRATION = "RIBBON_BOMB_OVER_PENETRATION"
    RIBBON_BOMB_PENETRATION = "RIBBON_BOMB_PENETRATION"
    RIBBON_BOMB_NO_PENETRATION = "RIBBON_BOMB_NO_PENETRATION"
    RIBBON_ROCKET = "RIBBON_ROCKET"
    RIBBON_BOMB_RICOCHET = "RIBBON_BOMB_RICOCHET"
    RIBBON_DETECTED = "RIBBON_DETECTED"
    RIBBON_ROCKET_PENETRATION = "RIBBON_ROCKET_PENETRATION"
    RIBBON_ROCKET_NO_PENETRATION = "RIBBON_ROCKET_NO_PENETRATION"
    RIBBON_SPLANE = "RIBBON_SPLANE"
    RIBBON_BULGE = "RIBBON_BULGE"
    RIBBON_BOMB_BULGE = "RIBBON_BOMB_BULGE"
    RIBBON_ROCKET_BULGE = "RIBBON_ROCKET_BULGE"
    RIBBON_ROCKET_RICOCHET = "RIBBON_ROCKET_RICOCHET"
    RIBBON_ROCKET_OVER_PENETRATION = "RIBBON_ROCKET_OVER_PENETRATION"

    _type_map = {
        # 0: (RIBBON_MAIN_CALIBER, "ribbon_main_caliber.png"),
        1: (RIBBON_TORPEDO, "ribbon_torpedo.png"),
        # 2: (RIBBON_BOMB, "ribbon_bomb.png"),
        3: (RIBBON_PLANE, "ribbon_plane.png"),
        4: (RIBBON_CRIT, "ribbon_crit.png"),
        5: (RIBBON_FRAG, "ribbon_frag.png"),
        6: (RIBBON_BURN, "ribbon_burn.png"),
        7: (RIBBON_FLOOD, "ribbon_flood.png"),
        8: (RIBBON_CITADEL, "ribbon_citadel.png"),
        9: (RIBBON_BASE_DEFENSE, "ribbon_base_defense.png"),
        10: (RIBBON_BASE_CAPTURE, "ribbon_base_capture.png"),
        11: (RIBBON_BASE_CAPTURE_ASSIST, "ribbon_base_capture_assist.png"),
        12: (RIBBON_SUPPRESSED, "ribbon_suppressed.png"),
        13: (RIBBON_SECONDARY_CALIBER, "ribbon_secondary_caliber.png"),
        14: (RIBBON_MAIN_CALIBER_OVER_PENETRATION, "subribbon_main_caliber_over_penetration.png"),
        15: (RIBBON_MAIN_CALIBER_PENETRATION, "subribbon_main_caliber_penetration.png"),
        16: (RIBBON_MAIN_CALIBER_NO_PENETRATION, "subribbon_main_caliber_no_penetration.png"),
        17: (RIBBON_MAIN_CALIBER_RICOCHET, "subribbon_main_caliber_ricochet.png"),
        18: (RIBBON_BUILDING_KILL, "ribbon_building_kill.png"),
        19: (RIBBON_DETECTED, "ribbon_detected.png"),
        20: (RIBBON_BOMB_OVER_PENETRATION, "subribbon_bomb_over_penetration.png"),
        21: (RIBBON_BOMB_PENETRATION, "subribbon_bomb_penetration.png"),
        22: (RIBBON_BOMB_NO_PENETRATION, "subribbon_bomb_no_penetration.png"),
        23: (RIBBON_BOMB_RICOCHET, "subribbon_bomb_ricochet.png"),
        # 24: (RIBBON_ROCKET, "ribbon_rocket.png"),
        25: (RIBBON_ROCKET_PENETRATION, "subribbon_rocket_penetration.png"),
        26: (RIBBON_ROCKET_NO_PENETRATION, "subribbon_rocket_no_penetration.png"),
        27: (RIBBON_SPLANE, "ribbon_splane.png"),
        28: (RIBBON_BULGE, "subribbon_bulge.png"),
        29: (RIBBON_BOMB_BULGE, "subribbon_bomb_bulge.png"),
        30: (RIBBON_ROCKET_BULGE, "subribbon_rocket_bulge.png"),
        34: (RIBBON_ROCKET_RICOCHET, "subribbon_rocket_ricochet.png"),
        35: (RIBBON_ROCKET_OVER_PENETRATION, "subribbon_rocket_over_penetration.png"),
    }

    _exciting_time = {
        1: {"AirCarrier" : 8000, "Battleship" : 10000, "Cruiser" : 8000, "Destroyer" : 8000, "Submarine" : 5000},
        3: {"AirCarrier" : 10000, "Battleship" : 10000, "Cruiser" : 10000, "Destroyer" : 10000, "Submarine" : 0},
        4: {"AirCarrier" : 12000, "Battleship" : 12000, "Cruiser" : 12000, "Destroyer" : 12000, "Submarine" : 12000},
        5: {"AirCarrier" : 20000, "Battleship" : 20000, "Cruiser" : 20000, "Destroyer" : 20000, "Submarine" : 20000},
        6: {"AirCarrier" : 15000, "Battleship" : 15000, "Cruiser" : 15000, "Destroyer" : 15000, "Submarine" : 0},
        7: {"AirCarrier" : 15000, "Battleship" : 15000, "Cruiser" : 15000, "Destroyer" : 15000, "Submarine" : 15000},
        8: {"AirCarrier" : 18000, "Battleship" : 18000, "Cruiser" : 18000, "Destroyer" : 18000, "Submarine" : 0},
        9: {"AirCarrier" : 12000, "Battleship" : 12000, "Cruiser" : 12000, "Destroyer" : 12000, "Submarine" : 12000},
        10: {"AirCarrier" : 30000, "Battleship" : 30000, "Cruiser" : 30000, "Destroyer" : 30000, "Submarine" : 30000},
        11: {"AirCarrier" : 25000, "Battleship" : 25000, "Cruiser" : 25000, "Destroyer" : 25000, "Submarine" : 25000},
        12: {"AirCarrier" : 10000, "Battleship" : 10000, "Cruiser" : 10000, "Destroyer" : 10000, "Submarine" : 10000},
        13: {"AirCarrier" : 8000, "Battleship" : 5000, "Cruiser" : 6000, "Destroyer" : 10000, "Submarine" : 10000},
        14: {"AirCarrier" : 5000, "Battleship" : 5000, "Cruiser" : 3000, "Destroyer" : 2500, "Submarine" : 3000},
        15: {"AirCarrier" : 8000, "Battleship" : 8000, "Cruiser" : 5000, "Destroyer" : 4000, "Submarine" : 4000},
        16: {"AirCarrier" : 5000, "Battleship" : 5000, "Cruiser" : 3000, "Destroyer" : 2500, "Submarine" : 3000},
        17: {"AirCarrier" : 5000, "Battleship" : 5000, "Cruiser" : 3000, "Destroyer" : 2500, "Submarine" : 3000},
        18: {"AirCarrier" : 10000, "Battleship" : 10000, "Cruiser" : 10000, "Destroyer" : 10000, "Submarine" : 10000},
        19: {"AirCarrier" : 20000, "Battleship" : 20000, "Cruiser" : 20000, "Destroyer" : 20000, "Submarine" : 20000},
        20: {"AirCarrier" : 6000, "Battleship" : 5000, "Cruiser" : 6000, "Destroyer" : 6000, "Submarine" : 0},
        21: {"AirCarrier" : 10000, "Battleship" : 8000, "Cruiser" : 10000, "Destroyer" : 10000, "Submarine" : 0},
        22: {"AirCarrier" : 6000, "Battleship" : 5000, "Cruiser" : 6000, "Destroyer" : 6000, "Submarine" : 0},
        23: {"AirCarrier" : 6000, "Battleship" : 5000, "Cruiser" : 6000, "Destroyer" : 6000, "Submarine" : 0},
        25: {"AirCarrier" : 10000, "Battleship" : 8000, "Cruiser" : 10000, "Destroyer" : 10000, "Submarine" : 0},
        26: {"AirCarrier" : 6000, "Battleship" : 5000, "Cruiser" : 6000, "Destroyer" : 6000, "Submarine" : 0},
        27: {"AirCarrier" : 10000, "Battleship" : 10000, "Cruiser" : 10000, "Destroyer" : 10000, "Submarine" : 0},
        28: {"AirCarrier" : 6000, "Battleship" : 5000, "Cruiser" : 6000, "Destroyer" : 6000, "Submarine" : 0},
        29: {"AirCarrier" : 6000, "Battleship" : 5000, "Cruiser" : 6000, "Destroyer" : 6000, "Submarine" : 0},
        30: {"AirCarrier" : 6000, "Battleship" : 5000, "Cruiser" : 6000, "Destroyer" : 6000, "Submarine" : 0},
        34: {"AirCarrier" : 6000, "Battleship" : 5000, "Cruiser" : 6000, "Destroyer" : 6000, "Submarine" : 0},
        35: {"AirCarrier" : 6000, "Battleship" : 5000, "Cruiser" : 6000, "Destroyer" : 6000, "Submarine" : 0},
    }

    _score = {
        1: 20.0,
        # 2: ,
        3: 1000.0 / 30.0,
        4: 15.0,
        5: 200.0,
        6: 20.0,
        7: 20.0,
        8: 50.0,
        9: 10.0,
        10: 200.0,
        11: 100.0,
        12: 20.0,
        13: 2.0,
        14: 1.0,
        15: 2.0,
        16: 0.5,
        17: 0.2,
        18: 20.0,
        19: 75.0,
        20: 2.0,
        21: 4.0,
        22: 2.0,
        23: 1.0,
        # 24: ,
        25: 4.0,
        26: 2.0,
        27: 1000.0 / 30.0,
        28: 0.2,
        29: 1.0,
        30: 1.0,
        34: 1.0,
        35: 1.0,
    }

    def __init__(self, ribbon_id):
        if ribbon_id in Ribbon._type_map:
            self._type = Ribbon._type_map[ribbon_id][0]
            self.file_name = Ribbon._type_map[ribbon_id][1]
            self.score = Ribbon._score[ribbon_id]
        else:
            self._type = Ribbon.RIBBON_UNKNOWN
            self.file_name = ""