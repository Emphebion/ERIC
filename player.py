wildcards = ['wildcard1', 'wildcard2', 'wildcard3', 'wildcard4']

class Player:
    def __init__(self, name, rfid, skills):
        self.name = name
        self.rfid = rfid
        self.skills = skills

    def __str__(self):
        return 'Player {} ({}, {})'.format(self.name, self.rfid, list(self.skills))

    def add_skill(self, new_skill):
        if new_skill in wildcards:
            for skill_name in wildcards:
                if skill_name in self.skills:
                    self.skills.remove(skill_name)
        self.skills.add(new_skill)

class Players:
    def __init__(self, config):
        self.players = []
        self.rfidmap = {}
        playernames = map(str.strip, config.get('common','spelers').split(','))
        for playername in playernames:
            rfid = config.getint('spelers', playername)
            skills = set(map(str.strip, config.get('skills', playername).split(',')))
            player = Player(playername, rfid, skills)
            self.players.append(player)
            self.rfidmap[player.rfid] = player

    def find_player_for_rfid(self, responce):
        players = [None]
        for tag in responce:
            result = self.rfidmap.get(tag, None)
            if result:
                if players[0] == None:
                    players[0] = result
                else:
                    players.append(result)
        return players
