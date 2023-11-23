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
