from flask import Flask
import datetime

app = Flask(__name__)

start_time = datetime.datetime(2022, 5, 20)  # 设置起始时间

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
          var current_time = new Date();
          var start_time = new Date("{start_time}");
          var time_difference = current_time - start_time;

          var days = Math.floor(time_difference / (1000 * 60 * 60 * 24));
          var minutes = Math.floor((time_difference % (1000 * 60 * 60)) / (1000 * 60));
          var seconds = Math.floor((time_difference % (1000 * 60)) / 1000);

          var element = document.getElementById("time-together");
          var timeString = days + "天 " + hours + "小时 " + minutes + "分钟 " + seconds + "秒";
          element.innerHTML = "我们在一起已经 " + timeString;
        }
        
        window.setInterval(updateTime, 1000); // 每秒更新一次时间
      </script>
    </head>
    <body onload="updateTime()"> <!-- 使用 onload 事件调用 updateTime 函数 -->
      <h1 class="animated-text">我爱你<span class="heart">❤</span>，小莹！</h1>
      <p id="time-together"></p>
      <img src="https://c-ssl.duitang.com/uploads/blog/202209/22/20220922161509_bc733.jpeg" alt="">
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()



