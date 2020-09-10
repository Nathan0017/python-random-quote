import random
def Nathan():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  r=random.randint(0,13)
  print(quotes[r])

if __name__== "__main__":
  Nathan()
