/*
/* authored by: atholcomb
/* GeneSequencer.go
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
  GeneSequencer(21)
}

func GeneSequencer(count int) {
  /* store genome transcription letters */
  var genome = []string{"a", "t", "g", "c"}

  for i := 1; i < count; i++ {
    /* Generates new sequence */
    fmt.Printf("Sequence:%02d ", i)

    for j := 0; j < 15; j++ {
      /* Generate a random index to be used in selecting genome letter */
      var choice = rand.Intn(4)   
      fmt.Printf("%s", genome[choice])
    }

  /* Prints 'validated sequence' with a 1 second delay, once sequence is created */
  time.Sleep(1 * time.Second)   
  fmt.Printf("%s", " -> Validated")
  fmt.Println()   // new line to return to
  }
}
