
print("="*70)
print()
print('''
                      - 메  뉴  -
             불고기 비빔밥 : 12,000원
             야채 비빔밥 :  8,000원
             전주 비빔밥 :  10,000월

             세트 주문시 : 3000원 추가
             (세트는 밥과 반찬이 추가됩니다.)


             ''')
print("="*70)
      
a=input("비빔밥의 종류를 선택하세요. 예) 불고기, 야채, 전주  >>>>>")
b=input("세트로 주문하시겠습니까? 3,000 추가: 예) 네, 아니요 >>>>>")

price = 0
if a=="불고기":
    price = 12_000 #숫자가크면 _로 숫자구분해줄수 있음. 다만 결과값에 반영안됨.
elif a=="야채":
    price = 8_000
elif a=="전주":
    price = 10_000
else:
    price = "메뉴에 없는 주문입니다"


if b=="네":
    price += 3_000 #price = price+3000


print (f"총 주문금액은 {price}원입니다.")
