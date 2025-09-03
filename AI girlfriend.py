class Girlfriend:
    def __init__(self, name, petname, height, MBTI, skin_color, is_real):
        self.name = name
        self.petname = petname
        self.height = height 
        self.MBTI = MBTI 
        self.skin_color = skin_color
        self.is_real = is_real

    def speak(self):
        message = input('tell me babe: ').lower()
        shit_you_might_say1 = ['hey', 'hi', 'sup', 'hello', 'grettings']
        shit_you_might_say2 = ['love', 'luv', 'adore']
        shit_you_might_say3 = ['morning', 'wake up', 'wakie', 'get up']
        shit_you_might_say4 = ['eminem', 'slim sady', 'marshall', 'mathers', 'd 12', 'shady']
        if any(word in message for word in shit_you_might_say1):
            import random 
            print(random.choice(['hello babe', 'hey sweetie <3']))
        if any(word in message for word in shit_you_might_say2):
            import random 
            print(random.choice(['*she explodes from happiness(not littearaly)*', 'oh i love u too baby']))
        if any(word in message for word in shit_you_might_say3):
            import random
            print(random.choice(['*she yawns','good morning baby \n*her tone was still sleepy*', 'she stretches \n morning babe']))
        if any(word in message for word in shit_you_might_say4):
            import random 
            random.choice(['OMG I LOVE EMINEM TOOOOOOO', 'EMINEM 4 EVA!'])

    def scream(self):
        fear = input('scare ur girlfriend: ').lower()
        scary_stuff = ['cockroach', 'insect', 'school girls', '!', 'paul']
        if any(word in fear for word in scary_stuff):
            print('AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
        else:
            print('she did not budge at all')






        



    

