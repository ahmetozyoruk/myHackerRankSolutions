func countingSort(arr []int32) []int32 {
    result := [100]int32{}
    for _, v := range arr {
        result[int(v)]++
    }
    return result[:] // convert to slice
}
