def perform_operation(num1, num2, operation):
   
    num1 = float(num1)
    num2 = float(num2)
    operation = str(operation).lower()
    
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                return("error: division by zero")
            else:
                return num1 / num2
        case _ :
            print("no such operation")
