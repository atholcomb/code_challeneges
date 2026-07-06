/*
/* authored by: atholcomb
/* add2.go
/* Adds two numbers and outputs the sum
*/

package main

import ( 
  "fmt"
)

func main() {
  /* Call the add2() function */
  fmt.Println(add2())
}

func add2() string {
  /* Set both variables to their zero value */
  var firstNum, secondNum int

  /* Prompt user to enter two numbers */ 
  fmt.Printf("Enter the 1st number: ")
  fmt.Scanf("%d", &firstNum)
  fmt.Printf("Enter the 2nd number: ")
  fmt.Scanf("%d", &secondNum)

  /* Output the result of the addition for the two numbers passed in */
  return fmt.Sprintf("The total sum equals: %d", firstNum + secondNum)
}
