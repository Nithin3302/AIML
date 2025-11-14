// Go: goroutine example
package main
import("fmt";"time")

func work(id int){
  time.Sleep(200*time.Millisecond)
  fmt.Println("Worker",id,"done")
}

func main(){
  for i:=1;i<=3;i++{
    go work(i)
  }
  time.Sleep(time.Second)
}
