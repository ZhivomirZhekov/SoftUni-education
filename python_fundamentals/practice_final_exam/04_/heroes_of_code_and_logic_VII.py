def cast_spell(heroes , hero_name , mp_need , spell_name):
    if hero_name in heroes.keys():
        if heroes[hero_name]['mp'] >= mp_need:
            heroes[hero_name]['mp'] -= mp_need
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    return heroes


def take_damage(heroes , hero_name , damage , attacker):
    if hero_name in heroes.keys():
        heroes[hero_name]['hp'] -= damage
        if heroes[hero_name]['hp'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hp']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]
    return heroes


def recharge(heroes , hero_name , amount , max_mp):
    if hero_name in heroes.keys():
        before_recharge = heroes[hero_name]['mp']
        heroes[hero_name]['mp'] = min(max_mp , before_recharge + amount)
        recharged = heroes[hero_name]['mp'] - before_recharge
        print(f"{hero_name} recharged for {recharged} MP!")
    return heroes


def heal(heroes , hero_name , amount , max_hp):
    if hero_name in heroes.keys():
        before_heal = heroes[hero_name]['hp']
        heroes[hero_name]['hp'] = min(max_hp , before_heal + amount)
        healed = heroes[hero_name]['hp'] - before_heal
        print(f"{hero_name} healed for {healed} HP!")
    return heroes


def main_funtion():
    number_of_heroes = int(input())
    heroes = {}
    for _ in range(number_of_heroes):
        hero = input().split(" ")
        hero_name , hp , mp = hero[0] , int(hero[1]) , int(hero[2])
        if hero_name not in heroes.keys():
            heroes[hero_name] = {}
        heroes[hero_name]['hp'] = hp
        heroes[hero_name]['mp'] = mp

    max_hp = 100
    max_mp = 200
    while True:
        command = input().split(" - ")
        action = command[0]
        if action == "End":
            break

        if action == "CastSpell":
            hero_name = command[1]
            mp_need = int(command[2])
            spell_name = command[3]
            heroes = cast_spell(heroes , hero_name , mp_need , spell_name)
        elif action == "TakeDamage":
            hero_name = command[1]
            damage = int(command[2])
            attacker = command[3]
            heroes = take_damage(heroes , hero_name , damage , attacker)
        elif action == "Recharge":
            hero_name = command[1]
            amount = int(command[2])
            heroes = recharge(heroes , hero_name , amount , max_mp)
        elif action == "Heal":
            hero_name = command[1]
            amount = int(command[2])
            heroes = heal(heroes , hero_name , amount , max_hp)

    for hero , attributes in heroes.items():
        hp = attributes['hp']
        mp = attributes['mp']
        print(f"{hero}\n  HP: {hp}\n  MP: {mp}")


main_funtion()
