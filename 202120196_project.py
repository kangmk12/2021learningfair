#인사, 이름 입력
name=input("어서오세요. 당신의 이름은 무엇인가요?>>>")
print()
print(name,'님 반갑습니다.')
#마스크 착용 여부 확인
while True:
    wear= int(input("마스크는 착용하셨나요? (네: 1 , 아니오: 2) >>>   "))
    if wear == 1:
        print()
        print("출입명부 작성을 도와드리겠습니다.")
        break
    else:
        print("입장하실 수 없습니다. 마스크를 착용하고 다시 와주세요.")
        print()
        continue
        
#명부작성
print('차례대로 기입해주세요.')
write = []
name = input('이름: ')
write.append(name)

time = input('방문시간: ')
write.append(time)

region = input('거주지역(시.군.구):  ')
write.append(region)

phone = input('전화번호:  ')
write.append(phone)

member = input('인원: ')
write.append(member)

print(write)
print('확인되었습니다.')
print()
print('오늘의 메뉴 선정에 도움을 드릴 수 있는 프로그램입니다.')
print()

#메뉴추천
when=input('언제 메뉴를 추천해드릴까요?(아침.점심.저녁)>>>  ')

#메뉴 종류 선택
menu = int(input('어떤 음식을 먹고 싶으신가요? 1.한식 2.중식 3.일식 4.양식 5.면 >>> '))


if menu == 1:
    from random import randint
    hansik = ['불고기','비빔밥','김치찌개','된장찌개','청국장','설렁탕','국밥','족발','보쌈']
    print()
    print('오늘', when, '추천 메뉴는', hansik[randint(0,8)] ,'입니다.')

elif menu == 2:
    from random import randint
    joongsik = ['짜장면','짬뽕','팔보채','탕수육','잡채밥','간짜장','양장피','유산슬','고추잡채','마라탕','마라샹궈']
    print()
    print('오늘', when, '추천 메뉴는', joongsik[randint(0,10)] ,'입니다.')

elif menu == 3:
    from random import randint
    japan = ['초밥','우동','볶음우동','카레','라멘','오므라이스']
    print()
    print('오늘', when, '추천 메뉴는', japan[randint(0,5)] ,'입니다.')

elif menu == 4:
    from random import randint
    yangsik = ['토마토 스파게티','피자','스테이크','오믈렛','스프','까르보나라','알리오올리오']
    print()
    print('오늘', when, '추천 메뉴는', yangsik[randint(0,6)] ,'입니다.')

else:
    from random import randint
    noodle = ['냉면','칼국수','잔치국수','콩국수','막국수','쌀국수','라면','비빔국수','모밀']
    print()
    print('오늘', when, '추천 메뉴는', noodle[randint(0,8)] ,'입니다.')

#마무리
print()      
print('맛있는 식사하시길 바랍니다.')


