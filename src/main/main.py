"""This module is used to write main function"""
import sys
from src.driver.scientific_calc import ScientificCalc


def main():
    """This main function is used to get input from user and call the exponential_function"""
    obj_exp = ScientificCalc()
    power = sys.argv[1]
    print(obj_exp.exponential_func(power))
