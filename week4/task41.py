def compare_strings(word1, word2):
 
    len1 = len(word1)
    len2 = len(word2)
    
    if len1 > len2:
        return word1 
    elif len2 > len1:
        return word2  
    else:
        print("Their length are same") 
        return None  

input1 = input("First Word: ")
input2 = input("Second Word: ")

result = compare_strings(input1, input2)

if result:
  print(result)