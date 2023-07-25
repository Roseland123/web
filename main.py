import streamlit as st
import logging
from dotenv import load_dotenv
import os


# Load the .env file to access the environment variables
load_dotenv()

# Get the values of the environment variables
api_key = os.getenv("STREAMLIT_API_KEY")
password = os.getenv("STREAMLIT_PASSWORD")
other_secret = os.getenv("STREAMLIT_OTHER_SECRET")

def configure_logging():
    # 设置日志级别为INFO，这样只记录INFO级别及以上的日志
    logging.basicConfig(level=logging.INFO)

def save_to_log(name, email, message):
    # 将用户留言写入日志文件
    logging.info(f"用户留言：姓名={name}, 邮箱={email}, 留言={message}")

def main():
    configure_logging()
    # 自定义CSS样式
    custom_css = """
    <style>

    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # 设置页面标题和描述
    st.title("重庆鑫迎鑫物业管理有限公司")
    st.write('欢迎来到公司网站！')

    # 添加公司介绍
    st.header('公司介绍')
    st.write('重庆鑫迎鑫物业管理有限公司是一家客户至上的专业物业管理服务提供商，我们始终将客户的需求和利益放在首位。针对川渝地区的业主和社区，我们提供全面的物业管理解决方案，确保为每一位客户创造最优质的物业服务体验')
    st.write('我们坚信客户至上是成功的基石。我们以关注和尊重每一位客户为己任。我们深入了解客户的需求，提供量身定制的服务方案，并通过持续沟通和反馈机制，不断优化和改进服务。')
    st.write('我们致力于建立长期的合作关系，通过诚信和透明的经营理念，赢得客户的信赖与支持。在我们的服务中，每一位客户都能感受到被重视和尊重，我们以客户的满意度为导向，持续提升服务品质。')
    st.write('我们理解物业管理对业主的重要性，因此我们始终以客户的利益为先，竭尽全力创造舒适、便捷和安心的居住环境。我们注重细节，确保物业的安全、干净和有序，让客户放心地享受美好生活。')
    st.write('如果您正在寻找一家真正以客户为中心的物业管理公司，ABC物业管理公司将是您的不二选择。我们期待与您合作，为您带来独特而出色的物业管理体验！')

    # 添加公司图片
    st.image('https://gchzfy.hncourt.gov.cn/upload/image/20211009/20211009094821_47261.jpg', caption='ABC物业公司照片')

    # 添加公司联系人方式
    st.header('联系人方式')
    st.write('电话：15223452401')
    st.write('邮箱：letisiafu@hotmail.com')

    # 添加联系表单
    st.header('联系我们')
    name = st.text_input('姓名', max_chars=50)
    email = st.text_input('邮箱', max_chars=100)
    message = st.text_area('留言', max_chars=500)
    submit_button = st.button('提交')

    if submit_button:
        # 保存用户留言到日志
        save_to_log(name, email, message)
        st.success('感谢您的留言！我们会尽快与您联系。')

if __name__ == '__main__':
    # 设置Streamlit应用程序的主题和背景
    st.set_page_config(page_title="重庆鑫迎鑫物业管理有限公司", page_icon="🏢", layout="wide", initial_sidebar_state="auto" )
    main()
