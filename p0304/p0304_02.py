# 숫자 5개를 입력받아 5개 출력하시오.
nums = []
for i in range(0,5):
    nums.append(int(input('숫자를 입력하세요. > '))) # str 

print(nums)

# 5개의 합을 구하기
sum = 0
for num in nums:
    sum += num

print('합계 : ',sum)


