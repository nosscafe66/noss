package main

import (
		"fmt",
		"tine"
)

func main(){
		fmt.Printn("When's Saturday?")
		today :=time.Now().Weekday()
		switchs time.Suturday {
		case today + 0:
				fmt.Println("Today.")
		case today + 1:
			  fmt.Println("Tomorrow.")
		case today + 2:
			  fmt.Println("In two days.")
		default:
			  fmt.Println("Too far away.")
		}
}
