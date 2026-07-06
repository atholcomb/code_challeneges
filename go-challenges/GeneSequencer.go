/*
/* Written By: atholcomb
/* genomesequencer.go
/* Outputs pseudo like DNA sequence strands 
*/

package main

import ( 
  "fmt"
  "math/rand"
  "time"
)

func main() {
  fmt.Println("Genome Sequencer | Sequence starts in 2 seconds")
  fmt.Println("-----------------------------------------------")

  /* Postpone sequence start by 2 seconds */
  time.Sleep(2 * time.Second)     

  /* Number of sequences to be printed, up to 21 */
  genomeSequencer(5)
}

func genomeSequencer(count int) {
  /* store DNA inscription letters in to genome variable */
  var genome = []string{"a", "t", "g", "c"}

  for i := 1; i < count; i++ {
    /* Sleeps 1 second before generating new sequence */
    time.Sleep(1 * time.Second)   
    fmt.Printf("Sequence:%02d ", i)

    for j := 0; j < 15; j++ {
      /* Generate a random index to be used in selecting genome letter */
      var choice = rand.Intn(4)   
      fmt.Printf("%s", genome[choice])
    }

  /* Prints 'validated sequence' once sequence is created */
  fmt.Printf("%s", " -> Validated")
  fmt.Println()   // new line to return to
  }
}
