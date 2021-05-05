package main

import (
	"fmt"
	"math/cmplx"
)

var (
	ToBe   bool       = false
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)

func main() {
	fmt.Println("Type: %T Value: %v\n", ToBe, ToBe)
	fmt.Println("Type: %T Value: %v\n", MaxInt, MaxInt)
	fmt.Println("Type: %T Value: %v\n", z, z)
}
