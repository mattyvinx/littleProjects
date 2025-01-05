for x in range(1,11):
   print(f"  {x:4}",end = "") ## headerRow
print()
print("    -------------------------------------------------------")
for r in range (1,11):
   print(f"{r:2} |", end = "")
   for c in range(1,11):
      print(f"{r*c:4}", end = "")
   print()
