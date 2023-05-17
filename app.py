from flask import Flask
app = Flask(__name__)

@app.route('/')
# def hello_world():
#    return '我爱你，小莹！' 
def hello_world():
    return '''
    <html>
    <head>
      <style>
        /* 定义动画效果 */
        @keyframes text-animation {
          0% { opacity: 0; }
          50% { opacity: 1; }
          100% { opacity: 0; }
        }
        
        /* 应用动画到文字元素 */
        .animated-text {
          animation: text-animation 2s infinite;
        }

        /* 设置桃心字符的文本颜色为红色 */
        .heart {
          color: red;
        }

      </style>
    </head>
    <body>
      <h1 class="animated-text">我爱你，小莹<span class="heart">\u2764</span>！</h1>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()