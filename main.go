package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func main() {
	a := []string{"a", "b", "c"}
	b := []int{1, 2, 3}

	fmt.Println(zip(a, b))
}

func zip(a []string, b []int) map[int]string {

	mapper := map[int]string{}
	for i, v := range a {

		for index, value := range b {

			if index == i {
				mapper[value] = v
			}
		}
	}
	return mapper
}

func multiply(num1 string, num2 string) (result string) {
	val1, _ := strconv.Atoi(num1)
	val2, _ := strconv.Atoi(num2)

	res := val1 * val2
	fmt.Println(res)
	result = strconv.Itoa(res)
	return
}

func Solution(str string) []string {
	res := str[:]
	val := []string{}
	if len(res)%2 != 0 {
		res += "-"
	}
	for i := 0; i < len(res); i += 2 {
		val = append(val, res[i:i+2])
		fmt.Println(i, i+2)

	}
	return val
}

func checkeven(num int) bool {

	if num%2 == 0 {
		fmt.Println("Valid even number")
		return true
	}

	defer func() {
		if e := recover(); e != nil {
			fmt.Println("this is the error: ", e)
		}
	}()

	panic("input must be an even number!!")
}

func Swapcase(letter string) string {

	return strings.ToUpper(letter)
}

func SquareSum(numbers []int) int {

	arr := numbers[:]
	arr2 := []int{}
	total := 0

	for _, v := range arr {
		arr2 = append(arr2, (v * v))
	}
	for _, v := range arr2 {

		total += v
	}
	return total
}

func Multiple3And5(number int) int {
	val := 0
	for i := 1; i < number; i++ {

		if (i%3 == 0) || (i%5 == 0) {
			val += i
			fmt.Println(i)
		}
	}
	return val
}

func Counter(word string) {

	word_count := map[string]int{
		"a": 0,
		"b": 0, "c": 0, "d": 0, "e": 0, "f": 0,
		"g": 0, "h": 0, "i": 0, "j": 0, "k": 0,
		"l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0,
		"r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0,
		"x": 0, "y": 0, "z": 0,
	}
	time.Sleep(1 * time.Second)
	fmt.Println("Sleeping for 1")
	for _, v := range word {
		for k := range word_count {
			if k == string(v) {
				word_count[k] += 1
			}
		}
	}

	for k := range word_count {
		if word_count[k] == 2 {
			fmt.Println(k, word_count[k])
		} else if word_count[k] >= 3 {
			fmt.Println(k, word_count[k])
		}
	}
	fmt.Println(word, word_count)
}

func search(nums []int, target int) bool {

	for _, v := range nums {
		if target == v {
			return true
		}
	}
	return false
}

func tSum(nums []int, target int) [][]int {

	hashmap := map[int]int{}
	res := [][]int{}
	for i, v := range nums {

		n := target - v
		for k := range hashmap {
			if n != k {
				hashmap[v] = i
			} else {
				res = append(res, []int{hashmap[v], i})
				return res
			}
		}

	}
	return res
}

func twoSum(nums []int, target int) []int {

	res := []int{}

	for i, _ := range nums {
		for j, _ := range nums {
			if i != j && nums[i]+nums[j] == target {
				res = append(res, i, j)

			}
		}
	}
	return res
}

func searchh(nums []int, target int) int {
	for i, v := range nums {
		if target == v {
			return i
		}
	}
	return -1
}

func getsum(a int, b int) int {
	sum := 0
	if a > b {
		for i := b; i <= a; i++ {
			sum += i
		}
		return sum
	} else if b > a {
		for i := a; i <= b; i++ {
			sum += i
		}
		return sum
	}
	return a
}

func longest(a string, b string) string {
	alp := a + b
	alp_set := ""

	for _, v := range alp {
		for _, val := range alp_set {
			if string(v) != string(val) {
				alp_set += string(v)
			}
		}
		continue
	}
	return alp_set
}
func removeElement(nums []int, val int) int {
	count := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != val {
			nums[count] = nums[i]
			count++
		}
	}
	fmt.Println(nums)
	return len(nums)
}

func RemoveIndex(s []int, index int) []int {
	return append(s[:index], s[index+1:]...)
}
