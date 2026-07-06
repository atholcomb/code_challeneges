/*
/* authored by: atholcomb
/* main.go
/* Iterate through the alphabet and output the rune 
/* literal of each letter as it's Unicode representation
*/

package main

import ( 
  "fmt"
)

func main() {
  /* declare and store the alphabet */
  alphabet := "abcdefghijklmnopqrstuvwxyz"

  /* create header row */
  fmt.Println("Rune\tChar")
  fmt.Println("----\t----")
  
  /* iterate over every letter in the alphabet and 
  convert each letter into its Unicode representation */
  for _, letter := range alphabet {
    fmt.Printf("%v\t%c\n", letter, letter)
  }
}
