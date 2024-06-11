class Game:
    def __init__(self, title):
        self._title = title
        
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, new_title):
        # if not hasattr(self, '_title'): 
        #     if isinstance(new_title, str) and len(new_title) <= 0: #hasattr if it has a title already or not.
        #         self._title = new_title
        #     else:
        #         print('title must be string with more than 0 chars')
        # else:
        #     print('title is already set')
        
        if hasattr(self, '_title'):
            print('title already set')
            return
        if not isinstance(new_title, str):
            print('title must be string')
            return
        if len(new_title) == 0:
            print('title must be greater than 0 char')
            return
        
    def results(self):
        # Loop through Results.all and check for the same Game, and return results
        result_list = []
        for result in Result.all:
            if result.game is self:
                result_list.append(result)
        return result_list

    def players(self):
        players = []
        for result in self.results():
            players.append(result.player)
        return list(set(players))

    def average_score(self, player):
        sum = 0
        length = 0
        for result in self.results():
            if result.player is player:
                sum += result.score
                length += 1
        return (sum / length)
    
    def __repr__(self) -> str:
        return f'<Game {self.title}>'

class Player:
    @classmethod
    def highest_scored(self, game):
        players = game.players()
        
        if len(players) == 0:
            return None
        
        max_player = players[0]
        max_player_avg = game.average_score(max_player)
        for player in players:
            avg = game.average_score(player)
            if avg > max_player_avg:
                max_player = player
                max_player_avg = avg
        return max_player
        # return max(players, key=lambda player: game.average_score(player))
    
    def __init__(self, username):
        self._username = username
        
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str):
            print('username must be a string')
            return
        if not (2 <= len(new_username) <= 16):
            print('username must be between 2 to 16 characters')
            return
        self._username = new_username

    def results(self):
        result_list = []
        for result_obj in Result.all:
            if result_obj.player is self:
                result_list.append(result_obj)
        return result_list
                

    def games_played(self):
        games = []
        for result in self.results():
            games.append(result.game)
        return list(set(games))
                

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        count = 0
        for result in self.results():
            if result.game is game:
                count +=1
        return count
    
    def __repr__(self) -> str:
        return f'<Player {self.username}>'

class Result:
    
    all = []
    
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if hasattr(self, '_score'):
            print('score has already been set')
            return 
        if not isinstance(new_score, int):
            print('score must be an integer')
            return
        if not (1 <= new_score <= 5000):
            print('score must be between 1 and 5000')
            return
        self._score = new_score
        
    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, new_player):
        if isinstance(new_player, Player):
            self._player = new_player
        else:
            print('invalid player')
            
    @property
    def game(self):
        return self._game
    @game.setter
    def game(self, new_game):
        if isinstance(new_game, Game):
            self._game = new_game
        else:
            print('invalid game')
            
    def __repr__(self) -> str:
        return f'<Result {self.score} {self.game.title} {self.player.username}>'

# TESTING
g1 = Game('Pacman')
g2 = Game('galaga')
g3 = Game('Checkers')

g1.title = 'test'

print("g1 title", g1.title)

p1 = Player('J')
p2 = Player('Ali')
print("p1 username", p1.username)

r1 = Result(p1, g1, 3000)
r2 = Result(p2, g1, 4000)
r3 = Result(p2, g1, 600)
r4 = Result(p2, g2, 1000)
print("r1 score", r1.score)

print("all results:", Result.all)

print("p2 results", p1.results())

print("games played for p2:", p2.games_played())

print("players for p1", g1.players())

print("did p1 play g1?" , p1.played_game(g1))

print("did p1 play g2?", p1.played_game(g2))

print("how many times p2 play g1?" , p2.num_times_played(g1))

print("g1 average score for p2", g1.average_score(p2))

print("g1 average score for p1", g1.average_score(p1))

print("highest scored in game g1", Player.highest_scored(g1))

print("highest scored in game g3", Player.highest_scored(g3))