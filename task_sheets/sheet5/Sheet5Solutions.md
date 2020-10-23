# Solutions for Task Sheet 5 

### Task 1 - 2
See the [software manual](../../SoftWare_Manual/Table_of_Contents.md) as well as the files [NewtonsMethod.py](NewtonsMethod.py) and [SecantMethod.py](SecantMethod.py)

### Task 3 - 4
Lets start with the Newtons Method Convergence:
![NewtonsMethodConvergence.png]
This is a loglog plot of the error and the tolerance becomes smaller and smaller. Notice that a tolerance of 10^-3 leads to an error of about 10^-7. That is a good show of the quadratic convergence.

Now lets look at the Secant Method.
![SecantMethodConvergence.png]
Notive how on this loglog plot of the error when the tolerance is about 10^-3 then the error is about 10^-6. This is a good sign of the near quadratic convergnce. In both plots you see that the error goes to zero. That is because the approximation for the root of the function used as the "true" value means that at somepoint both approximations equal each other.


### Task 5
See the software manual as well as the file [HybridMethod.py](HybridMethod.py)

### Task 6
Newtons method seems to be the gold standard, but it seems you need the perfect equation to make it work. Though most functions have second derivatives it may not be possible to analytically find one, which is a big con of newtons method. The next best is the secant method, but the biggest con it faces is that you need to know good starting values or it will diverge. Finally the bisection method is the tried and true function that works most of the time as long as your know that your function is continuous.

Sources
[https://www.lehigh.edu/~ineng2/clipper/notes/newtons.htm](
https://www.lehigh.edu/~ineng2/clipper/notes/newtons.htm)
[https://www.lehigh.edu/~ineng2/clipper/notes/secant.htm](
https://www.lehigh.edu/~ineng2/clipper/notes/secant.htm)
[https://mmiranda96blog.wordpress.com/2017/03/08/root-finding-method-comparison/](
https://mmiranda96blog.wordpress.com/2017/03/08/root-finding-method-comparison/)
