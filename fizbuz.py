from dataclasses import dataclass


def generate_fizbuz_answers(answers_count: int) -> list[str]:
    results = []
    for number in range(1, answers_count + 1):
        results.append(compile_result(number))
    return results


@dataclass
class FizzBuzzResult:
    fizz: int = 0
    buzz: int = 0

    def __add__(self, other: 'FizzBuzzResult') -> 'FizzBuzzResult':
        fizzes = self.fizz + other.fizz
        buzzes = self.buzz + other.buzz

        return FizzBuzzResult(fizz=fizzes, buzz=buzzes)


def get_fizbuz(number: int) -> FizzBuzzResult:
    result = FizzBuzzResult()

    if number % 3 == 0:
        result.fizz += 1
    if number % 5 == 0:
        result.buzz += 1

    return result


def get_extended_fizbuz(number) -> FizzBuzzResult:
    result = FizzBuzzResult()
    if '3' in str(number):
        result.fizz += 1
    if '5' in str(number):
        result.buzz += 1
    return result


def compile_result(number):
    fizbuz = get_fizbuz(number)
    extended_fizbuz = get_extended_fizbuz(number)
    summary_fizbuz = fizbuz + extended_fizbuz

    result = 'Fizz' * summary_fizbuz.fizz + 'Buzz' * summary_fizbuz.buzz or str(number)

    return result


def main():
    print(*generate_fizbuz_answers(100), sep='\n')


if __name__ == '__main__':
    main()