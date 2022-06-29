"""
单元测试

@author  : zhouhuajian
@version : v1.0
"""
import pytest

from main import DigitChallengeCalculator

calculator = DigitChallengeCalculator()


@pytest.mark.parametrize(('exp', 'result'), [
    ('?+?=3', '1+2=3'),
    ('?*(?-?)=21', '3*(8-1)=21'),
    ('(?+?)*(?-?)=36', '(1+5)*(8-2)=36'),
    ('(?+?)*(?-?)+?=39', '(1+4)*(8-2)+9=39'),
])
def test_calculate(exp, result):
    """测试2、2、3、4、5个问号"""
    assert calculator.start_calculate(exp) == result

# def test_qmark_2_3_4_5():
#     """测试2、2、3、4、5个问号"""
#     exp_results = [
#         ('?+?=3', '1+2=3'),
#         ('?*(?-?)=21', '3*(8-1)=21'),
#         ('(?+?)*(?-?)=36', '(1+5)*(8-2)=36'),
#         ('(?+?)*(?-?)+?=39', '(1+4)*(8-2)+9=39'),
#     ]
#     for exp, result in exp_results:
#         assert calculator.start_calculate(exp) == result
