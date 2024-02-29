# import matplotlib.pyplot as plt
# import numpy as np
#
#
# def frst_function(x):
#     x_2 = (10.2*x - 149)/3.2
#     return x_2
#
# def sec_function(x):
#     x_2 = (83+5.8*x)/16
#     return x_2
#
# def thrd_function(x):
#     x_2=(234-10.3*x)/7.3
#     return x_2
#
#
#
#
# x_1 = np.linspace(0, 20, 1000)
#
# x_2_1=frst_function(x_1)
# x_2_2=sec_function(x_1)
# x_2_3=thrd_function(x_1)
#
# a = np.array([[10.2, -3.2], [-5.8, 16]])
# b = np.array([149, 83])
# x_f1_f2 = np.linalg.solve(a, b)
#
# a = np.array([[10.3, 7.3], [-5.8, 16]])
# b = np.array([234, 83])
# x_f2_f3 = np.linalg.solve(a, b)
#
# a = np.array([[10.3, 7.3], [10.2, -3.2]])
# b = np.array([234, 149])
# x_f3_f1 = np.linalg.solve(a, b)
#
#
# plt.grid(True)
#
# plt.plot(x_1, x_2_1,linestyle='dashed',label='f[1]')
# plt.plot(x_1, x_2_2,linestyle='dashdot', label='f[2]')
# plt.plot(x_1, x_2_3,linestyle='dotted', label='f[3]')
#
#
# plt.plot(x_f1_f2[0],x_f1_f2[1],marker='o',color='purple')
# plt.plot(x_f2_f3[0],x_f2_f3[1],marker='o',color='navy')
# plt.plot(x_f3_f1[0],x_f3_f1[1],marker='o',color='teal')
# x=[x_f1_f2[0],x_f2_f3[0],x_f3_f1[0]]
# y=[x_f1_f2[1],x_f2_f3[1],x_f3_f1[1]]
#
#
# plt.fill(x + [x[0]], y + [y[0]], color='skyblue')
#
#
#
# plt.xlabel('$x_1$')
# plt.ylabel('$x_2$')
# plt.text(x_1[5], x_2_1[110], '$x_2 = (10.2*x_1 - 149)/3.2$', fontsize=10,rotation=30)
# plt.text(x_1[5], x_2_2[110], '$x_2 = (83+5.8*x_1)/16$', fontsize=10,rotation=5)
# plt.text(x_1[110], x_2_3[410], '$x_2=(234-10.3*x_1)/7.3$', fontsize=10,rotation=-15)
#
# plt.text(10, -30, 'the intersection point \n of f[1] and f[3]', fontsize=10)
# plt.arrow(13, -20,x_f3_f1[0] - 13,x_f3_f1[1]+20)
#
# plt.text(14.2, -20, 'the intersection point \n of f[1] and f[2]', fontsize=10)
# plt.arrow(17, -13,x_f1_f2[0] - 17,x_f1_f2[1]+13)
#
#
# plt.text(10, 25, 'the intersection point \n of f[2] and f[3]', fontsize=10)
# plt.arrow(13, 25,x_f2_f3[0] - 13,x_f2_f3[1]-25)
#
# plt.legend()
# fig=plt.gcf()
# fig.set_size_inches(7,5)
# fig.savefig('final.png', dpi=100)
# plt.show()