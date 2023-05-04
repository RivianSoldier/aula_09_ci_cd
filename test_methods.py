import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_sum_values():
    # given number 1 = 5 and number 2 = 5
    num1 = 5
    num2 = 5

    # when we calculate the sum
    output = methods.sum_values(num1, num2)

    # then the result must be 10
    assert output == 10

def test_subtraction():
    # given number 1 = 10 and number 2 = 5
    num1 = 10
    num2 = 5

    # when we calculate the subtraction of the values
    output = methods.sub(num1, num2)

    # then the result must be 5
    assert output == 5

def test_multiplication():
    # given number 1 = 5 and number 2 = 5
    num1 = 5
    num2 = 5

    # when we calculate the multiplication of the values
    output = methods.mult(num1, num2)

    # then the result must be 25
    assert output == 25

def test_division():
    # given number 1 = 10 and number 2 = 5
    num1 = 10
    num2 = 5

    # when we calculate the division of the values
    output = methods.div(num1, num2)

    # then the result must be 2
    assert output == 2