# coding=utf-8
from Ribbon import Ribbon

API_VERSION = 'API_v1.0'
MOD_NAME = 'YetAnotherRibbonSystem'
VERSION = '0.2.3'

def flash_log(ModName, msg):
    pass
    # utils.logInfo("flash_log: " + str(msg))

class YARS:

    __slots__ = ('MOD_DIR', 'RIBBONS_DIR', 'ShipType', 'players_health', 'StandarScore', 'Score', 'Level')

    def __init__(self):
        self.MOD_DIR = utils.getModDir()
        self.RIBBONS_DIR = self.MOD_DIR + '/Ribbons'
        self.ShipType = ""
        self.players_health = {}
        self.StandarScore = 1000.0
        self.Score = 1.0
        self.Level = 'N'
        flash.addExternalCallback("mlog", flash_log)
        self.setup_events()

    def on_flash_ready(self, state):
        self.register_assets()
        
    def showRibbon(self, ribbon_id, exist_time = 10000, alpha = 0.7):
        flash.call("Show", [ribbon_id, exist_time, alpha])

    def cleanRibbons(self, arg):
        flash.call("Clean", [])

    def setup_events(self):
        events.onFlashReady(self.on_flash_ready)
        events.onGotRibbon(self.on_got_ribbon)
        events.onBattleStart(self.on_battle_start)
        events.onBattleQuit(self.cleanRibbons)
        events.onSFMEvent(self.on_sfm_event)
        # events.onAchievementEarned(self.on_achievement_earned)
        events.onReceiveShellInfo(self.on_receive_shell_info)

    def on_achievement_earned(self, *args):
        pass
        # utils.logInfo('YetAnotherRibbonSystem achievement_earned', [args])
        # self.add_score(300.0)

    def on_receive_shell_info(self, victim_id, shooter_id, ammo_id, mat_id, shoot_id, booleans, damage, shot_position, yaw, hlinfo):
        #utils.logInfo('YetAnotherRibbonSystem', {'booleans': booleans,'damage': damage,})
        if booleans & 1 == 0:
            earned_score = float(damage) * self.StandarScore / float(self.players_health[victim_id])
            victim = battle.getPlayerByVehicleId(victim_id)
            shooter = battle.getPlayerByVehicleId(shooter_id)
            victim_sub_type = victim.shipInfo.subtype
            if victim_sub_type in ["Destroyer"]:
                earned_score *= 2.0
            elif victim_sub_type in ["AirCarrier", "Submarine"]:
                earned_score *= 1.5
            elif victim_sub_type in ["Cruiser"]:
                earned_score *= 1.2
            victim_level = victim.shipInfo.level
            shooter_level = shooter.shipInfo.level
            earned_score *= 1.0 + float(victim_level - shooter_level) * 0.1
            # utils.logInfo('YetAnotherRibbonSystem calculate score', [{'damage': damage, 'earned_score': earned_score, 'victim_sub_type': victim_sub_type, 'mx_health': self.players_health[victim_id]}])
            self.add_score(earned_score)    


    def on_sfm_event(self, event_name, event_data):
        #utils.logInfo('YetAnotherRibbonSystem', {'event_name': event_name,'event_data': event_data,})
        if event_name == 'window.show' and event_data['windowName'] == 'GameMenu':
            flash.call("HideAll", [])
        elif event_name == 'window.hide' and event_data['windowName'] == 'GameMenu':
            flash.call("ShowAll", [])

    def on_battle_start(self):
        mShip = battle.getSelfPlayerShip()
        self.ShipType = mShip.subtype
        players_info_collection = battle.getPlayersInfo()
        self.players_health = {}
        self.Score = 0
        for playerId in players_info_collection:
            player_info = players_info_collection[playerId]
            if player_info.teamId == 1:
                self.players_health[player_info.shipId] = player_info.maxHealth
        flash.call("UpdateLevel", [self.Level, 0.5])

    def on_got_ribbon(self, ribbon_id, a_value):
        ribbon = Ribbon(ribbon_id)
        if ribbon._type != Ribbon.RIBBON_UNKNOWN:
            if self.ShipType in ["AirCarrier", "Battleship", "Cruiser", "Destroyer", "Submarine"]:
                exciting_time = Ribbon._exciting_time[ribbon_id][self.ShipType]
                self.showRibbon(ribbon_id, exciting_time)
            else:
                self.showRibbon(ribbon_id)
            self.add_score(ribbon.score)

    def add_score(self, score):
        self.Score += score
        # utils.logInfo("Score: " + str(self.Score))
        new_level = self.get_level()
        if new_level != self.Level:
            self.Level = new_level
            flash.call("UpdateLevel", [self.Level, 0.5])
        if score > 10:
            flash.call("ShakeLevel", [int(score), 100, 5])

    def get_level(self):
        if self.Score < 600.0:
            return 'N'
        elif self.Score < 1400.0:
            return 'R'
        elif self.Score < 2800.0:
            return 'SR'
        elif self.Score < 3800.0:
            return 'SSR'
        elif self.Score < 5500.0:
            return 'PRY'
        elif self.Score < 8000.0:
            return 'UR'
        else:
            return 'DR'

    def register_assets(self):
        for key, value in Ribbon._type_map.items():
            file_path = self.RIBBONS_DIR + '/' + value[1]
            if utils.isPathExists(file_path):
                flash.call("Register", [key, file_path])
        for level in ['N', 'R', 'SR', 'SSR', 'PRY', 'UR', 'DR']:
            file_path = self.MOD_DIR + '/Level/' + level + '.png'
            if utils.isPathExists(file_path):
                flash.call("RegisterLevel", [level, file_path])

#devmenu.enable()

g_YARS = YARS()
