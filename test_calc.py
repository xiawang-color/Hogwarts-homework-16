import pytest
from calculator import Calculator
import yaml

class TestCalc:
    #在类之前执行
    def setup_class(self):
        #定义一个类对象
        self.cal=Calculator()
        print("计算开始！")
    #在类之后执行
    def teardown_class(self):
        print("计算结束！")
    #在每个方法之前执行
    def setup_method(self):
        print("计算开始！")
    #在每个方法之后执行
    def teardown_method(self):
        print("计算结束！")

   #参数化的方式
   # @pytest.mark.parametrize("a,b,expect",[(1,2,3),(-1,-2,-3),(100,200,300)])
    #数据驱动的方式，测试加法
    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("./calc.yml")))
    def test_add(self,a,b,expect):
        assert self.cal.add(a,b)==expect

    #参数化的方式，测试减法
    @pytest.mark.parametrize("a,b,expect",[(1,2,-1),(-3,-4,1),(2000,1000,1000)])
    def test_sub(self,a,b,expect):
        assert self.cal.sub(a,b)==expect

    #参数化的方式，测试乘法
    @pytest.mark.parametrize("a,b,expect", [(1, 2, 2), (-3, -4, 12), (20, 10, 200)])
    def test_mul(self, a, b, expect):
        assert self.cal.mul(a, b) == expect

    #参数化的方式，测试除法
    @pytest.mark.parametrize("a,b,expect", [(1, 2, 0.5), (-3, -4, 0.75), (2000, 1000, 2)])
    def test_div(self, a, b, expect):
        assert self.cal.div(a, b) == expect