/*
/* authored by: atholcomb
/* GeneSequencer.go
/* Prints out genomic strands which are validated upon creation
*/

package main

import ( 
  "fmt"
  "math/rand"
  "time"
)

func main() {
  /* Postpone sequence start by 2 seconds */
  time.Sleep(2 * time.Second)     
  fmt.Println("----------- Genome Sequencer ----------- ")

  /* Number of sequences to be printed */
  GeneSequencer(21)
}

func GeneSequencer(count int) {
  /* store genome transcription letters */
  var genome = []string{"a", "t", "g", "c"}

  /* Generates a new sequence */
  for seqnum := 1; seqnum < count; seqnum++ {

  /* Generate a random index to be used in selecting genome letter */
  var choice string
  for i := 0; i < 15; i++ {
    var random = rand.Intn(4)   
    choice += genome[random]
  }
  /* Prints 'validated' with a 1 second delay, once sequence is created */
  time.Sleep(1 * time.Second)   
  fmt.Printf("Sequence%02d: %v %s\n", seqnum, choice, "-> Validated")
  }
}
