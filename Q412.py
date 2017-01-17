class Solution(object):
    def fizzBuzz(self, n):
        """
        :param n: int
        :return:  list[n]
        """
        arr = range(1,n+1)
        for i in arr:
            if 0 == i % 3 and 0 == i % 5:
                arr[i-1] = "FizzBuzz"
            elif 0 == i % 3 :
                arr[i-1] = "Fizz"
            elif 0 == i % 5:
                arr[i-1] = "Buzz"
            else:
                arr[i-1] = arr[i-1].__str__()
        return arr

if __name__ == '__main__':
    print Solution().fizzBuzz(15)


