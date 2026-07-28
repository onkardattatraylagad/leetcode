class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i=1
        l=[]
        while i<=n:
            if i%3==0 and i%5==0:
                l.append("FizzBuzz")
            elif i%3==0:
                l.append("Fizz")
            elif i%5==0:
                l.append("Buzz")
            else:
                l.append(f"{i}")
            i=i+1
        return l


        