def main(m,n):
    for i in range(10):
        an = m * i + n
        print(str("\n"+str(an)+"\n").strip(),end=" ")
        
    
if __name__ =="__main__":
    m,n= [int(x) for x in input().split(" ")]
    main(m,n)
