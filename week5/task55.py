def search_and_count():
    searchable = input("Enter the input to search: ")

    item = input("Which item do you want to search?: ")
  
    count_result = searchable.count(item)
    
    print(f"item {item} appeared {count_result} times")

search_and_count()