#!/usr/bin/python


from copy import deepcopy


verbose = False


class Spell:

    def __init__(self, name, num, cost, damage=0, heal=0, effects=None, turns=None):
        self.name = name
        self.num = num
        self.cost = cost
        self.damage = damage
        self.heal = heal
        self.effects = effects        # (name, val)
        self.turns = turns


class Player:

    def __init__(self, name, hp, damage=0, mana=0):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.mana = mana
        self.armor = 0

    def effects_wear_off(self):
        # resets player to normal
        self.damage = 0
        self.armor = 0

    def heal(self, hp):
        self.hp += hp

    def apply(self, spell):
        for effect in spell.effects:
            x, y = effect

            if x == "mana":
                if verbose: print(f"{spell.name} provies {y} mana")
                self.mana += y
            if x == "armor":
                if verbose: print(f"{spell.name} increases armor by {y}; remaining turns {spell.turns-1}")
                self.armor += y
            if x == "damage":
                if verbose: print(f"{spell.name} deals {y} damage; remaining turns {spell.turns-1}")
                self.damage += y

    def apply_effects(self, effects):
        in_effect = []
        for spell in effects:
            self.apply(spell)
            spell.turns -= 1
            if spell.turns > 0:
                in_effect.append(spell)
        return in_effect

    def get_attacked(self, boss):
        # boss attacks player; reduces damage by at least 1 hp
        damage = boss.damage - self.armor
        if verbose: print(f"Boss attacks for {damage} damage")
        self.hp -= max(damage, 1)


class Boss(Player):

    def get_attacked(self, damage):
        # player attacks boss
        self.hp -= damage

    def get_attacked_effect(self, player):
        self.hp -= player.damage


SPELLS = [
    Spell("Magic Missile", "1", 53, damage=4),
    Spell("Drain", "2", 73, damage=2, heal=2),
    Spell("Shield", "3", 113, effects=[("armor", 7)], turns=6),
    Spell("Poison", "4", 173, effects=[("damage", 3)], turns=6),
    Spell("Recharge", "5", 229, effects=[("mana", 101)], turns=6),
]


def get_possible_spells(effects, mana):
    can_cast = []
    for sp in SPELLS:
        # if sp matches current spell in effect; cannot cast spell
        if sp.name in [s.name for s in effects]:
            continue
        if sp.cost > mana:
            continue
        can_cast.append(deepcopy(sp))
    return can_cast


def play(player, boss, in_effect, sp):
    if verbose:
        print(f"-- Player turn --")
        print(f"Player has {player.hp} hit points, {player.armor} armor, {player.mana} mana")
        print(f"Boss has {boss.hp} hit points")

    # cast spell
    player.mana -= sp.cost
    if sp.damage:
        string = f"Player casts {sp.name}, dealing {sp.damage} damage"
        string += f", healing {sp.heal} hp" if sp.heal else ""
        if verbose: print(string)
        boss.get_attacked(sp.damage)
        player.heal(sp.heal)
    else:
        if verbose: print(f"Player casts {sp.name}")

    # check if boss dead
    if boss.hp <= 0:
        return player, boss, in_effect, sp.cost

    if verbose: print(f"-- Boss turn --")

    # apply spell effects
    if sp.effects:
        in_effect.append(sp)

    s_in_effect = player.apply_effects(in_effect)

    if verbose:
        print(f"Player has {player.hp} hit points, {player.armor} armor, {player.mana} mana")
        print(f"Boss has {boss.hp} hit points")

    boss.get_attacked_effect(player)

    # boss attacks
    player.get_attacked(boss)
    player.effects_wear_off()
    return player, boss, s_in_effect, sp.cost


def get_state(player, boss, in_effect, mana_spent):
    return (
        player.hp,
        player.mana,
        boss.hp,
        "".join(sp.num for sp in in_effect),
        mana_spent
    )


def main(player, boss):
    min_mana = 1000000000000
    start = (
        "0",                                            # state_id
        Player("Player", player[0], mana=player[1]),    # player
        Boss("Boss", boss[0], damage=boss[1]),          # boss
        [],                                             # in_effect [spell]
        0                                               # mana spent
    )
    states = [start]
    seen = set()
    while states:
        state_id, player, boss, in_effect, mana_spent = states.pop(0)
        # import pdb; pdb.set_trace()

        # effects can be started on the same turn they end
        # apply effects and turn off any that no longer apply
        in_effect = player.apply_effects(in_effect)
        boss.get_attacked_effect(player)
        player.effects_wear_off()

        possible_spells = get_possible_spells(in_effect, player.mana)
        if not possible_spells:
            # cannot cast anything; player automatically loses
            continue

        for sp in possible_spells:
            if verbose: print(f"State: {state_id + sp.num}")
            nplayer, nboss, n_in_effect, sp.cost = play(
                deepcopy(player), deepcopy(boss), deepcopy(in_effect), sp
            )
            if nboss.hp <= 0:
                # player wins
                if verbose: print(f"This kills the boss, and the player wins.")
                min_mana = min(min_mana, mana_spent+sp.cost)
            elif nplayer.hp <= 0:
                # boss wins
                if verbose: print(f"Players dies, and the boss wins.")
            else:
                # player and boss still alive; continue game and save state
                # if we've never seen this state, don't have a better one
                seen_state = get_state(nplayer, nboss, n_in_effect, mana_spent+sp.cost)
                if seen_state not in seen:
                    seen.add(seen_state)
                    states.append(
                        (state_id + sp.num, nplayer, nboss, n_in_effect, mana_spent+sp.cost)
                    )
            if verbose: print()
        # import pdb; pdb.set_trace()
    return min_mana


if __name__ == '__main__':
    # print(f'Example {main((10, 250), (14, 8))}')
    print(f'Part 1 {main((50, 500), (71, 10))}')
