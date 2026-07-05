/*
/* Written By: atholcomb
/* main.go
/* Program outputs a mock system check analysis
*/

package main

import ( 
  "fmt"
  "time"
)

func main() {
  env := sysCheck()

  fmt.Printf("%s%s\n", "Connected to system: ", "glk-ath-2427-OMA")
  fmt.Println("/reading attributes...")

  for k, v := range env {
    time.Sleep(1 * time.Second)
    fmt.Printf("%v: %v\n", k, v)
  }
}

func sysCheck() map[string]string {
  env := map[string]string {
    "os": "linux",
    "cpu_cores": "24",
    "gpu_type": "cuda xtreme",
    "ram_size": "2Tb",
    "kernel": "3.2.1",
    "vm": "yes",
  }
  return env
}
