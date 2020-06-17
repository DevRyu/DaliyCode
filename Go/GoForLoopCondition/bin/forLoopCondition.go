package main

import "fmt"

func main() {
	// initial, condition, additional
	a := 0
	for i := 0; i < 10; i++ {
		a += i
	}
	// only contain condition
	fmt.Println(a)

	sum := 0
	for sum < 10 {
		sum += sum
	}
	fmt.Println(sum)
}
