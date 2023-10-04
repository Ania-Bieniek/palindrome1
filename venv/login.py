



import sys

def print_maturity(age):
    if age >= 18:
        print("Adult")
    else:
        print('kidd')

if __name__ == "__main__":
    age = int(sys.argv[1])
    print_maturity(age)






