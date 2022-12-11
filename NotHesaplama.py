print("Merhaba, ADU Almanca Hazirlik Not Hesaplama Sistemine Hosgeldiniz")
print("Lutfen 1. Donem notlarinizi giriniz: ")
q1 = input('1. Quiz Hörverstehen: ')
q2 = input('2. Quiz Grammatik: ')
q3 = input('3. Quiz Wortschatz: ')
q4 = input('4. Quiz Schreiben: ')
q5 = input('5. Quiz Sprechen: ')
v1 = input('Vize 1: ')
v2 = input('Vize 2: ')
ortalamaquiz=(float(q1)*2)+(float(q2)*2)+(float(q3*2)/12)
ortalamavize=(float(q1)*9)+(float(q2)*9)/18
notoquiz = ortalamaquiz / 12
notovize = ortalamavize / 18
print("Quiz Ortalamaniz : ",ortalamaquiz / 12)
print("Vize Ortalamaniz : ",ortalamavize / 18)
print("Dönem Not Ortalamaniz : ",notoquiz + notovize / 2)