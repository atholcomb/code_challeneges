/*
// authored by: atholcomb
// add2.go
// Adds two numbers and outputs the sum
*/

package main

import ( 
  "fmt"
)

func main() {
  fmt.Println(add2())
}

func add2() string {
  var firstNum, secondNum int

  fmt.Printf("Enter the 1st number: ")
  fmt.Scanf("%d", &firstNum)
  fmt.Printf("Enter the 2nd number: ")
  fmt.Scanf("%d", &secondNum)

  return fmt.Sprintf("The total sum equals: %d", firstNum + secondNum)
}
