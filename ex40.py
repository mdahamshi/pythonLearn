

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_cday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"
])

bulls_on_parade = Song(["They rally around the family",
                    "With pockets full of shells"
])

happy_cday.sing_me_a_song()
print '-'*10
bulls_on_parade.sing_me_a_song()