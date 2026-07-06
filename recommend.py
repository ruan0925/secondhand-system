from data_manager import load_data
import streamlit as st
from ui import empty_state, page_header, product_card, section_title

def recommend_products():
    products = load_data("products")
    if not products:
        empty_state("✨", "暂无商品数据", "当前没有商品，暂时无法进行分类推荐。")
        return
    # input替换为网页输入框
    page_header("✨", "按类别推荐商品", "输入感兴趣的商品类别，系统会展示同类在售商品。")
    categories = sorted({p["category"] for p in products})
    st.caption("当前已有分类：" + "、".join(categories))
    category = st.text_input("请输入你感兴趣的类别：", placeholder="例如：教材")
    if category:
        section_title("为你推荐同类商品")
        flag = False
        matched_products = []
        for p in products:
            if p["category"] == category:
                matched_products.append(p)
                flag = True
        if not flag:
            empty_state("🔎", "该类别暂无在售商品", "可以参考上方已有分类，换一个分类试试。")
        else:
            cols = st.columns(3)
            for index, p in enumerate(matched_products):
                with cols[index % 3]:
                    product_card(p)
