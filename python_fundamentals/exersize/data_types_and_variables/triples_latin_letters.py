number_for_character = int(input())
for i in range(0 , number_for_character):
    for j in range(0, number_for_character):
        for k in range(0, number_for_character):
            i_character = chr(97 + i)
            j_character = chr(97 + j)
            k_character = chr(97 + k)
            print(f'{i_character}{j_character}{k_character}')
