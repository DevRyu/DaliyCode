package main

import "fmt"

func main() {
	var a int
	var b int
	var p *int

	p = &a
	a = 3
	b = 2
	fmt.Println(a, p, *p)

	p = &b
	fmt.Println(b, p, *p)
}
