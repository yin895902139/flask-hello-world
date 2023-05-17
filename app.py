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
      </style>
    </head>
    <body>
      <h1 class="animated-text">我爱你，小莹！\u2764</h1>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()