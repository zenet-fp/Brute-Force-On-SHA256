import hashlib
import random

# made by Zenet
# NOTE: this is purely for educational purposes only!

class BFA:
    def __init__(self, apply_algorithm: bool):
        self.iterations = 100_000

        if apply_algorithm is True:
            run_restriction = DataRestriction()
            self.restriction = run_restriction.restriction_algorithm()

        else:
            self.restriction = 10
            # otherwise set the restriction to 10

        print(f"The restriction length of the word was: {self.restriction}")
        print("...")
        print()

    def brute_force(self):
        password = 'eaabde6fabac741d3ceab34c2f9453a659ff77ff1f80d81b8ff4ff6f880aee50'

        self.password_combination = []

        self.alphabet = [
                        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        for x in range(self.iterations):
            random_letter = random.choice(self.alphabet)
            self.password_combination.append(random_letter)

            if len(self.password_combination) == self.restriction:
                temp_pass = ''.join(self.alphabet)
                random_hashed_password = hashlib.sha256(temp_pass.encode()).hexdigest()

                if random_hashed_password == password:
                    print(f"WE HAVE CRACKED THE IMPOSSIBLE")
                    print(
                        f"THE PASSWORD RANDOMLY GENERATED: {temp_pass} | HASHED PASSWORD FROM THAT: {random_hashed_password}")
                    print("...")
                    break

                else:
                    print(self.password_combination)
                    print(f"WE HAVE FAILED")
                    self.password_combination.clear()
                    continue
            else:
                continue


class DataRestriction:

    def restriction_algorithm(self) -> int:
        MAX_LENGTH = 50
        MIN_LENGTH = 1

        random_restriction_length = random.randint(MIN_LENGTH, MAX_LENGTH)

        # return a random restriction length for the word

        return random_restriction_length


if __name__ == '__main__':
    run = BFA(True)
    # enter False if you want a pre-determined restriction length
    run.brute_force()
