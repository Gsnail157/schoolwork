from stackclass import Stack


def postfix(exp):
    stack = Stack()
    exp = exp.split()
    for i in exp:
        if i == '+':
            right = stack.pop()
            left = stack.pop()
            result = float(left) + float(right)
            stack.push(result)
        elif i == '-':
            right = stack.pop()
            left = stack.pop()
            result = float(left) - float(right)
            stack.push(result)
        elif i == '*':
            right = stack.pop()
            left = stack.pop()
            result = float(left) * float(right)
            stack.push(result)
        elif i == '/':
            right = stack.pop()
            left = stack.pop()
            result = float(left) / float(right)
            stack.push(result)
        else:
            stack.push(i)
    print(f"Result: {stack.top()}")


def main():
    print(f'Welcome to Postfix Calculator')
    print(f'Enter exit to quit')
    while True:
        # try:
        response = input("Enter Expression \n")
        if response == 'exit':
            return

        else:
            postfix(response)

        # except Exception as e:
        #     pass


if __name__ == '__main__':
    main()
