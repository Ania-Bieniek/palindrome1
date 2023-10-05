
import sys

def print_maturity(age):
    if age >= 18:
        print(" You Adult")
    else:
        print('You kidd')

if __name__ == "__main__":
    age = int(sys.argv[1])
    print_maturity(age)
# na podst. wywołania bedziemy mogli stwierdzić czy ktoś jest dorosły-  python venv/login.py 16 >>  You kidd lub .../login.py 20 wtedy >> You Adult








