# def cast_spell(dictionary: dict , name: str , mp_needed: int , spell: str):
#     if name in dictionary.keys():
#         current_mp = dictionary[hero]
#         if current_mp >= mp_needed:
#             dictionary[name] -= mp_needed
#             current_mp = dictionary[hero]
#             print(f"{name} has successfully cast {spell} and now has {current_mp} MP!")
#         else:
#             print(f"{name} does not have enough MP to cast {spell}!")
#     return dictionary
#
#
# def take_damage(dictionary: dict , name: str , damage: int , attacker: str):
#     if name in dictionary.keys():
#         dictionary[name] -= damage
#         current_hp = dictionary[name]
#         if current_hp > 0:
#             print(f"{name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
#         else:
#             print(f"{name} has been killed by {attacker}!")
#             del dictionary[name]
#     return dictionary
#
#
# def recharge(dictionary , name , amount , max_mp):
#     if name in dictionary.keys():
#         current_mp = dictionary[name]
#         dictionary[name] = min(current_mp + amount , max_mp)
#         recharged = min(max_mp - current_mp , amount)
#         print(f"{name} recharged for {recharged} MP!")
#     return dictionary
#
#
# def heal(dictionary: dict , name: str , amount: int , max_hp: int):
#     if name in dictionary.keys():
#         current_hp = dictionary[name]
#         dictionary[name] = min(current_hp + amount , max_hp)
#         healed = min(max_hp - current_hp , amount)
#         print(f"{name} healed for {healed} HP!")
#     return dictionary
#
#
# number_of_heroes = int(input())
# heroes_mp_dict = {}
# heroes_hp_dict = {}
# hit_points_max = 100
# mana_points_max = 200
# for number in range(number_of_heroes):
#     hero , hit_points , mana_points = input().split()
#     if int(hit_points) > hit_points_max:
#         hit_points = hit_points_max
#     if int(mana_points) > mana_points_max:
#         mana_points = mana_points_max
#     heroes_hp_dict[hero] = int(hit_points)
#     heroes_mp_dict[hero] = int(mana_points)
#
# while True:
#     command = input().split(" - ")
#     if command[0] == 'End':
#         break
#     if command[0] == "CastSpell":
#         hero_name = command[1]
#         mana_points_needed = int(command[2])
#         spell_name = command[3]
#         heroes_dict = cast_spell(heroes_mp_dict , hero_name , mana_points_needed , spell_name)
#     elif command[0] == 'TakeDamage':
#         hero_name = command[1]
#         damage_hit_points = int(command[2])
#         attacker_name = command[3]
#         heroes_dict = take_damage(heroes_hp_dict , hero_name , damage_hit_points , attacker_name)
#     elif command[0] == 'Recharge':
#         hero_name = command[1]
#         recharge_amount = int(command[2])
#         heroes_dict = recharge(heroes_mp_dict , hero_name , recharge_amount , mana_points_max)
#     elif command[0] == 'Heal':
#         hero_name = command[1]
#         healed_amount = int(command[2])
#         heroes_dict = heal(heroes_hp_dict , hero_name , healed_amount , hit_points_max)
# for hero_name in heroes_hp_dict.keys():
#     hero_mp = heroes_mp_dict[hero_name]
#     hero_hp = heroes_hp_dict[hero_name]
#     print(f"{hero_name}\n"
#           f"  HP: {hero_hp}\n"
#           f"  MP: {hero_mp}")
def hero_creation(name , hp , mp):
    return {'name': name , 'hp': hp , 'mp': mp}


def spell_cast(hero , mp , spell):
    if hero['mp'] >= mp:
        hero['mp'] -= mp
        print(f"{hero['name']} has successfully cast {spell} and now has {hero['mp']} MP!")
    else:
        print(f"{hero['name']} does not have enough MP to cast {spell}!")


def take_damage(hero , damage_taken , attacker_name):
    hero['hp'] -= damage_taken
    if hero['hp'] > 0:
        print(f"{hero['name']} was hit for {damage_taken} HP by {attacker_name} and now has {hero['hp']} HP left!")
        return False
    else:
        print(f"{hero['name']} has been killed by {attacker_name}!")
        return True


def recharge(hero , max_mp , mp_recharge):
    mp_to_recharge = min(mp_recharge , max_mp - hero['mp'])
    hero['mp'] += mp_to_recharge
    print(f"{hero['name']} recharged for {mp_to_recharge} MP!")


def heal(hero , max_hp , hp_heal):
    hp_healed = min(hp_heal , max_hp - hero['hp'])
    hero['hp'] += hp_healed
    print(f"{hero['name']} healed for {hp_healed} HP!")


def main_function():
    number_of_heroes = int(input())
    heroes = []
    for number in range(number_of_heroes):
        hero_attributes = input().split()
        hero_name = hero_attributes[0]
        hero_hp = int(hero_attributes[1])
        hero_mp = int(hero_attributes[2])
        hero = hero_creation(hero_name , hero_hp , hero_mp)
        heroes.append(hero)

    max_hp = 100
    max_mp = 200

    while True:
        command = input()
        if command == "End":
            break

        action_to_perform = command.split(' - ')
        action = action_to_perform[0]
        hero_name = action_to_perform[1]
        for hero in heroes:
            if hero['name'] == hero_name:
                if action == 'CastSpell':
                    required_mp = int(action_to_perform[2])
                    spell_name = action_to_perform[3]
                    spell_cast(hero , required_mp , spell_name)
                elif action == 'TakeDamage':
                    damage_taken = int(action_to_perform[2])
                    attacker_name = action_to_perform[3]
                    if take_damage(hero , damage_taken , attacker_name):
                        heroes.remove(hero)
                elif action == 'Recharge':
                    mp_recharge = int(action_to_perform[2])
                    recharge(hero , max_mp , mp_recharge)
                elif action == 'Heal':
                    hp_heal = int(action_to_perform[2])
                    heal(hero , max_hp , hp_heal)
    for hero in heroes:
        print(f"{hero['name']}\n  HP: {hero['hp']}\n  MP: {hero['mp']}")


main_function()
