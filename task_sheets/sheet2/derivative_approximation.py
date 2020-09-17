from math import cos
import matplotlib.pyplot as plt

def cosApprox(x, h):
    return (cos(x + h) - 2 * cos(x) + cos(x - h)) / (h ** 2)


h = [1, .5]
count = 1
while count <= 16:
    h.append(1 / 10 ** count)
    count += 1
print("h--Error Magnitude")
difference = [];
for a in h:
	approx = cosApprox(2, a)
	true = -cos(2)
	diff = abs(true - approx)
	difference.append(diff)
	print(f"h={a}, Error={diff}")

plt.title("Centered Difference Approximation Error of cos Second Derivative")
plt.xlabel("h values (logarithmic)")
plt.ylabel("Absolute Error (logarithmic)")
plt.loglog(h,difference)
plt.show()
