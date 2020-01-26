def getShare(row): #z řádku z katastru vrátí podíl vlastnictví
    share = row.split('\t')[-1]
    numerator = int(share.split('/')[0])
    denumerator = int(share.split('/')[1][:-1])
    return numerator * 1.0 /  denumerator


def compareRow(first, second):
    if getShare(first) - getShare(second) > 0.0000001:
        print('compare',first,"---",second)

def clearSJM(ownerList): #vyčistí ty dva 'bonusové' řádky u SJM
    if ownerList[0][:3] == 'SJM' and len(ownerList) >=3:
        surname = ownerList[0].split()[1]
        if surname in ownerList[1]:
            ownerList.pop(1)
        if surname in ownerList[1]: #toto je dvakrát protože odstraňuji dva manželé
            ownerList.pop(1)

def compareFile(first, second):
    solo = [] # vlastníci kteří jsou pouze v jednom listu
    while True:
        if len(first) == 0:
            return solo + list(zip([1]*len(second),second))
        if len(second) == 0:
            return solo + list(zip([2]*len(first),first))
        clearSJM(first)
        clearSJM(second)
        if first[0][:7] == second[0][:7]:
            compareRow(first.pop(0),second.pop(0))
        else:
            if first[0] < second[0]:
                solo.append((1,first.pop(0)))
            else:
                solo.append((2,second.pop(0)))

###################################

with open('1083-2') as f:
  okoli = f.readlines()

with open('1083-64') as f:
  garaz = f.readlines()

owners = compareFile(okoli, garaz )
for site, owner in owners:
    pass
    print(site, owner[:-1])
