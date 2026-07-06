from data_manager import load_data, save_data
import streamlit as st
from ui import empty_state, order_card, page_header, product_card, section_title

def create_order(user):
    products = load_data("products")
    orders = load_data("orders")

    if not products:
        empty_state("🧺", "暂无商品可以下单", "当前没有在售商品，等有商品发布后再来选购。")
        return

    page_header("🧾", "选购商品下单", "先查看可购买商品，再输入商品 ID 完成下单。")
    section_title("可购买商品清单")
    cols = st.columns(3)
    for index, p in enumerate(products):
        with cols[index % 3]:
            product_card(p, show_owner=False)

    section_title("确认下单")
    txt = st.text_input("请输入商品ID:", placeholder="输入上方卡片中的商品 ID")
    if st.button("确认下单", use_container_width=True):
        try:
            product_id = int(txt)
        except ValueError:
            st.error("商品ID必须是纯数字！")
            return

        find_p = None
        for p in products:
            if p["id"] == product_id:
                find_p = p
                break
        if find_p:
            order = {
                "user": user,
                "product": find_p["name"],
                "price": find_p["price"]
            }
            orders.append(order)
            save_data("orders", orders)
            st.success("下单成功！")
        else:
            st.error("商品ID不存在")

def show_orders(user):
    orders = load_data("orders")
    page_header("📦", "我的全部订单", "查看当前登录账号产生的所有订单记录。")
    find_flag = False
    user_orders = []
    for o in orders:
        if o["user"] == user:
            user_orders.append(o)
            find_flag = True
    if not find_flag:
        empty_state("📦", "你还没有任何订单", "完成一次下单后，订单会显示在这里。")
    else:
        section_title(f"共 {len(user_orders)} 条订单记录")
        cols = st.columns(3)
        for index, o in enumerate(user_orders):
            with cols[index % 3]:
                order_card(o, user)
