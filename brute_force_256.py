import hashlib
import random

class BFA:
    def __init__(self):
        self.iterations = 100_000
      
    def brute_force(self):
        password = 'eaabde6fabac741d3ceab34c2f9453a659ff77ff1f80d81b8ff4ff6f880aee50'
        self.restriction = 13
        self.password_combination = []
        self.alphabet = ["m", "a", "d", "e", " ", "b", "y", " ", "z", "e", "n", "e", "t"]

        for x in range(self.iterations):
            random_letter = random.choice(self.alphabet)
            self.password_combination.append(random_letter)

            if len(self.password_combination) == self.restriction:
                temp_pass = ''.join(self.alphabet)
                random_hashed_password = hashlib.sha256(temp_pass.encode()).hexdigest()

                if random_hashed_password == password:
                    print(f"WE HAVE CRACKED THE IMPOSSIBLE")
                    print(f"THE PASSWORD RANDOMLY GENERATED: {temp_pass} | HASHED PASSWORD FROM THAT: {random_hashed_password}")
                    print("...")
                    break

                else:
                    print(self.password_combination)
                    print(f"WE HAVE FAILED")
                    self.password_combination.clear()
                    continue
            else:
                continue


if __name__ == '__main__':
    run = BFA()
    run.brute_force()

