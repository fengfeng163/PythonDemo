class Calculator:
    """简单的计算器类，支持基本算术运算"""
    
    # 版本信息
    VERSION = "1.0.0"
    
    def add(self, a, b):
        """返回a加b的结果"""
        return a + b
    
    def subtract(self, a, b):
        """返回a减b的结果"""
        return a - b
    
    def multiply(self, a, b):
        """返回a乘b的结果"""
        return a * b
    
    def divide(self, a, b):
        """返回a除以b的结果，除数为0时抛出ValueError"""
        if b == 0:
            raise ValueError("除数不能为0")
        return a / b
    
    def print_version(self):
        """打印当前计算器的版本信息"""
        print(f"计算器版本: {self.VERSION}")
