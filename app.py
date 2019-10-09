from flask import Flask
from flask import url_for
from flask import render_template
from flask import Blueprint
from views.meituan import mtapp

app = Flask(__name__)


# 访问地址为 https://localhost:<port>/
@app.route('/')  # 构建路由 默认为get请求
def index():  # 定义路由对应函数
    '''
    这也对应的路由函数
    :return: 主页对应的网址
    '''
    return render_template('index.html')
    # return 'index 页面!'  # 视图函数处理结果返回网页显示对应内容

@app.route('/taobao/')
def taobao():
    '''
    淘宝网页链接路由
    :return: 淘宝网主页
    '''
    return render_template('./taobao/index.html')

@app.route('/jingdong/')
def jingdong():
    '''

    :return:
    '''
    return render_template('./jingdong/index.html')

@app.route('/meituan/')
def meituan():
    '''

    :return:
    '''
    return render_template('./meituan/index.html')


if __name__ == '__main__':
    app.run(debug=True, port=22222)  # 启动对象， 开发者模式
