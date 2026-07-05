/*
// written by: atholcomb
// main.go
// Program outputs the length of a given sequential string
*/

package main

import (
  "fmt"
)

func main() {
  var str string

  fmt.Println("Program outputs the length of a sequential string\n")

  fmt.Printf("Enter a string (without spaces): ")
  fmt.Scanf("%v", &str)

  fmt.Println(showLen(str))
}

func showLen(s string) string {
  return fmt.Sprintf("%v%v%v%v%v\n", "The length of ", s, ",",  " is: ", len(s))
}
