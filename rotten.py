inner = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","0", "1","2","3","4","5","6","7","8","9"]
p = 0
final = []
msg = input("Enter message: ")
shift = int(input())
key = int(input())


for i in msg:
  sinner = inner[shift:]+inner[:shift]
  shift += key
  if shift >= len(inner):
    shift = 1
  final.append(sinner[inner.index(msg[p])])
  p += 1

final = ''.join(final)
print(final)
