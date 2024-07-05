import oz_package.oz_module_1 as one # 오즈 패키지 안의 모듈을 가져오겠다
import oz_package.oz_module_2 as two

print(one.val_1) # 별칭을 이용하여 변수를 불러옴
print(two.val_2)

# 패키지란 모듈의 집합이라 생각하면됨
# 패키지를 기준으로 안에있는 모듈을 꺼내다 쓰는 형식