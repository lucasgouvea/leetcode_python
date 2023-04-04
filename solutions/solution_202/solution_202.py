class Solution202:
    max_iterations = 100

    def is_happy(self, n: int) -> bool:
        total:int = 0
        num:str = str(n)
        iterations = 0

        while iterations < self.max_iterations:
            iterations += 1
            for char in num:
                total += int(char) ** 2
            num = str(total)
            if total == 1:
                break
            else:
                total = 0
        
        if iterations == self.max_iterations:
            return False

        return True