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
        surname = ownerList[0].split()[1][:-2] # krátím společné příjmení kvůli skloňování
        if surname in ownerList[1] and surname in ownerList[2]:
            ownerList.pop(1) #manžel 
            ownerList.pop(1) #manželka

def alfabeticalyFirst(ownerList1, ownerList2): #vrátí ten list, který má první prvek abecedně nejvýš SJM se nepočítá
    def cutSJM(row):
        if row[:3] == 'SJM':
            return row[4:]
        else:
            return row
    row1 = cutSJM(ownerList1[0])
    row2 = cutSJM(ownerList2[0])
    if row1 < row2:
        return 1, ownerList1
    else:
        return 2, ownerList2
    

def compareFile(ownerList1, ownerList2):
    solo = [] # vlastníci kteří jsou pouze v jednom listu
    while True:
        if len(ownerList1) == 0:
            return solo + list(zip([1]*len(ownerList2),ownerList2))
        if len(ownerList2) == 0:
            return solo + list(zip([2]*len(ownerList1),ownerList1))
        clearSJM(ownerList1)
        clearSJM(ownerList2)
        if ownerList1[0][:7] == ownerList2[0][:7]:
            compareRow(ownerList1.pop(0),ownerList2.pop(0))
        else:
            site, ownerList = alfabeticalyFirst(ownerList1, ownerList2)
            solo.append((site,ownerList.pop(0)))

###################################

with open('1083-2') as f:
  okoli = f.readlines()
with open('1083-74') as f:
  prijezd = f.readlines()
with open('1083-64') as f:
  garaz = f.readlines()
with open('1083-65') as f:
  klubovna = f.readlines()
with open('1083-90') as f:
  mycka = f.readlines()
with open('stavba') as f:
  stavba = f.readlines()

#owners = compareFile(okoli, garaz )
#owners = compareFile(prijezd, garaz )
owners = compareFile(okoli, stavba)
for site, owner in owners:
    pass
    print(site, owner[:-1])
