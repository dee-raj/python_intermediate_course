unit = {"AI": 11.9, "STQA":11.9, "INS":12.9, "CF":12.9, "PM":13.9}
print("orgin Unit: ",unit)

theory = dict(ai=12.12, ins=13.12, STQA=14.12, CF=15.12, Project=16.12)
print("orgin theory: ",theory)


#updated
unit.update(theory)
print("\nupdated Unit: ",unit)

theory.update(unit)
print("updated theory: ",theory)