import matplotlib.pyplot as plt
ax=plt.subplot(111)#新建一个名为ax的分割网格，不适用
ax.text(0.1,0.8,r"$\int_a^b f(x)\mathrm{d}x$",fontsize=30,color="red")
ax.text(0.1,0.3,r"$\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}!$",fontsize=30)
plt.show()