from src.db import connect_mongoengine
from src.models import Player

def show_players_over_25(limit=5):
    connect_mongoengine()
    players = Player.objects(age__gte=25).limit(limit)
    for p in players:
        print(p.id, p.name, p.age, p.club)

def update_dayot_age():
    connect_mongoengine()
    updated = Player.objects(name="Dayot Upamecano").update(set__age=25)
    print("Updated documents:", updated)

def create_new_player():
    connect_mongoengine()
    player = Player(
        name="Harry Kane",
        age=30,
        height=1.88,
        nationality="England",
        price=100000000,
        max_price=150000000,
        position="Attack - Centre-Forward",
        club="Bayern Munich"
    )
    player.save()
    print("Created player with id:", player.id)

if __name__ == "__main__":
    show_players_over_25()
    create_new_player()