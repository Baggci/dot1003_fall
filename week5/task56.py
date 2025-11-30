
def clear_vowels(text):
    vowels = "aeiouAEIOU"  
    result = ""           
    
    for char in text:     
        if char not in vowels: 
            result += char      
            
    return result         

menu_button = "new game"

print(clear_vowels(menu_button))