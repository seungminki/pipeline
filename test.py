# 파이프라인과 상관없는 테스트용 파일

print('hello')

def test_car():
    a = 1
    b = 1
    print(a+b)
    print('hello')

def test_car2():
    a = 2
    b = 3
    return print(a+b)

# if __name__ == '__main__':
#     test_car()
#     test_car2()
