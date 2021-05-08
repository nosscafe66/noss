package main

import (
	"fmt"
)

func Sqrt(x float64) float64 {
	for z := 1.0; z < 10; z++ {
		fmt.Println(z)
		z -= (z*z - x) / (2*z)
		if z > 10{
				fmt.Println("10回より多い")
			}else if z < 10{
				fmt.Println("10回より少ない")}
		if z == (z*z - x) / (2*z) || z <= (z*z - x) / (2*z){
			break}
		return z
    }
	return x
}

func main() {
	fmt.Println(Sqrt(2))
}
