def sum_of_odds_up_to_n(n):
  if n <= 0:
    return 0
  if n % 2 == 0:
    return sum_of_odds_up_to_n(n-1)
  return n + sum_of_odds_up_to_n(n-2)

def main():
	n = float(raw_input("The next number:"))
	sum_of_odds_up_to_n(n)
main()
	
