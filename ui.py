from html import escape

import streamlit as st


def apply_global_style():
    st.markdown("""
    <style>
    :root {
        --primary: #0f766e;
        --primary-dark: #115e59;
        --primary-soft: #e6fffb;
        --accent: #0891b2;
        --text: #0f172a;
        --muted: #64748b;
        --border: #e2e8f0;
        --surface: #ffffff;
        --page: #f8fafc;
        --shadow: 0 12px 28px rgba(15, 23, 42, 0.07);
        --radius: 14px;
    }

    .stApp {
        background:
            radial-gradient(circle at top right, rgba(8,145,178,0.10), transparent 28rem),
            linear-gradient(180deg, #f7fbff 0%, var(--page) 42%, #ffffff 100%);
        color: var(--text);
    }

    .main .block-container {
        max-width: 1180px;
        padding-top: 1.4rem;
        padding-bottom: 3rem;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f766e 0%, #0f5f59 100%);
        border-right: 0;
    }

    [data-testid="stSidebar"] * {
        color: #ffffff;
    }

    [data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
        color: rgba(255,255,255,0.78);
    }

    [data-testid="stSidebar"] div[data-baseweb="select"],
    [data-testid="stSidebar"] div[data-baseweb="select"] * {
        color: var(--text) !important;
    }

    [data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.18);
    }

    h1, h2, h3 {
        letter-spacing: 0;
        color: var(--text);
    }

    .hero {
        position: relative;
        overflow: hidden;
        padding: 34px 36px;
        border-radius: 20px;
        background: linear-gradient(135deg, #0f766e 0%, #0891b2 100%);
        color: white;
        box-shadow: 0 18px 44px rgba(15, 118, 110, 0.20);
        margin-bottom: 22px;
    }

    .hero:after {
        content: "";
        position: absolute;
        right: -60px;
        top: -70px;
        width: 210px;
        height: 210px;
        border-radius: 999px;
        background: rgba(255,255,255,0.15);
    }

    .hero h1 {
        margin: 0 0 10px 0;
        color: #ffffff;
        font-size: clamp(1.75rem, 3vw, 2.35rem);
        line-height: 1.18;
    }

    .hero p {
        max-width: 760px;
        margin: 0;
        color: rgba(255,255,255,0.94);
        font-size: 1.02rem;
        line-height: 1.8;
    }

    .page-head {
        margin: 0 0 18px 0;
        padding-bottom: 14px;
        border-bottom: 1px solid var(--border);
    }

    .page-head h2 {
        margin: 0 0 6px 0;
        font-size: 1.55rem;
        line-height: 1.3;
    }

    .page-head p {
        margin: 0;
        color: var(--muted);
        line-height: 1.7;
    }

    .section-title {
        margin: 24px 0 12px 0;
        color: var(--text);
        font-size: 1.15rem;
        font-weight: 800;
    }

    .soft-card,
    .product-card,
    .order-card,
    .empty-card,
    .side-note {
        background: rgba(255,255,255,0.96);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        box-shadow: var(--shadow);
    }

    .soft-card,
    .product-card,
    .order-card,
    .empty-card {
        padding: 18px;
        min-height: 132px;
        transition: transform 160ms ease, box-shadow 160ms ease, border-color 160ms ease;
    }

    .soft-card:hover,
    .product-card:hover,
    .order-card:hover {
        transform: translateY(-2px);
        border-color: #b6e3de;
        box-shadow: 0 16px 34px rgba(15, 23, 42, 0.10);
    }

    .soft-card h3,
    .product-card h3,
    .order-card h3 {
        margin: 0 0 10px 0;
        color: var(--text);
        font-size: 1.05rem;
        line-height: 1.35;
    }

    .soft-card p,
    .product-card p,
    .order-card p,
    .empty-card p {
        margin: 0;
        color: var(--muted);
        line-height: 1.7;
    }

    .price {
        margin: 4px 0 10px 0;
        color: var(--primary);
        font-size: 1.5rem;
        font-weight: 850;
    }

    .tag-row {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 12px;
    }

    .tag {
        display: inline-flex;
        align-items: center;
        padding: 5px 9px;
        border-radius: 999px;
        background: var(--primary-soft);
        color: var(--primary-dark);
        font-size: 0.82rem;
        font-weight: 700;
    }

    .muted {
        color: var(--muted);
    }

    .empty-card {
        text-align: center;
        padding: 26px 18px;
        background: #ffffff;
    }

    .empty-card .icon {
        margin-bottom: 8px;
        font-size: 1.8rem;
    }

    .side-note {
        padding: 18px;
        background: linear-gradient(180deg, #ffffff 0%, #f8fffe 100%);
    }

    .side-note h3 {
        margin: 0 0 8px 0;
        font-size: 1rem;
        color: var(--text);
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        max-width: 100%;
        padding: 7px 11px;
        border-radius: 999px;
        background: rgba(255,255,255,0.17);
        font-weight: 750;
        overflow-wrap: anywhere;
    }

    div.stButton > button {
        min-height: 42px;
        border: 0;
        border-radius: 11px;
        background: var(--primary);
        color: white;
        font-weight: 750;
        box-shadow: 0 7px 18px rgba(15, 118, 110, 0.18);
        transition: transform 140ms ease, background 140ms ease, box-shadow 140ms ease;
    }

    div.stButton > button:hover {
        transform: translateY(-1px);
        border: 0;
        background: var(--primary-dark);
        color: white;
        box-shadow: 0 11px 24px rgba(15, 118, 110, 0.23);
    }

    div.stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 5px 12px rgba(15, 118, 110, 0.18);
    }

    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div,
    textarea {
        border-radius: 11px !important;
        border-color: var(--border) !important;
        background: #ffffff !important;
    }

    div[data-baseweb="input"]:focus-within > div,
    div[data-baseweb="select"]:focus-within > div,
    textarea:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 3px rgba(15, 118, 110, 0.12) !important;
    }

    [data-testid="stMetric"] {
        padding: 17px 18px;
        border: 1px solid var(--border);
        border-radius: var(--radius);
        background: #ffffff;
        box-shadow: var(--shadow);
    }

    [data-testid="stExpander"] {
        border: 1px solid var(--border);
        border-radius: 12px;
        background: #ffffff;
        box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04);
    }

    [data-testid="stDataFrame"] {
        border-radius: var(--radius);
        overflow: hidden;
        box-shadow: var(--shadow);
    }

    .stAlert {
        border-radius: 12px;
    }

    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        .hero {
            padding: 26px 22px;
            border-radius: 16px;
        }
        .product-card,
        .order-card,
        .soft-card {
            min-height: auto;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def page_header(icon, title, subtitle):
    st.markdown(
        f"""
        <div class="page-head">
            <h2>{escape(icon)} {escape(title)}</h2>
            <p>{escape(subtitle)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_title(text):
    st.markdown(
        f'<div class="section-title">{escape(text)}</div>',
        unsafe_allow_html=True,
    )


def side_note(title, text):
    st.markdown(
        f"""
        <div class="side-note">
            <h3>{escape(title)}</h3>
            <p>{escape(text)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def empty_state(icon, title, text):
    st.markdown(
        f"""
        <div class="empty-card">
            <div class="icon">{escape(icon)}</div>
            <h3>{escape(title)}</h3>
            <p>{escape(text)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def product_card(product, show_owner=True, show_category=True):
    name = escape(str(product["name"]))
    category = escape(str(product["category"]))
    owner = escape(str(product["owner"]))
    price = float(product["price"])

    tags = [f'<span class="tag">ID {product["id"]}</span>']
    if show_category:
        tags.append(f'<span class="tag">{category}</span>')
    if show_owner:
        tags.append(f'<span class="tag">卖家 {owner}</span>')

    st.markdown(
        f"""
        <div class="product-card">
            <h3>{name}</h3>
            <div class="price">￥{price:.2f}</div>
            <p>校园闲置商品</p>
            <div class="tag-row">{''.join(tags)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def order_card(order, user):
    product = escape(str(order["product"]))
    buyer = escape(str(user))
    price = float(order["price"])
    st.markdown(
        f"""
        <div class="order-card">
            <h3>{product}</h3>
            <div class="price">￥{price:.2f}</div>
            <p>购买用户：{buyer}</p>
            <div class="tag-row"><span class="tag">订单记录</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
