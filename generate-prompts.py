sentence_template = """
Need to generate test cases for a given function description. 

public class Calculator {{
{new_function_description}
}}

Provide only the code.
public class CalculatorTest {{
    @Test
    public void 
"""

def generate_sentences(sentence_template, new_function_description):
    templates = sentence_template.format(new_function_description=new_function_description)
    return templates


function_descriptions = [
"""
/**
* Adds two numbers.
*
* @param a First operand
* @param b Second operand
* @return The sum of a and b
*/
public static double add(double a, double b) {
    return a + b;
}
""", 
"""
/**
* Subtracts the second number from the first number.
*
* @param a First operand
* @param b Second operand
* @return The result of subtracting b from a
*/
public static double subtract(double a, double b) {
    return a - b;
}
""",
"""
/**
* Multiplies two numbers.
*
* @param a First operand
* @param b Second operand
* @return The product of a and b
*/
public static double multiply(double a, double b) {
    return a * b;
}
""",
"""
/**
* Divides the first number by the second number.
*
* @param a Numerator
* @param b Denominator
* @return The result of dividing a by b
* @throws ArithmeticException If the denominator is zero
*/
public static double divide(double a, double b) {
    if (b == 0) {
        throw new ArithmeticException("Cannot divide by zero.");
    }
    return a / b;
}
""",
"""
/**
* Calculates the square root of a given number.
*
* @param a The number for which the square root is calculated.
* @return The square root of the input number.
* @throws ArithmeticException If the input number is negative, as the square root of
*                             a negative number is not defined in the real number system.
*/
public static double squareRoot(double a) {
    if (a < 0) {
        throw new ArithmeticException("Cannot calculate square root of a negative number.");
    }
    return Math.sqrt(a);
}
""",
"""
/**
* Calculates the percentage value of a given number.
*
* @param a The number for which the percentage is calculated.
* @return The percentage value of the input number.
*/
public static double percentage(double a) {
    return a / 100;
}
""",
"""
/**
* Calculates the modulus (remainder) of dividing one number by another.
*
* @param a The dividend (the number to be divided).
* @param b The divisor (the number by which the dividend is divided).
* @return The remainder when dividing the dividend by the divisor.
* @throws ArithmeticException If the divisor is zero, as division by zero is undefined.
*/
public static double modulus(double a, double b) {
    if (b == 0) {
        throw new ArithmeticException("Cannot calculate modulus with zero divisor.");
    }
    return a % b;
}
""",
"""
/**
* Calculates the result of raising a base to a specified exponent.
*
* @param base     The base number.
* @param exponent The exponent to which the base is raised.
* @return The result of raising the base to the exponent.
*/
public static double power(double base, double exponent) {
    return Math.pow(base, exponent);
}
""",
"""
/**
* Calculates the sine of an angle specified in degrees.
*
* @param angleInDegrees The angle in degrees.
* @return The sine of the given angle.
*/
public static double sin(double angleInDegrees) {
    return Math.sin(Math.toRadians(angleInDegrees));
}
""",
"""
/**
* Calculates the cosine of an angle specified in degrees.
*
* @param angleInDegrees The angle in degrees.
* @return The cosine of the given angle.
*/
public static double cos(double angleInDegrees) {
    return Math.cos(Math.toRadians(angleInDegrees));
}
""",
"""
/**
* Calculates the tangent of an angle specified in degrees.
*
* @param angleInDegrees The angle in degrees.
* @return The tangent of the given angle.
*/
public static double tan(double angleInDegrees) {
    return Math.tan(Math.toRadians(angleInDegrees));
}
""",
"""
/**
* Calculates the logarithm (base 10) of a positive number.
*
* @param a The positive number for which the logarithm is calculated.
* @return The logarithm (base 10) of the input number.
* @throws ArithmeticException If the input number is non-positive, as logarithms of non-positive numbers are undefined.
*/
public static double log(double a) {
    if (a <= 0) {
        throw new ArithmeticException("Cannot calculate logarithm for non-positive number.");
    }
    return Math.log10(a);
}
""",
"""
/**
* Calculates the exponential function (e^x) for a given number.
*
* @param a The exponent for the exponential function.
* @return The result of raising the mathematical constant 'e' to the power of the input exponent.
*/
public static double exp(double a) {
    return Math.exp(a);
}
"""
]

i=1
for description in function_descriptions:
    file_path = f'./prompts-2/{i}.txt'
    result = generate_sentences(sentence_template, description)
    with open(file_path, 'w') as file:
            file.write(result)
    i+=1

print('finish')
    
