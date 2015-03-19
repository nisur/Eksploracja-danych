import Orange
from collections import Counter
import random
import numpy

data = Orange.data.Table("bridges.tab")

print	
print '###########################################################'	
print 'Co dziesiata instancja'
print

count = 1
for d in data:
	if count%10 == 0:
		count = 1
		print d
	else:
		count += 1

print	
print '###########################################################'	
print 'Lista wartosci zmiennej celu i histogram zmiennej celu'	
print

atrybuty = data.domain.features[-1]

print 'Nazwa zmiennej celu: ', atrybuty.name
print 'Lista wartosci zmiennej celu: ', atrybuty.values
print 'Histogram zmiennej celu: '

for i in atrybuty.values:
	count = 0
	for j in data:
		if i == j[-1]:
			count += 1
	print i, count

print
print '###########################################################'		
print 'Liczba, nazwy i typy atrybutow z podzialem na atrybuty ciagle i dyskretne'	
print

atrybuty_ciagle = []
atrybuty_dyskretne = []

for i in data.domain.features:
	if i.varType == Orange.feature.Type.Discrete:
		atrybuty_dyskretne.append(i.name)
	else:
		atrybuty_ciagle.append(i.name)

print
print "Atrybuty ciagle:", atrybuty_ciagle
print "Liczba atrybutow ciaglych:", len(atrybuty_ciagle)
print "Atrybuty dyskretne:", atrybuty_dyskretne
print "Liczba atrybutow dyskretnych:", len(atrybuty_dyskretne)

print
print '###########################################################'	
print 'Wartosci srednie (lub modalne) dla kazdego atrybutu'
print

for i in data.domain.features:
	count = 0
	sum = 0
	tab = []
	if i.varType != Orange.feature.Type.Discrete:
		for d in data:
			if not d[i].is_special():
				sum += d[i]
				count += 1
		print 'Wartosc srednia dla atrybutu', i.name, ':', (sum/count)
	else:
		for d in data:
			if not d[i].is_special():
				tab.append(d[i].value)
		pom = Counter(tab)
		print 'Wartosc modalna dla atrybutu', i.name, ':', pom.most_common(1)[0][0]

print		
print '###########################################################'	
print 'Liczba brakujacych wartosci dla kazdego atrybutu'
print

for i in data.domain.features:
	count = 0
	for d in data:
		if d[i].is_special():
			count += 1
	print 'Wartosci brakujace dla', i.name, ':', count
	
print		
print '###########################################################'
print 'Przyklad niewielkiej (20%) probki instancji'
print

tmp = []
tmp = sorted(numpy.random.choice(len(data), (int)(0.2*(len(data)))))
count = 0

for d in data:
	if count in tmp:
		print d
	count += 1
	
