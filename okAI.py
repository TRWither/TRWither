# okAI: the IA that always answers "OK"

def main():
  while True:
    q = input("You: ")
    if q.lower() == "quit":
      break
    else:
      print("okAI: OK")

if __name__ == "__main__":
  main()
