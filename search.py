def search(x, nums):

	low = 0

	high = len(nums) - 1

	while low <= high:

		mid = (low + high)//2

		item = nums[mid]

		if x == item:

			return mid

		elif x < item:

			high = mid - 1

		else:

			low = mid + 1
	return -1
#first attempt
#def main():

        #x = int(input("Enter the number you are searching for: "))

        #nums = 0
        
        #for i in nums():
                
        #nums = list(int(input("Enter a list of numbers: "))).split(",")

        #for i in range(0, nums - 1):

        #        nums.sort()
                                                                   
        #print() 
#main()
        
#second attempt
def main():

        myList = input("Enter values separated by a comma: ").split(",")

        #looking from the length of the list
        for i in range(0, len(myList)):
                
                #casting- converting each number in list to integer
                myList[i]= int(myList[i])
                
        #sorting the integers
        myList.sort()
        #indentation is important for loop *remember for exam

        #Optional: print the list of value after they are sorted
        print(myList)

        x = int(input("Enter the number you are searching for: "))

        print(search(x, myList))

main()
#can be done with words just have to use string methods
