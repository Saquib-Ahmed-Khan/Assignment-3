import pytest  
from src.area import calculate_area_square  
  
def test_calculate_area_square_negative():  
    with pytest.raises(TypeError):  
        calculate_area_square(-2)  
  
def test_calculate_area_square_string():  
    with pytest.raises(TypeError):  
        calculate_area_square("2")  
  
def test_calculate_area_square_list():  
    with pytest.raises(TypeError):  
        calculate_area_square([2])

def test_calculate_area_square_student_id():
    assert calculate_area_square(97) == 97 * 97
    
def test_calculate_area_square_student_id_fail():
    assert calculate_area_square(97) == 100  # Incorrect expected value
