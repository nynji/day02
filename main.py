
PI = 3.14
print(f'원주율의 값은 {PI}이고 타입은 {type(PI)}입니다.')

#chap 3

#진법

#number = 0b10011010
#number = 0x9A
#number = 0o232
#print(number)

number = 154
print(bin(number))
print(hex(number))
print(oct(number))

print(ord("a")) #아스키
print(hex(ord(" ")))

PI = 3.14
print(f'원주율의 값은 {PI}이고 타입은 {type(PI)}입니다.')


#chap 4 if

limits = 20
tweets = "pass" * 6
diff = limits - len(tweets)
if diff >= 0:
    print(tweets)
else:
    print(f'제한 글자 수 {abs(diff)}초과')

