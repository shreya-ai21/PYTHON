class User:
    def __init__(self,username,id):
        self.username=username
        self.id=id
        self.followers=0
        self.following=0

    def follow(self,user):
        user.followers+=1
        self.following+=1

user1=User('Shreya','001')
user2=User('Ninni','002')
user1.follow(user2)
user2.follow(user1)