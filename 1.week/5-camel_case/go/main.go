package main
import (
    "bufio"
    "strings"
    "fmt"
    "os"
    "regexp"
)

func main() {
    //Enter your code here. Read input from STDIN. Print output to STDOUT
    var lines []string
    scn := bufio.NewScanner(os.Stdin)
    for scn.Scan() {
        line := scn.Text()
        if len(line) == 1 {
            if line[0] == '\x1D' {
                break
            }
        }
        lines = append(lines, line)
    }

    for _, text := range lines {        
        ops := text[0:1]
        valueType := text[2:3]
        value := text[4:]
        if ops == "S" {
            handle_split(value, valueType)
        } else {
            handle_combine(value, valueType)
        }
        fmt.Println("")
    }  
}

func handle_split(value, valueType string) {
    reSp := regexp.MustCompile("[A-Z]")
    reRe := regexp.MustCompile("[()]")
    newValue := reRe.ReplaceAllString(value, "",)
    
    value = ""
    for i, c := range newValue {
        if reSp.MatchString(string(c)) && value != "" {
            fmt.Printf("%s ", strings.ToLower(value))
            value = string(c)
            continue
        }
        value += string(c)
        if i == len(newValue)-1{
            fmt.Printf("%s ", strings.ToLower(value))    
        }
    }
}

func handle_combine(value, valueType string) {
    reSp := regexp.MustCompile("\\s")
    words := reSp.Copy().Split(value, -1)
    result := ""
    for _, word := range words {
        if valueType != "C" && result == "" {
            result += strings.ToLower(word)
            continue
        } else {
            result += strings.ToUpper(word[0:1]) + word[1:]
        }
    }
    
    if valueType == "M" {
        result += "()"
    }
    fmt.Print(result)
}

