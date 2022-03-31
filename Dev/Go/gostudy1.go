package main

import (
	"fmt"
	"time"
)

var number1 = 100 //パッケージ変数
var number2 = 200 //パッケージ変数

//構造体1
type Number struct {
	number5 int
	number6 int
	number7 int
}

//構造体2
type Number struct {
	number5,number6,number7 int
}

var n Number
n.number5
n.number6
n.number7

n2 := Number{1000,2000,3000}
n3 := Number{number5:1000,number6:2000,number7:3000}

//コンストラクタ関数




//メイン関数
func main() {
	var number3 = 300 //ローカル変数
	fmt.Println("Hello Go" + time.now())
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

//サブ関数
func sub() {
	var number4 = 400 //ローカル変数
	fmt.Println(number2 + number4)
	fmt.Println(number2)
}
