# Steps 
1. Clone code
2. `python3 main.py`
3. Follow steps prompted in the CLI

# Useful test cases
- Not enough change
    - Select `water`
    - Insert 10, expect fail because insufficient change to return
    - Insert 9, expect success with [5,1,1,1]
 
- Not enough of the largest note and use smaller notes
  - Select `coke`
  - Insert 120. Expect [100,5,1,1,1] but because not enough 100 notes expect change as [50,50,5,1,1,1]
 
- Juice doesen't display in catalog even though the vending machine usually sells it
    - Because the stock for `juice` is 0

- Enter 'X' to exit program during drink prompt and amount paid prompt. Expect to exit program.
