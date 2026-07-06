from data_manager import load_data, save_data
import streamlit as st
from ui import empty_state, page_header, product_card, section_title, side_note

def add_product(user):
    products = load_data("products")
    page_header("➕", "发布新商品", "填写商品基本信息后即可上架，商品数据仍保存到原有 JSON 文件。")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("商品名称", placeholder="例如：高等数学教材")
        price_str = st.text_input("商品价格", placeholder="例如：29.9")
    with col2:
        category = st.text_input("商品分类", placeholder="例如：教材 / 日用品 / 数码")
        side_note("卖家信息", f"当前卖家：{user}。商品上架后会出现在全部商品列表中。")

    if st.button("上架商品", use_container_width=True):
        if not name.strip() or not category.strip():
            st.warning("名称、分类不能为空！")
            return
        try:
            price = float(price_str)
            if price <= 0:
                st.error("价格必须大于0")
                return
        except ValueError:
            st.error("价格请输入合法数字")
            return

        product = {
            "id": len(products) + 1,
            "name": name,
            "price": price,
            "category": category,
            "owner": user
        }
        products.append(product)
        save_data("products", products)
        st.success("商品发布成功！")

def show_products():
    products = load_data("products")
    page_header("🛍️", "全部在售商品", "浏览当前平台中的所有校园闲置物品。")
    if not products:
        empty_state("🧺", "暂无商品", "登录后可以发布第一件商品，商品会自动保存到原有 products.json。")
        return
    section_title(f"共 {len(products)} 件在售商品")
    cols = st.columns(3)
    for index, p in enumerate(products):
        with cols[index % 3]:
            product_card(p)
            with st.expander("查看商品详情"):
                st.write(f"商品编号：{p['id']}")
                st.write(f"商品名称：{p['name']}")
                st.write(f"商品价格：{p['price']} 元")
                st.write(f"商品类别：{p['category']}")
                st.write(f"卖家账号：{p['owner']}")
