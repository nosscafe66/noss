// 特定の条件で数値を表示
package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
 	number, _ := strconv.Atoi(sc.Text())
 	
    if number < 100 {
        fmt.Println(strconv.Itoa(number) + "は100より小さい")
    } else if number >= 100 && number < 200{
        fmt.Println(strconv.Itoa(number) + "は100以上200より小さい")
    } else {
        fmt.Println(strconv.Itoa(number) + "は200以上")
    }
}
