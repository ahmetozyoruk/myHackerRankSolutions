package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

/*
 * Complete the 'diagonalDifference' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

func diagonalDifference(arr [][]int32) int32 {
    // Write your code here
    
    var leftArray []int32
    var rightArray []int32

    var sumLeft int32
    var sumRight int32
    
    var result int32
    
    if len(arr) == 1 && len(arr[0]) == 1 {
        return 0
    }
    
    if len(arr) != len(arr[0]) {
        fmt.Print("please enter equal dimention array each other")
    }
    
    for i:=0; i<len(arr); i++ {
        var temp int
        var righttItem int32
        var leftItem int32
        
        temp = len(arr[0])-(i+1)
        righttItem = arr[i][temp]
        leftItem = arr[i][i]
        
        leftArray = append(leftArray, leftItem)
        rightArray = append(rightArray, righttItem)
    }
    
    for i:=0; i<len(leftArray); i++ {
        sumLeft = sumLeft + leftArray[i]
    }
    
    for i:=0; i<len(rightArray); i++ {
        sumRight = sumRight + rightArray[i] 
    }
    
    if sumLeft > sumRight {
        result = sumLeft - sumRight
    } else {
        result = sumRight - sumLeft 
    }
    
    return result
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    n := int32(nTemp)

    var arr [][]int32
    for i := 0; i < int(n); i++ {
        arrRowTemp := strings.Split(strings.TrimRight(readLine(reader)," \t\r\n"), " ")

        var arrRow []int32
        for _, arrRowItem := range arrRowTemp {
            arrItemTemp, err := strconv.ParseInt(arrRowItem, 10, 64)
            checkError(err)
            arrItem := int32(arrItemTemp)
            arrRow = append(arrRow, arrItem)
        }

        if len(arrRow) != int(n) {
            panic("Bad input")
        }

        arr = append(arr, arrRow)
    }

    result := diagonalDifference(arr)

    fmt.Fprintf(writer, "%d\n", result)

    writer.Flush()
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}
