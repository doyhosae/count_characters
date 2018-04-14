#문자 길이 검사(characters count)
import codecs #utf-8을 하기 위하여

f = open("text.txt", "r", encoding="utf-8")
c = f.read()
f.close()

#설명서
print('''
    ※개행과 공백은 기본적으로 카운트 하지 않음(별도 표시)
     text.txt 파일 수정시 프로그램 재실행 필요
    1.글자 수 확인
    2.카운트에서 제외하고 싶은 문자 추가
    3.종료
''')

def check():            #글자수 판독
    new_line = 0
    spacing = 0
    check_list_number = 0

    for a in c:
        if a == "\n":
            new_line += 1
        elif a == " ":
            spacing += 1
        for b in check_list.values():
            if a == b:
                check_list_number += 1

    len_c = len(c) - new_line - spacing - check_list_number
    print(
    '''
        개행 수: {a}
        공백 수: {b}          -         문자 수: {d}
        제외한 문자 수: {c}
        ================================================
        = 총 글자 수: {sum}
    '''.format(a=new_line, b=spacing, c=check_list_number,d=len(c) ,sum=len_c))

    # return(len_c)

i = 0     #기능 선택 번호
j = 0     #제외하고 싶은 문자 딕셔너리에 차례대로 들어갈 키 ex)0,1,2,3...
check_list = {}
while True:
    i = input("number: ")
    if i == "1":
        check()
    elif i == "2":
        j += 1
        print(
        '''
        ※한 글자씩 넣어야 됨
         한글, 특수문자 가능
        ''')
        check_list[j] = input("제거하고 싶은 문자: " )
    elif i == "3":
        break
    else:
        print("Please, 1,2,3 중 하나를 입력")
