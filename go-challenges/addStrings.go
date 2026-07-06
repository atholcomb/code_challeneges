/*
/* authored by: atholcomb
/* addStrings.go
/* returns the sum of two strings 
*/

package main

import (
  "fmt"
  "strconv"
)

func main() {
  /* Call addStrings() function */
  fmt.Println(addStrings("111", "111"))
  fmt.Println(addStrings("10", "80"))
  fmt.Println(addStrings("", "20"))
}

func addStrings(n, m string) string {
  /* Convert n and m to their integer representations */
  n1, _ := strconv.Atoi(n) 
  n2, _ := strconv.Atoi(m)
  
  /* if parameter has an empty string, make it invalid */
  if n == "" || m == "" {
    return "Empty string - Invalid"
  }
  
  /* return the result with the initial values represented */
  return fmt.Sprintf("%v + %v = Result: %v", n, m, strconv.Itoa(n1 + n2))
}
