#metro = float(input('Digite uma medida em metros'))

#km = metro/1000
#hm = metro/100
#dam = metro/10
#dm = metro*10
#cm = metro*100
#mm = metro*1000

#print('A medida de {} corresponde a '.format(metro))
#print('{}km'.format(km))
#print('{}hm'.format(hm))
#print('{}dm'.format(dam))
#print('{}cm'.format(cm))
#print('{}mm'.format(mm))


medida = float(input('Digite uma medida em metros: '))

km = medida/1000
hm = medida/100
dam = medida/10
dm = medida*10
cm = medida*100
mm = medida*1000

print(f'A medida de {medida} corresponde a ')
print(f'{km}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{dm:.0f}dm')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm')
