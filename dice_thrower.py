import random

# heiti      : Die.
# notað      : K2 verkefni.
# hlutverk   : Hjúpar virkni eins tenings.
# lýsing     : klasinn inniheldur eina breytu(töluna á teningnum) og aðferðina throw()
# höfundur   : Sigurdur R. Ragnarsson
# dagsetning : 11.09.2016
# uppfært    : komment þýdd 23.09.2018
class Die:
    def __init__(self):
        self.number = 0

    # throw aðferðin gerir ráð fyrir sex hliða teningi
    # með tölunum 1 til og með 6
    def throw(self):
        self.number = random.randint(1, 6)
        return self.number


# heiti	     : DiceThrower.
# notað      : K2 verkefni.
# hlutverk	 : inniheldur lista af teningum.
# lýsing	   : klasinn getur unnið með mismarga teninga, kastað þeim og endurkastað
# höfundur   : Sigurdur R. Ragnarsson
# dagsetning : 11.09.2016
# uppfært    : komment þýdd 23.09.2018
class DiceThrower:
    def __init__(self, how_many=5):  # sjálfgefið eru 5 teningar
        self.number_of_dice = how_many
        self.dice = Die()
        self.dice_list = [0 for i in range(self.number_of_dice)]

    # kastar öllum teningunum í listanum
    def throw(self):
        for x in range(0, self.number_of_dice):
            self.dice_list[x] = self.dice.throw()
        return self.dice_list

    # endurkastar þeim teningum sem eru í rethrow-listanum.
    # ATH: sá listi inniheldur staðsetningu(indexa) teninganna
    #  í listanum ekki tölurnar sjálfar.
    def rethrow(self, rethrow_list=[]):
        if 0 < len(rethrow_list) <= self.number_of_dice:
            if min(rethrow_list) >= 0 and max(rethrow_list) <= self.number_of_dice - 1:
                for item in rethrow_list:
                    self.dice_list[item] = self.dice.throw()
            return self.dice_list
        else:
            return self.throw()
