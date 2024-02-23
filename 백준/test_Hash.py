from enum import Enum
from HashAlgorithm import ChainedHash

Menu = Enum('Menu', ['add', 'search', 'printed', 'exit'])
# 메뉴를 만들어줍니다.

def select_menu() -> Menu:  # 메뉴를 선택합니다.
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = ChainedHash(13)	# 크기가 13인 배열을 만들어줍니다.

while True:
    menu = select_menu()

    if menu == Menu.add:
        value = int(input('추가할 값을 입력하세요.: '))
        if not hash.add(value):
            print('추가 실패')
        else:
            print('추가 성공')

    elif menu == Menu.search:
        value = int(input('검색할 값을 입력하세요.: '))
        t = hash.search(value)
        if t is not None:
            print(f'검색한 값을 갖는 인덱스는 {t}입니다.')
        else:
            print('검색한 값이 없습니다.')

    elif menu == Menu.printed:
        hash.printed()

    else:
        break