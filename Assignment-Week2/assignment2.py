# 要求1: 完成以下函式，在函式中使用迴圈計算最小值到最大值之間，所有整數的總和。
def calculate(min, max):
    sum = 0
    for i in range(min, max + 1):
        sum += i
    print(sum)


calculate(1, 3)
calculate(4, 8)

# 要求2: 正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
import json


def avg(data):
    count = data["count"]
    sum = 0
    for employee in data["employees"]:
        sum += employee["salary"]
    average = sum / count
    print(average)


avg({
    "count":
    3,
    "employees": [{
        "name": "John",
        "salary": 30000
    }, {
        "name": "Bob",
        "salary": 60000
    }, {
        "name": "Jenny",
        "salary": 50000
    }]
})  # 呼叫 avg 函式


#要求三：演算法-找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
def maxProduct(nums):
    max = 0
    if len(nums) == 2:
        max = nums[0] * nums[1]
    else:
        for x in range(0, len(nums)):
            for y in range(x + 1, len(nums)):
                sum = nums[x] * nums[y]
                if sum > max:
                    max = sum
    print(max)


maxProduct([5, 20, 2, 6])  # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3])  # 得到 30 因為 10 和 3 相乘得到最大值


# 要求四：( 請閱讀英文 )：演算法
def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


'''
# 優化: 使用hash table
def twoSum(nums, target):
    hash_table = {}  # {key1 (= num): value1 (= index)}
    for i, num in enumerate(nums):
        if target - num in hash_table:
            return ([hash_table[target - num], i])
        else:
            hash_table[num] = i
    return []
'''

result = twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9


# 要求五 ( Optional )：演算法：給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大長度。
def maxZeros(nums):
    maxLen = 0
    currentLen = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            currentLen += 1
            if currentLen > maxLen:
                maxLen = currentLen
        else:
            currentLen = 0
    print(maxLen)


maxZeros([0, 1, 0, 0])  # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])  # 得到 4
maxZeros([1, 1, 1, 1, 1])  # 得到 0
