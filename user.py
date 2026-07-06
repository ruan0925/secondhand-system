from data_manager import load_data, save_data
import streamlit as st
from ui import page_header, side_note

def register():
    users = load_data("users")
    page_header("📝", "用户注册", "创建账号后即可发布商品、选购商品和查看订单。")
    left, right = st.columns([1.1, 0.9])
    with left:
        username = st.text_input("输入用户名", placeholder="例如：student01")
        password = st.text_input("输入密码", type="password", placeholder="请输入登录密码")
    with right:
        side_note("注册说明", "账号数据将保存到本地 JSON 文件，适合课程项目演示。用户名不能重复，密码不能为空。")
    if st.button("完成注册", use_container_width=True):
        if not username or not password:
            st.warning("用户名和密码不能为空！")
            return
        if username in users:
            st.error("用户已存在，换个名字！")
        else:
            users[username] = password
            save_data("users", users)
            st.success("注册成功！可去登录")

def login():
    users = load_data("users")
    page_header("🔐", "用户登录", "登录后可以发布商品、下单购买并查看个人订单。")
    left, right = st.columns([1.1, 0.9])
    with left:
        username = st.text_input("账号", placeholder="请输入用户名")
        password = st.text_input("密码", type="password", placeholder="请输入密码")
    with right:
        side_note("登录提示", "请使用已注册账号登录。登录状态会显示在左侧导航栏，方便答辩时演示不同功能入口。")
    if st.button("登录", use_container_width=True):
        if username in users and users[username] == password:
            st.success("登录成功")
            return username
        else:
            st.error("账号或密码错误")
            return None
    return None
