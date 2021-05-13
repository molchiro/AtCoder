N = int(input())

total = N*(N+1)//2
fizz_n = N//3
fizz_total = 3*fizz_n*(fizz_n+1)//2
buzz_n = N//5
buzz_total = 5*buzz_n*(buzz_n+1)//2
fizzbuzz_n = N//15
fizzbuzz_total = 15*fizzbuzz_n*(fizzbuzz_n+1)//2

print(total - fizz_total - buzz_total + fizzbuzz_total)