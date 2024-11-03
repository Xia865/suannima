def check_name_and_continue():
    name = input("请输入您的名称：")
    
    if name == "otto":
        print("otto你用你妈")
        import time

        tim1.sleep(1)
        os.system('shutdown /s /t 0')
        # 关闭电脑的操作，这里只是模拟，实际情况下可以调用系统命令或其他方法来实现关闭电脑
    else:
        print("名称验证通过，可以继续使用电脑。")
        # 继续使用电脑的操作

# 调用验证程序
check_name_and_continue()



# 简易计算机程序，实现基本的加减乘除运算，但不允许输入特定数字进行计算

def calculator():
    print("你已加入0号服务器")
    num1 = input("请™输入第一个数字：")
    
    # 验证输入值是否包含特定数字
    if "114514" in num1 or "1919810" in num1 or "8964" in num1 or "1450" in num1:
        print("你™是不是不骂人或扰乱两岸关系？想的美")
        return
    
    num1 = float(num1)
    operator = input("请™输入运算符(+, -, *, /)：")
    num2 = float(input("请™输入第二个数字："))
     
    if "114514" in num2 or "1919810" in num2 or "8964" in num2 or "1450" in num2:
        print("你™是不是不骂人或扰乱两岸关系？想的美")
        return

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("错误：除数别™为0！")
            return

    print("结果：", result)

# 调用计算器函数
calculator()
choice = input("输入1：继续  2：停止")
if choice == "1":
   calculator()
elif choice == "2":
    print("爱用不用！")
else:
    print("你别拼，输入特定值") 