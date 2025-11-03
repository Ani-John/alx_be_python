def safe_divide (numerator, denominator):
    
    try:
      result = float(numerator)/float(denominator)
      
    except ZeroDivisionError:
        return "Error: You cannot divide by zero"
        
    except ValueError:
       return "Error: Please enter a valid numeric input"
       
    else:
        return result

if __name__ == "__main__":
    main()
