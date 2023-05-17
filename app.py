from flask import Flask

app = Flask(__name__)

@app.route('/')
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
      <script>
        function updateTime() {
          var element = document.getElementById("current-time");
          var currentTime = new Date().toLocaleTimeString();
          element.innerText = currentTime;
        }
        
        setInterval(updateTime, 1000); // 每秒更新一次时间
      </script>
    </head>
    <body>
      <h1 class="animated-text">我爱你<span class="heart">❤</span>，小莹！</h1>
      <p>当前时间：<span id="current-time"></span></p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
