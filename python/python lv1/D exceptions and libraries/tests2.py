from tests import square
def main():
    test_SQUARE()

def test_SQUARE():
    assert square(2) == 4
    assert square(4) == 16


if __name__ == "__main__":
    main()

