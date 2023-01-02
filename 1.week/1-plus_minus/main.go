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
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */
 
type Condition struct {
    isBigger, isNegative, isEquals int
}
var _condition = Condition{1,2,3}

func calculateRatioOfItems(arr []int32, conditionType int) float32 {
    var sumNumOfItems int = 0
    for item := 0; item<len(arr); item++{
       if getConditionResult(arr[item], conditionType) {
           sumNumOfItems++;
       }
    }
    
    return float32(sumNumOfItems)/float32(len(arr))
}

func getConditionResult(item int32, conditionType int) bool {
    if conditionType == _condition.isBigger {return item>0}
    if conditionType == _condition.isEquals {return item==0}
    if conditionType == _condition.isNegative {return item<0}
    return false    
}
 
func printTheCalculationRatioOfArr(arr []int32) {
    // pos, neg , zeros num sum [seperate]
    // print sum/arr.lenght
    // values zero
    var ratios[3] float32
    
    ratios[0] = calculateRatioOfItems(arr,_condition.isBigger)
    ratios[1] = calculateRatioOfItems(arr,_condition.isNegative)
    ratios[2] = calculateRatioOfItems(arr,_condition.isEquals)    
    
    for _, itemRatio := range ratios {
        fmt.Println(itemRatio)
    }
}

func plusMinus(arr []int32) {
    printTheCalculationRatioOfArr(arr)
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    n := int32(nTemp)

    arrTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    var arr []int32

    for i := 0; i < int(n); i++ {
        arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
        checkError(err)
        arrItem := int32(arrItemTemp)
        arr = append(arr, arrItem)
    }

    plusMinus(arr)
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
