def find_substring_indices(main_str, sub_str):
    indices=[]
    start = 0
    while True:
        pos = main_str.find(sub_str, start)
        if pos ==-1:
            break
        indices.append(pos)
        start = pos+1
    return indices
text = "abababa"
sub="aba"
print(f"Substring found at indices: {find_substring_indices}")