from console import output_system_func
from console import output_creator_func
from victory import victory_test

def test_output_system_func():
    assert output_system_func() == 'Моя операционная система это - win32, nt'
def test_output_creator_func():
    assert output_creator_func() == 'Создатель программы - Борис Животное'
