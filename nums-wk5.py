def oddOrEven(num):
    if num % 2 != 0:
        print("Odd")
    else:
        print("Even num.")

def getAvg(nums: list):
    avg = sum(nums) / len(nums)
    print(avg)

def sortNums(nums: list):
    print(f"Smallest: {min(nums)}, Largest: {max(nums)}")