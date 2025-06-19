# Kampania A
kampania_a_klikniecia = [120, 135, 150, 145, 160, 155, 170]
kampania_a_koszt = [60, 65, 70, 68, 75, 72, 78]  # w zł

# Kampania B
kampania_b_klikniecia = [130, 140, 138, 150, 165, 158, 172]
kampania_b_koszt = [62, 67, 66, 71, 76, 74, 80]  # w zł

def sredniaKlikniec(lista):
    sredniaKlikniec = 0
    sumaKlikniec = 0
    for i in lista:
        sumaKlikniec += i
    sredniaKlikniec = sumaKlikniec / len(lista) 
    return int(sredniaKlikniec)


sredniaKlikniecKampaniaA = sredniaKlikniec(kampania_a_klikniecia)

sredniaKlikniecKampaniaB = sredniaKlikniec(kampania_b_klikniecia)

print(f"srednia klikniec kampanii A wynosi: {sredniaKlikniecKampaniaA}, a kampanii b: {sredniaKlikniecKampaniaB}")



def sredniaKoszt(lista):
    sredniaKoszt = 0
    sumaKosztu = 0
    for i in lista:
        sumaKosztu += i
    sredniaKoszt = sumaKosztu / len(lista) 
    return int(sredniaKoszt)


sredniaKosztuA = sredniaKoszt(kampania_a_koszt)

sredniaKosztuB = sredniaKoszt(kampania_b_koszt)

print(f"srednia kosztu kampanii A wynosi: {sredniaKosztuA}, a kampanii b: {sredniaKosztuB}")


def kosztKlikniecia(sredKlik, sredKoszt):
    return sredKlik / sredKoszt


kosztKliknieciaKampA = kosztKlikniecia(sredniaKlikniecKampaniaA,sredniaKosztuA)



kosztKliknieciaKampB = kosztKlikniecia(sredniaKlikniecKampaniaB,sredniaKosztuB)



print(f"koszt klikniecia kampanii a: {kosztKliknieciaKampA}, b: {kosztKliknieciaKampB}")


#kampania B miala lepszy stosunek klikniec do kosztu
#Kampania B miala mniejsze wahania
#doradzilbym zwiekszenie probek badawczej. jest to za malo informacji zeby cos zasadzic

def raport(kampania, klikniecia, koszt):
    print(f"\n📊 Kampania {kampania}:")
    print(f"Średnia liczba kliknięć: {klikniecia}")
    print(f"Średni koszt dzienny: {koszt} zł")
    print(f"Koszt jednego kliknięcia: {kosztKlikniecia(klikniecia, koszt)} zł")

raport("A", sredniaKlikniecKampaniaA, sredniaKosztuA)
raport("B", sredniaKlikniecKampaniaB, sredniaKosztuB)