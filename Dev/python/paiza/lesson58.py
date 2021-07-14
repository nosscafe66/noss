def main():
    a_1,a_2,a_3,a_4,a_5 = [int(x) for x in input().split(" ")]
    total = a_1+a_2+a_3+a_4+a_5
    return total
if __name__ == "__main__":
    result = main()
    print(str(result)[-1])
