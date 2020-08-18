package extract_function

import "fmt"

type OutStanding struct {
	customer string
	amount   int64
}

func PrintOwing() {
	customer := OutStanding{
		customer: "john",
		amount:   100,
	}
	fmt.Print(customer.amount)
	fmt.Print(customer.customer)
}

func NewPrintOwing() {
	customer := OutStanding{
		customer: "john",
		amount:   100,
	}
	printDetail(customer)
}

func printDetail(customer OutStanding) {
	fmt.Print(customer.amount)
	fmt.Print(customer.customer)
}

func main() {
	PrintOwing()
	NewPrintOwing()
}
