def main():
    #return [("test_{}".format(i),"test_{}".format(j)) for i in range(20) for j in range(20)]
    return ["Column_{}".format(i) if i % 2 == 0 else "NaN" for i in range(20)]
if __name__ == "__main__":
    result = main()
    print(result)
    with open("test.csv",mode="w") as f:
        f.write(str(result))
