import streamlit as st
from user import register, login
from product import add_product, show_products
from order import create_order, show_orders
from recommend import recommend_products
from statistics import show_statistics
from data_manager import load_data
from html import escape
from ui import apply_global_style, product_card, section_title

st.set_page_config(
    page_title="校园二手交易系统",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

def show_home():
    products = load_data("products")
    orders = load_data("orders")
    users = load_data("users")

    cate_count = {}
    for product in products:
        cate = product["category"]
        cate_count[cate] = cate_count.get(cate, 0) + 1
    hot_cate = max(cate_count, key=cate_count.get) if cate_count else "暂无"

    st.markdown("""
    <div class="hero">
        <h1>校园二手交易与推荐系统</h1>
        <p>面向校园闲置物品流通的轻量化交易平台，支持账号注册登录、商品发布浏览、分类推荐、在线下单和数据统计，适合课程项目答辩演示。</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("在售商品", len(products))
    col2.metric("订单数量", len(orders))
    col3.metric("注册用户", len(users))
    col4.metric("热门分类", hot_cate)

    section_title("🌟 平台功能概览")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="soft-card">
            <h3>商品发布与浏览</h3>
            <p>学生可以发布闲置商品，浏览全部在售物品，快速了解价格、分类和卖家。</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="soft-card">
            <h3>分类推荐</h3>
            <p>根据输入的商品类别筛选同类商品，保持原有推荐规则，展示更清晰。</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="soft-card">
            <h3>订单与统计</h3>
            <p>登录后可按商品 ID 下单、查看个人订单，并通过统计页展示项目数据。</p>
        </div>
        """, unsafe_allow_html=True)

    section_title("🛍️ 最新商品预览")
    if not products:
        st.info("暂无商品，登录后可以发布第一件校园闲置物品。")
    else:
        preview_cols = st.columns(3)
        for index, product in enumerate(products[-3:]):
            with preview_cols[index % 3]:
                product_card(product)

# 初始化登录会话
if "current_user" not in st.session_state:
    st.session_state.current_user = None

apply_global_style()

# 左侧侧边栏导航
with st.sidebar:
    st.title("🎓 校园集市")
    if st.session_state.current_user:
        current_user = escape(str(st.session_state.current_user))
        st.markdown(f'<div class="status-pill">当前用户：{current_user}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-pill">当前状态：未登录</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.caption("功能导航")
    opt = st.selectbox("请选择功能",
        ["🏠 首页", "📝 注册账号", "🔐 用户登录", "🛍️ 浏览全部商品", "➕ 发布我的商品",
         "✨ 按类别推荐商品", "🧾 选购商品下单", "📦 查看我的订单", "📊 数据统计", "🚪 退出登录"])

# 功能分发
if opt == "🏠 首页":
    show_home()
elif opt == "📝 注册账号":
    register()
elif opt == "🔐 用户登录":
    res = login()
    if res:
        st.session_state.current_user = res
elif opt == "🛍️ 浏览全部商品":
    show_products()
elif opt == "➕ 发布我的商品":
    if st.session_state.current_user:
        add_product(st.session_state.current_user)
    else:
        st.warning("请先登录账号，再发布商品。")
elif opt == "✨ 按类别推荐商品":
    recommend_products()
elif opt == "🧾 选购商品下单":
    if st.session_state.current_user:
        create_order(st.session_state.current_user)
    else:
        st.warning("请先登录账号，再选购商品。")
elif opt == "📦 查看我的订单":
    if st.session_state.current_user:
        show_orders(st.session_state.current_user)
    else:
        st.warning("请先登录账号，再查看订单。")
elif opt == "📊 数据统计":
    show_statistics()
elif opt == "🚪 退出登录":
    st.session_state.current_user = None
    st.info("已退出登录，欢迎下次继续使用校园集市。")
