import random

def main():
    list_size = int(input("List Size: "))

    element_type = input("Element Type: ").strip().lower()

    random_list = []

  
    if element_type == "integer":
        for _ in range(list_size):
       
            random_list.append(random.randint(0, 999999))
            
    elif element_type == "float":
        for _ in range(list_size):
        
            random_list.append(random.uniform(0, 999999))
            
    else:
        print("Hatali giriş! Lütfen 'integer' veya 'float' yazin.")
        return

    
    print("Here is your random list you asked for:")
    print(random_list)

if __name__ == "__main__":
    main()