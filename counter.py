def count_characters(input_string):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    d_count = 0
    s_count = 0
 
    for char in input_string:
        if char.isalpha():
            if char in vowels:
                v_count+=1
            else:
                c_count+=1
        elif char.isdigit():
            d_count+=1
        else:
            s_count+=1
    print(f"vowels: {v_count}")
    print(f"consonants: {c_count}")
    print(f"Digits: {d_count}")
    print(f"Special Characters: {s_count}")
    
    text = input("Enter a string:")
    count_characters(text)