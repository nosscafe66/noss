def main(a_1,a_2,a_3,a_4,a_5,a_6,a_7,total_avg):
    total_amount = a_1+a_2+a_3+a_4+a_5+a_6+a_7
    total_avg_ = total_amount/7
    if total_avg_ >= total_avg:
        print("pass")
    elif total_avg_ < total_avg:
        print("failure")

if __name__ == "__main__":
     a_1,a_2,a_3,a_4,a_5,a_6,a_7 = [int(x) for x in input().split(" ")]
     X = int(input())
     main(a_1,a_2,a_3,a_4,a_5,a_6,a_7,X)
