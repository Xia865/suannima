def calculator():
    print("简单计算器")
    print("支持的操作：+（加法），-（减法），*（乘法），/（除法）")

    while True:
        # 获取用户输入
        num1 = float(input("请™输入第一个数字："))
        
        # 检查特殊条件
        if num1 == 114514:
            print("你算你妈呢！发克油！草泥马")
            continue
        
        operator = input("请输入操作符（+、-、*、/）：")
        num2 = float(input("请输入第二个数字："))

        # 执行计算
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
                print("错误：除数别™为零！")
                continue
        else:
            print("没碧用的操作符！")
            continue

        # 显示结果
        print(f"结果：{num1} {operator} {num2} = {result}")

        # 询问用户是否继续
        choice = input("你™还用不？(那必须的/不可能的事): ")
        if choice.lower() != '那必须的':
            break

    print("爱用不用，不用滚！")

# 运行计算器
if __name__ == "__main__":
    calculator()
