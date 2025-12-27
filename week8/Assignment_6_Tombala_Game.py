import random
def generate_card():
    card = []
    while len(card) < 5:
        num = random.randint(1, 99)
        if num not in card:
            card.append(num) 
    return card

print("--- Tombala Game ---")
user_name = input("Lütfen kullanıcı adınızı giriniz: ") 

cards = []
for i in range(4):
    cards.append(generate_card())

print("Mevcut Kartlar:")
for i in range(len(cards)):
    print(f"Kart {i+1}: {cards[i]}")

try:
    choice = int(input("Bir kart seçiniz (1-4): ")) - 1
    my_card = cards[choice]
except:
    print("Geçersiz giriş, ilk kart otomatik seçildi.")
    my_card = cards[0]

print(f"Seçilen Kart: {my_card}")

draws = []
found_on_card = []
game_result = "Kaybettiniz"

flag = True
count = 0
while flag and count < 10:
    draw = random.randint(1, 99)
    draws.append(draw)
    print(f"\nÇekilen Sayı: {draw}")
    
    ans = input("Kartınızda var mı? (evet/hayır): ")
    
    is_present = draw in my_card
    
    if ans == "evet":
        if is_present:
            if draw not in found_on_card:
                found_on_card.append(draw)
                print("Doğru bildiniz!")
        else:
            print("Yanlış! Sayı kartınızda yok (Hileci).")
    
    if len(found_on_card) == len(my_card):
        game_result = "Kazandınız"
        print("TOMBALA! Kazandınız!")
        flag = False
    
    count += 1

with open("log.txt", "a") as my_file:
    my_file.write(f"oyuncu: {user_name}\n")
    my_file.write(f"Kart: {my_card}\n")
    my_file.write(f"Cekilen Sayilar: {draws}\n")
    my_file.write(f"Sonuc: {game_result}\n")
    my_file.write("-" * 20 + "\n")

print("Oyun bitti, veriler log.txt dosyasina kaydedildi.") 