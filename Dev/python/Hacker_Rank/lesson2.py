import sys

def merge_the_tools(string, k):
    # your code goes here
    try:
        s = int(len(string)/k)
        #print(string[0:s] + "\n" + string[s:2*s] + "\n" + string[2*s:3*s])
        t0 = string[0:s]
        t1 = string[s:2*s]
        t2 = string[2*s:3*s]
        
        count = 0
        for i in t0:
            count += 1
            if t0.count(i) >=2 and count >= 2:
                t0 = "'" + t0 + "'"
                print(t0)
                print("Check count {} more than 2 is {}".format(count,i))
                break

        count = 0
        for j in t1:
            count += 1
            if t1.count(j) >=2 and count >= 2:
                t1 = "'" + t1 + "'"
                print(t1)
                print("Check count {} more than 2 is {}".format(count,j))
                break
                
        count = 0
        for k in t2:
            count += 1
            if t2.count(k) >=2 and count >= 2:
                t2 = "'" + t2 + "'"
                print(t2)
                print("Check count {} more than 2 is {}".format(count,k))
                break
    except Exception as e:
        print(e)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
