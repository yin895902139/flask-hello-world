from flask import Flask
import datetime

app = Flask(__name__)

start_time = datetime.datetime(2022, 5, 20)  # 设置起始时间

@app.route('/')
def hello_world():
    current_time = datetime.datetime.now()
    time_difference = current_time - start_time

    days = time_difference.days
    minutes, seconds = divmod(time_difference.seconds, 60)
    hours, minutes = divmod(minutes, 60)

    return f'''
    <html>
    <head>
      <style>
        /* 定义动画效果 */
        @keyframes text-animation {{
          0% {{ opacity: 0; }}
          50% {{ opacity: 1; }}
          100% {{ opacity: 0; }}
        }}
        
        /* 应用动画到文字元素 */
        .animated-text {{
          animation: text-animation 2s infinite;
        }}
        
        /* 设置桃心字符的文本颜色为红色 */
        .heart {{
          color: red;
        }}
      </style>
      <script>
        function updateTime() {{
          var element = document.getElementById("time-together");
          var timeString = "{days}天 {hours}小时 {minutes}分钟 {seconds}秒";
          element.innerText = "我们在一起已经 " + timeString;
        }}
        
        setInterval(updateTime, 1000); // 每秒更新一次时间
      </script>
    </head>
    <body>
      <h1 class="animated-text">我爱你<span class="heart">❤</span>，小莹！</h1>
      <p id="time-together"></p>
      <script>
        updateTime(); // 初始化时间
      </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
