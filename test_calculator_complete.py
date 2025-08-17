import pytest
from calculator import Calculator
import io
import sys

def test_calculator_addition():
    """测试加法功能的各种情况"""
    calc = Calculator()
    # 正常情况
    assert calc.add(2, 3) == 5
    # 包含负数
    assert calc.add(-1, 1) == 0
    assert calc.add(-5, -3) == -8
    # 包含零
    assert calc.add(0, 0) == 0
    assert calc.add(0, 5) == 5
    # 浮点数
    assert calc.add(2.5, 3.5) == 6.0

def test_calculator_subtraction():
    """测试减法功能的各种情况"""
    calc = Calculator()
    # 正常情况
    assert calc.subtract(5, 3) == 2
    # 被减数小于减数
    assert calc.subtract(3, 5) == -2
    # 包含负数
    assert calc.subtract(-1, -1) == 0
    # 包含零
    assert calc.subtract(0, 0) == 0
    assert calc.subtract(0, 5) == -5
    # 浮点数
    assert calc.subtract(6.5, 2.5) == 4.0

def test_calculator_division():
    """测试除法功能的各种情况"""
    calc = Calculator()
    # 正常整除
    assert calc.divide(6, 3) == 2
    # 非整除
    assert calc.divide(5, 2) == 2.5
    # 包含负数
    assert calc.divide(-6, 3) == -2
    assert calc.divide(6, -3) == -2
    assert calc.divide(-6, -3) == 2
    # 除以1
    assert calc.divide(5, 1) == 5
    # 被除数为零
    assert calc.divide(0, 5) == 0
    
    # 测试异常情况：除数为零
    with pytest.raises(ValueError) as excinfo:
        calc.divide(5, 0)
    assert "除数不能为0" in str(excinfo.value)

def test_calculator_version():
    """测试版本信息是否正确"""
    calc = Calculator()
    
    # 检查版本属性
    assert calc.VERSION == "1.0.0"
    
    # 检查版本打印功能
    # 捕获标准输出
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # 调用打印版本方法
    calc.print_version()
    
    # 恢复标准输出
    sys.stdout = sys.__stdout__
    
    # 验证输出内容
    assert captured_output.getvalue().strip() == "计算器版本: 1.0.0"

# 运行测试
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
