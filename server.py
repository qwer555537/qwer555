from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {
        "origins": "*",
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# 预设的回复模板
RESPONSES = [
    "哈哈哈，你说得对！😆",
    "啊？我刚才在发呆，没听清...😅",
    "这个嘛...让我想想...🤔",
    "我觉得可以去吃火锅！🍲",
    "你说什么都对！我先去睡觉了...😴",
    "这个问题太难了，我要去问问我的猫咪...🐱",
    "我刚才在想一个特别好笑的事情...😂",
    "要不我们去跳舞吧！💃",
    "这个问题嘛...（开始傻笑）😝"
]

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({"error": "消息不能为空"}), 400

        # 随机选择一个回复
        response = random.choice(RESPONSES)
        
        # 添加一点延迟，模拟思考时间
        time.sleep(0.3)
        
        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": "服务器遇到了问题"}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)