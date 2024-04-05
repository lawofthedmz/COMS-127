x = 3
def foo():
    global x
    for i in range(0, x):
        x += x
    return x
def main():
    x = foo()
    print(x + x)
if __name__ == "__main__":
    main()