# ========================================
# GitHub推送测试文件 - hello_git.py
# 作者: LeaveS-bot | 创建时间: 2025-10-16
# ========================================

print("🎉 恭喜！GitHub推送成功！")
print("=" * 50)


# 简单功能测试
def greet(name="World"):
    return f"👋 Hello, {name}! PyCharm → GitHub 零问题！"


# 主程序
if __name__ == "__main__":
    print(greet("LeaveS-bot"))
    print(greet("Python"))

    # 数据统计（让文件更有意义）
    commits = ["Initial commit", "Add hello_git.py", "🚀 Success!"]
    print(f"\n📊 提交历史: {len(commits)} 次")
    for i, commit in enumerate(commits, 1):
        print(f"  {i}. {commit}")

    print("\n🌟 刷新GitHub查看: https://github.com/LeaveS-bot/submussion")