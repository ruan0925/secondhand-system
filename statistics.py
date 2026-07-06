from data_manager import load_data
import streamlit as st
import pandas as pd
from ui import empty_state, page_header, section_title

def show_statistics():
    products = load_data("products")
    orders = load_data("orders")
    page_header("📊", "数据统计看板", "基于当前 JSON 数据生成项目运行概览，便于课程答辩展示。")
    total_goods = len(products)
    total_order = len(orders)
    
    cate_count = {}
    for good in products:
        cate = good["category"]
        cate_count[cate] = cate_count.get(cate, 0) + 1
        
    if cate_count:
        hot_cate = max(cate_count, key=cate_count.get)
    else:
        hot_cate = "暂无"

    col1, col2, col3 = st.columns(3)
    col1.metric("商品总数", total_goods)
    col2.metric("订单总数", total_order)
    col3.metric("最热门商品类别", hot_cate)

    section_title("商品分类分布")
    if cate_count:
        chart_data = pd.DataFrame(
            [{"分类": cate, "商品数量": count} for cate, count in cate_count.items()]
        )
        st.bar_chart(chart_data.set_index("分类"))
        st.dataframe(chart_data, use_container_width=True, hide_index=True)
    else:
        empty_state("📊", "暂无商品分类数据", "发布商品后，这里会自动展示各分类的商品数量。")
