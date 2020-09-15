from math import cos

def cosApprox(x, h):
    return (cos(x + h) - 2 * cos(x) + cos(x - h)) / (h ** 2)


h = [1, .5]
count = 1
while count <= 16:
    h.append(1 / 10 ** count)
    count += 1
print("True Value-----------h---------Approximation---------Error Magnitude")
for a in h:
	approx = cosApprox(2, a)
	true = -cos(2)
	diff = abs(true - approx)
	print(f"True={true} h={a} approx={approx}, Error={diff}")
