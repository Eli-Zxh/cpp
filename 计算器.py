import tkinter as tk
import subprocess
import shlex
import re
import matplotlib.pyplot as plt
"""
尚未解决的问题：
1.科学计数法的括号问题
2.根号运算的表示问题
3.三角函数以及角度制弧度制问题
4.选择显示模式问题
5.计算器处理速度
6.latex显示问题
"""
root = tk.Tk()
root.title('Casio')
root.geometry('460x460+100+100')
#root.attributes("-topmost", True)
#root.attributes("-alpha", 0.9)
root["background"]='#2d2c32'
font = ('宋体', 30)
font_16 = ('宋体', 16)
font_12 = ('宋体', 12)

output_num = tk.StringVar()
output_num.set('')

tk.Label(root,
         textvariable=output_num, font=font, height=2,
         width=23, justify=tk.LEFT , anchor=tk.SE
         ).grid(row=1,column=1,columnspan=30)
"""按钮设置"""
button_OPTN = tk.Button(root, text='OPTN',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_OPTN.grid(row=2,column=1,columnspan=5,padx=4,pady=2)
button_CALC = tk.Button(root, text='CALC',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_CALC.grid(row=2,column=6,columnspan=5,padx=4,pady=2)
button_Integral = tk.Button(root,text='∫',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_Integral.grid(row=2,column=21,columnspan=5,padx=4,pady=2)
button_X = tk.Button(root,text='x',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_X.grid(row=2,column=26,columnspan=5,padx=4,pady=2)
button_Fraction = tk.Button(root, text='—',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_Fraction.grid(row=3,column=1,columnspan=5,padx=4,pady=2)
button_Squared = tk.Button(root,text='√',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_Squared.grid(row=3,column=6,columnspan=5,padx=4,pady=2)
button_Square =tk.Button(root,text='x²',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_Square.grid(row=3,column=11,columnspan=5,padx=4,pady=2)
button_Power = tk.Button(root,text='xº',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_Power.grid(row=3,column=16,columnspan=5,padx=4,pady=2)
button_log = tk.Button(root,text='logₒ▫',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_log.grid(row=3,column=21,columnspan=5,padx=4,pady=2)
button_ln = tk.Button(root,text='ln',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_ln.grid(row=3,column=26,columnspan=5,padx=4,pady=2)
button_negative =tk.Button(root,text='(-)',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_negative.grid(row=4,column=1,columnspan=5,padx=4,pady=2)
button_degree = tk.Button(root,text='°′″',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_degree.grid(row=4,column=6,columnspan=5,padx=2,pady=1)
button_reciprocal = tk.Button(root,text='x⁻¹',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_reciprocal.grid(row=4,column=11,columnspan=5,padx=4,pady=2)
button_sin = tk.Button(root,text='sin',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_sin.grid(row=4,column=16,columnspan=5,padx=4,pady=2)
button_cos = tk.Button(root,text='cos',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_cos.grid(row=4,column=21,columnspan=5,padx=4,pady=2)
button_tan = tk.Button(root,text='tan',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_tan.grid(row=4,column=26,columnspan=5,padx=4,pady=2)
button_STO = tk.Button(root,text='STO',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_STO.grid(row=5,column=1,columnspan=5,padx=4,pady=2)
button_ENG = tk.Button(root,text='ENG',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_ENG.grid(row=5,column=6,columnspan=5,padx=4,pady=2)
button_Lbracket = tk.Button(root,text='(',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_Lbracket.grid(row=5,column=11,columnspan=5,padx=4,pady=2)
button_Rbracket =tk.Button(root,text=')',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_Rbracket.grid(row=5,column=16,columnspan=5,padx=4,pady=2)
button_tranfer = tk.Button(root,text='S⇔D',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_tranfer.grid(row=5,column=21,columnspan=5,padx=4,pady=2)
button_M =tk.Button(root,text='M+',width=4,font=font_16,relief=tk.FLAT, bg='#36353c',fg='#c9c9cb')
button_M.grid(row=5,column=26,columnspan=5,padx=4,pady=2)
button_7 = tk.Button(root, text='7', width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_7.grid(row=6, column=1,columnspan=6, padx=4,pady=2)
button_8 = tk.Button(root, text='8', width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_8.grid(row=6, column=7,columnspan=6, padx=4,pady=2)
button_9 = tk.Button(root, text='9', width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_9.grid(row=6, column=13,columnspan=6,padx=4,pady=2)
button_DEL = tk.Button(root, text='DEL', width=5, font=font_16, relief=tk.FLAT, bg='#0c39b1',fg='#e3f3e4')
button_DEL.grid(row=6, column=19,columnspan=6, padx=4,pady=2)
button_AC = tk.Button(root, text='AC', width=5, font=font_16, relief=tk.FLAT, bg='#0c39b1',fg='#e3f3e4')
button_AC.grid(row=6, column=25,columnspan=6, padx=4,pady=2)
button_4 = tk.Button(root, text='4',  width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_4.grid(row=7, column=1,columnspan=6,padx=4,pady=2)
button_5 = tk.Button(root, text='5',  width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_5.grid(row=7, column=7,columnspan=6, padx=4,pady=2)
button_6 =tk.Button(root, text='6', width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_6.grid(row=7, column=13,columnspan=6, padx=4,pady=2)
button_multiply =tk.Button(root, text='×', width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_multiply.grid(row=7,column=19,columnspan=6,padx=4,pady=2)
button_divide =tk.Button(root, text='÷', width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_divide.grid(row=7,column=25,columnspan=6,padx=4,pady=2)
button_1 =tk.Button(root,text='1', width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_1.grid(row=8,column=1,columnspan=6,padx=4,pady=2)
button_2 = tk.Button(root,text='2', width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_2.grid(row=8,column=7,columnspan=6,padx=4,pady=2)
button_3 = tk.Button(root, text='3', width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_3.grid(row=8,column=13,columnspan=6,padx=4,pady=2)
button_add = tk.Button(root,text='+', width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_add.grid(row=8,column=19,columnspan=6,padx=4,pady=2)
button_subtract = tk.Button(root,text='-', width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_subtract.grid(row=8,column=25,columnspan=6,padx=4,pady=2)
button_0 = tk.Button(root,text='0', width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_0.grid(row=9,column=1,columnspan=6,padx=4,pady=2)
button_point = tk.Button(root,text='·',width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_point.grid(row=9,column=7,columnspan=6,padx=4,pady=2)
button_magnitude = tk.Button(root, text='×10ˣ', width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_magnitude.grid(row=9,column=13,columnspan=6,padx=4,pady=2)
button_ANS = tk.Button(root,text='Ans', width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_ANS.grid(row=9,column=19,columnspan=6,padx=4,pady=2)
button_equal = tk.Button(root, text='=', width=5, font=font_16, relief=tk.FLAT, bg='#efefef')
button_equal.grid(row=9,column=25,columnspan=6,padx=4,pady=2)
"""特殊运算符转换"""
special_list =['×','÷']
special_dict = {'×' :'*',
           '÷' :'/',
           }
"""计算函数"""
def click_button(x,y):#应当渲染出符合latex表达式的函数,仍然使用output.num变量进行显示，但使用caculate变量进行运算
    if y==0:#一般运算
     output_num.set(output_num.get() + x)
def clearone():
    string = output_num.get()
    output_num.set(string[:-1])
def clearall():
    output_num.set('')
def calculate():#计算函数,实现了使用qal计算，尚未解决复杂运算问题
    string = output_num.get()
    string_list = list(string)
    for i in string_list:#字符合法性审查第一部分-特殊字符转化
        if i in special_list:
            order = string_list.index(i)
            string_list[order]=special_dict[i]
    string =''.join(string_list)
    #启动qalculate
    result = subprocess.Popen(shlex.split( './qalculate/qalc.exe'),stdout=subprocess.PIPE,stdin=subprocess.PIPE,text=True,universal_newlines=True)
    result.stdin.write(f'{string}\n')
    result.stdin.close()#关闭stdin以保证进程正常结束
    #等待进程结束
    return_code = result.wait()
    qalc_result = result.stdout.read()
    qalc_result_list = qalc_result.split('\n')
    output_result = qalc_result_list[2]
    print(output_result)
    # 使用正则表达式去除 ANSI 转义码
    output_result = re.sub(r'\x1b\[[0-9;]*m', '', output_result)
    output_result = output_result.encode('utf-8')
    # 使用字节模式的分隔符进行分割
    ANS_list = output_result.split(b' ')
    ANS = ANS_list[-1].decode('utf-8')
    #设置输出
    output_num.set(ANS)
    # 输出标准错误
    error_result = result.stderr.read() if result.stderr else None  # 检查 stderr 是否为 None
    if error_result:
        print(f"错误信息：{error_result}")
"""一般字符按钮"""
button_0.config(command=lambda: click_button('0',0))
button_1.config(command=lambda: click_button('1',0))
button_2.config(command=lambda: click_button('2',0))
button_3.config(command=lambda: click_button('3',0))
button_4.config(command=lambda: click_button('4',0))
button_5.config(command=lambda: click_button('5',0))
button_6.config(command=lambda: click_button('6',0))
button_7.config(command=lambda: click_button('7',0))
button_8.config(command=lambda: click_button('8',0))
button_9.config(command=lambda: click_button('9',0))
button_add.config(command=lambda: click_button('+',0))
button_subtract.config(command=lambda: click_button('-',0))
button_multiply.config(command=lambda: click_button('×',0))
button_divide.config(command=lambda: click_button('÷',0))
button_ANS.config(command=lambda: click_button('ANS',0))
button_point.config(command=lambda: click_button('.',0))

"""多字符按钮"""#尚未实现的运算有分式、积分导数、调用、数值转换
"""y=0普通类"""
button_magnitude.config(command=lambda: click_button('×10^',0))
button_Power.config(command=lambda: click_button('^',0))
button_sin.config(command=lambda: click_button('sin',0))
button_cos.config(command=lambda: click_button('cos',0))
button_tan.config(command=lambda: click_button('tan',0))
button_Lbracket.config(command=lambda: click_button('(',0))
button_Rbracket.config(command=lambda: click_button(')',0))
button_Squared.config(command=lambda: click_button('^0.5',0))
button_ln.config(command=lambda: click_button('ln',0))
button_log.config(command=lambda: click_button('log',0))
button_negative.config(command=lambda: click_button('-',0))

"""y≠0特殊类"""
button_Square.config(command=lambda: click_button('^2',0))#根式较为特殊\sqrt[n]{}
button_Fraction.config(command=lambda: click_button('frac',0))#分式较为特殊，应换行符的使用\frac{}{}
"""特殊功能按钮"""
button_DEL.config(command=lambda: clearone())
button_AC.config(command=lambda: clearall())
button_equal.config(command=lambda: calculate())

root.mainloop()