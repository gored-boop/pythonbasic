word = "bottles" # 단어 지정 'bottles를 호출할 용어로 word 지정
for beer_num in range(99,0,-1): #99부터 0까지 반복해서 1씩감소
    print(beer_num, word, "of beer on the wall") #beer_num의 숫자를 가져오고 ""사이의 문자를 출력
    print(beer_num, "of beer.") #beer_num의 숫자를 가져오고 ""사이의 문자를 출력
    print("Take on down.") #""사이의 문자 출력
    print("pass it around.")#""사이의 문자 출력
    if beer_num == 1: #beer_num 의 숫자가 1이 되면,
        print("No more bottles of beer in the wall.") #""사이의 문자 출력
    else: #beer_num의 숫자가 1이 아니면
        new_num = beer_num - 1 #new_num은 남은수 할당
        if new_num == 1: # new_num 의 값이 1이면
            word = "bottle" #word에 지정된 문자 수정
        print(new_num,word,"of beer on then wall") #new_num으로 지정된 word와 ""사이의 문자 출력
print()#최종출력
