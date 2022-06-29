"""
数字挑战计算器

@author: zhouhuajian
@version: v1.2
"""


class DigitChallengeCalculator:
    """数字挑战计算器"""

    def __init__(self):
        """初始化"""
        self.digits = list(range(1, 10))  # 1 2 3 4 5 6 7 8 9

    def start_calculate(self, exp: str) -> str:
        """开始计算"""
        # TODO: 目前暂且只支持2-5个问号，排列组合算法可能可以优化
        qmark_num = exp.count('?')
        # 让表达式变成结果为布尔值的表达式
        # 另外把?变成{}，这样可以使用字符串的format方法
        try:
            equal_sign_index = exp.index("=")
        except ValueError:
            raise ValueError("必须要有=号")
        exp = exp[:equal_sign_index] + '=' + exp[equal_sign_index:]
        exp = exp.replace("?", "{}")
        result = ''
        if qmark_num < 2:
            raise ValueError("?必须2个以上")
        elif qmark_num == 2:
            result = self.calculate_qmark_2(exp)
        elif qmark_num == 3:
            result = self.calculate_qmark_3(exp)
        elif qmark_num == 4:
            result = self.calculate_qmark_4(exp)
        elif qmark_num == 5:
            result = self.calculate_qmark_5(exp)
        # 两个等号变成一个
        return result.replace("==", '=')

    def calculate_qmark_2(self, exp: str) -> str:
        """2个问号"""
        for num_1 in self.digits:
            for num_2 in self.get_digits_exclude(num_1):
                new_exp = exp.format(num_1, num_2)
                # 如果执行后为True，则得到答案
                if eval(new_exp):
                    return new_exp
        return ''

    def calculate_qmark_3(self, exp) -> str:
        """3个问号"""
        for num_1 in self.digits:
            for num_2 in self.get_digits_exclude(num_1):
                for num_3 in self.get_digits_exclude(num_1, num_2):
                    new_exp = exp.format(num_1, num_2, num_3)
                    # 如果执行后为True，则得到答案
                    if eval(new_exp):
                        return new_exp
        return ''

    def calculate_qmark_4(self, exp) -> str:
        """4个问号"""
        for num_1 in self.digits:
            for num_2 in self.get_digits_exclude(num_1):
                for num_3 in self.get_digits_exclude(num_1, num_2):
                    for num_4 in self.get_digits_exclude(num_1, num_2, num_3):
                        new_exp = exp.format(num_1, num_2, num_3, num_4)
                        # 如果执行后为True，则得到答案
                        if eval(new_exp):
                            return new_exp
        return ''

    def calculate_qmark_5(self, exp) -> str:
        """5个问号"""
        for num_1 in self.digits:
            for num_2 in self.get_digits_exclude(num_1):
                for num_3 in self.get_digits_exclude(num_1, num_2):
                    for num_4 in self.get_digits_exclude(num_1, num_2, num_3):
                        for num_5 in self.get_digits_exclude(num_1, num_2, num_3, num_4):
                            new_exp = exp.format(
                                num_1, num_2, num_3, num_4, num_5
                            )
                            # 如果执行后为True，则得到答案
                            if eval(new_exp):
                                return new_exp
        return ''

    def get_digits_exclude(self, *exclude_nums) -> list:
        """获取数字里列表，排查exclude_nums里面的数字"""
        return list(set(self.digits).difference(set(exclude_nums)))


if __name__ == '__main__':
    print("共9个数字 1 2 3 4 5 6 7 8 9")
    print("不能重复使用")
    print("请输入表达式，例如(?+?)*?=21")
    calculator = DigitChallengeCalculator()
    while True:
        exp = input("Input: ")
        try:
            result = calculator.start_calculate(exp)
            if not result:
                print("没有正确答案，请检查输入是否正确")
                continue
        except Exception as e:
            result = repr(e)
        print("Output: " + result)
