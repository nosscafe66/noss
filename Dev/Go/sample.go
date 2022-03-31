package main

import (
	"fmt"
)

var number1 = 100//パッケージ変数
var number2 = 200//パッケージ変数

func main() {
	var number3 = 300//ローカル変数
	fmt.Println("Hello Go")
	total1 := number1 + number2
	fmt.Println(total1)
	total2 := number1 + number3
	fmt.Println(total2)

	if total2 == 400 {
		fmt.Println("Success")
		sub()
	} else {
		fmt.Println("Failed")
	}
}

func sub() {
	var number4 = 400//ローカル変数
	fmt.Println(number2 + number4)
	fmt.Println(number2)
}