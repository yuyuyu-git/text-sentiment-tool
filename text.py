import pandas as pd

# 正面词库
positive_words = {
    '好', '很好', '非常好', '真好', '太好了', '棒', '很棒', '优秀', '出色', '满意',
    '喜欢', '开心', '高兴', '快乐', '愉快', '舒畅', '舒服', '轻松',
    '推荐', '值得', '不错', '挺好', '靠谱', '给力', '赞', '支持',
    '进步', '改善', '完美', '良心', '划算', '超值',
    '感谢', '温暖', '幸福', '美好', '阳光', '希望'
}

# 负面词库
negative_words = {
    '差', '很差', '极差', '太差', '烂', '垃圾',
    '恶心', '讨厌', '烦', '失望', '崩溃', '无语',
    '坑', '骗人', '假', '难用', '不好吃', '难吃',
    '慢', '卡', '贵', '太贵', '不值', '浪费',
    '后悔', '糟糕', '倒霉', '痛苦', '累', '疲惫',
    '失败', '拒绝', '心累'
}

def analyze_sentiment(text):
    if not isinstance(text, str) or len(text.strip()) == 0:
        return "中性"
    pos_count = sum(1 for w in positive_words if w in text)
    neg_count = sum(1 for w in negative_words if w in text)
    if pos_count > neg_count:
        return "正面"
    elif neg_count > pos_count:
        return "负面"
    return "中性"

test_data = pd.DataFrame({
    "text": [
        "今天天气真好，心情特别舒畅",
        "这家餐厅太难吃了，服务态度极差",
        "这个产品不错，值得购买",
        "老板人很好，很负责任",
        "下雨天堵车，真烦人",
        "一般般吧，还行"
    ]
})

# 应用分析
test_data["情感分类"] = test_data["text"].apply(analyze_sentiment)

# 保存为 Excel（这一步如果报错，说明文件被占用，关掉 Excel 再运行）
test_data.to_excel("test_结果.xlsx", index=False)

print("处理完成！结果保存在 test_结果.xlsx")
print(test_data)