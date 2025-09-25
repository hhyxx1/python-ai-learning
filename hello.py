# 保存为 week1/hello.py
"""
我的第一个Python程序
作者：[侯宇轩]
日期：2025-09-25
目标：验证Python环境配置成功
"""

import sys
import platform
from datetime import datetime

def print_section(title):
    """打印格式化的章节标题"""
    print("\n" + "="*50)
    print(f" {title} ")
    print("="*50)

def main():
    """主程序"""
    # 1. 基础输出
    print_section("Hello, AI World!")
    print("🎉 恭喜！Python环境配置成功！")
    print("🚀 让我们开始AI学习之旅！")
    
    # 2. 系统信息
    print_section("系统信息")
    print(f"Python版本：{sys.version}")
    print(f"操作系统：{platform.system()} {platform.release()}")
    print(f"处理器：{platform.processor()}")
    print(f"当前时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 3. Python路径
    print_section("Python环境")
    print(f"Python可执行文件：{sys.executable}")
    print(f"Python路径：")
    for i, path in enumerate(sys.path[:5], 1):
        print(f"  {i}. {path}")
    
    # 4. 个人信息（修改这部分）
    print_section("学员信息")
    student = {
        "姓名": "侯宇轩",
        "目标": "掌握AI编程",
        "决心": "每天学习2小时",
        "梦想": "成为AI工程师"
    }
    
    for key, value in student.items():
        print(f"{key}：{value}")
    
    # 5. 第一个交互
    print_section("交互测试")
    name = input("请输入你的名字：")
    print(f"Hello, {name}! 欢迎加入AI学习！")
    
    # 6. 简单计算
    print_section("Python计算测试")
    numbers = [1, 2, 3, 4, 5]
    print(f"数字列表：{numbers}")
    print(f"总和：{sum(numbers)}")
    print(f"平均值：{sum(numbers)/len(numbers)}")
    print(f"最大值：{max(numbers)}")
    print(f"最小值：{min(numbers)}")
    
    print_section("测试完成！")
    print("✅ 所有功能正常")
    print("📚 现在可以开始学习了！")

if __name__ == "__main__":
    main()