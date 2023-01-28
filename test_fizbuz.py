from fizbuz import generate_fizbuz_answers, get_fizbuz, get_extended_fizbuz, FizzBuzzResult, compile_result


def test_fizbuz_solution():
    result = generate_fizbuz_answers(100)

    assert len(result) == 100


def test_get_fizbuz():
    assert get_fizbuz(3) == FizzBuzzResult(fizz=1, buzz=0)
    assert get_fizbuz(5) == FizzBuzzResult(fizz=0, buzz=1)
    assert get_fizbuz(1) == FizzBuzzResult(fizz=0, buzz=0)
    assert get_fizbuz(10) == FizzBuzzResult(fizz=0, buzz=1)
    assert get_fizbuz(15) == FizzBuzzResult(fizz=1, buzz=1)
    assert get_fizbuz(9) == FizzBuzzResult(fizz=1, buzz=0)
    assert get_fizbuz(49) == FizzBuzzResult(fizz=0, buzz=0)


def test_get_extended_fizbuz():
    assert get_extended_fizbuz(53) == FizzBuzzResult(fizz=1, buzz=1)
    assert get_extended_fizbuz(49) == FizzBuzzResult(fizz=0, buzz=0)
    assert get_extended_fizbuz(3) == FizzBuzzResult(fizz=1, buzz=0)
    assert get_extended_fizbuz(55) == FizzBuzzResult(fizz=0, buzz=1)


def test_compile_result():
    assert compile_result(49) == '49'
    assert compile_result(9) == 'Fizz'
    assert compile_result(3) == 'FizzFizz'
    assert compile_result(32) == 'Fizz'
    assert compile_result(52) == 'Buzz'
    assert compile_result(35) == 'FizzBuzzBuzz'
