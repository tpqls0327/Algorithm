class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = ['']*n
        for i in range(n):
            if not (i+1) % 3 and not (i+1) % 5:
                arr[i] = "FizzBuzz"
            elif not (i+1) % 3:
                arr[i] = "Fizz"
            elif not (i+1) % 5:
                arr[i] = "Buzz"
            else:
                arr[i] = str(i+1)
        return arr