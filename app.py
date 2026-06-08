import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.models import Product, User
from src.engine import RecommendationEngine

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="E-Commerce Recommendation Engine",
    page_icon="🛒",
    layout="wide"
)

# ---------------------------
# DATA
# ---------------------------

@st.cache_resource
def load_engine():

    engine = RecommendationEngine()

    products = [

        Product("P01","Apple MacBook Pro M3","Electronics",1999),
        Product("P02","Dell XPS 15","Electronics",1799),
        Product("P03","Sony Headphones","Electronics",399),
        Product("P04","Logitech Mouse","Electronics",99),
        Product("P05","Samsung Monitor","Electronics",299),

        Product("P06","CLRS Algorithms","Books",79),
        Product("P07","Clean Code","Books",49),
        Product("P08","Python Crash Course","Books",59),

        Product("P09","Ergonomic Chair","Office",249),
        Product("P10","Standing Desk","Office",399),

        Product("P11","Hydro Flask","Fitness",39),
        Product("P12","Resistance Bands","Fitness",29)

    ]

    for p in products:
        engine.register_product(p)

    alice = User("U01","Alice")
    alice.add_rating("P01",5)
    alice.add_rating("P04",4)
    alice.add_cart("P03")

    bob = User("U02","Bob")
    bob.add_rating("P06",5)
    bob.add_rating("P07",4)
    bob.add_cart("P08")

    engine.register_user(alice)
    engine.register_user(bob)

    return engine

engine = load_engine()

# ---------------------------
# SIDEBAR
# ---------------------------

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "Product Catalog",
        "Search Products",
        "Recommendations",
        "Product Similarity",
        "Analytics",
        "User Profiles"
    ]
)

# ---------------------------
# DASHBOARD
# ---------------------------

if menu == "Dashboard":

    st.title("🛒 E-Commerce Recommendation Engine")

    col1,col2,col3,col4 = st.columns(4)

    products_count = len(list(engine.products.keys()))
    users_count = len(list(engine.users.keys()))

    categories = set()

    prices = []

    for pid in engine.products.keys():

        p = engine.products.get(pid)

        categories.add(p.category)
        prices.append(p.price)

    col1.metric("Products", products_count)
    col2.metric("Users", users_count)
    col3.metric("Categories", len(categories))
    col4.metric("Average Price", round(sum(prices)/len(prices),2))

    st.success(
        "DSA Concepts: HashMap • Trie • Heap • Similarity Algorithms"
    )

# ---------------------------
# PRODUCT CATALOG
# ---------------------------

elif menu == "Product Catalog":

    st.title("📦 Product Catalog")

    data = []

    for pid in engine.products.keys():

        p = engine.products.get(pid)

        data.append(
            [
                p.product_id,
                p.title,
                p.category,
                p.price
            ]
        )

    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "Title",
            "Category",
            "Price"
        ]
    )

    st.dataframe(df, use_container_width=True)

# ---------------------------
# SEARCH
# ---------------------------

elif menu == "Search Products":

    st.title("🔍 Trie Search")

    query = st.text_input(
        "Search Product or Category"
    )

    if query:

        results = engine.search_trie.get_suggestions(query)

        if results:

            for pid in results:

                p = engine.products.get(pid)

                st.write(
                    f"✅ {p.title} | {p.category}"
                )

        else:
            st.warning("No matches found")

# ---------------------------
# RECOMMENDATIONS
# ---------------------------

elif menu == "Recommendations":

    st.title("🎯 Personalized Recommendations")

    user_id = st.selectbox(
        "Select User",
        list(engine.users.keys())
    )

    if st.button("Generate Recommendations"):

        recs = engine.get_personalized_recommendations(
            user_id,
            5
        )

        names = []
        scores = []

        for score, product in recs:

            names.append(product.title)
            scores.append(score)

            st.write(
                f"⭐ {product.title} "
                f"(Score {round(score,2)})"
            )

        fig = plt.figure(figsize=(8,4))
        plt.bar(names, scores)
        plt.xticks(rotation=45)

        st.pyplot(fig)

# ---------------------------
# SIMILARITY
# ---------------------------

elif menu == "Product Similarity":

    st.title("⚡ Product Similarity")

    products = list(engine.products.keys())

    p1 = st.selectbox(
        "Product A",
        products
    )

    p2 = st.selectbox(
        "Product B",
        products,
        index=1
    )

    if st.button("Compare"):

        score = engine.compute_item_similarity(
            p1,
            p2
        )

        st.metric(
            "Similarity Score",
            round(score,4)
        )

# ---------------------------
# ANALYTICS
# ---------------------------

elif menu == "Analytics":

    st.title("📈 Analytics")

    categories = {}

    for pid in engine.products.keys():

        p = engine.products.get(pid)

        categories[p.category] = \
            categories.get(p.category,0)+1

    fig = plt.figure(figsize=(6,4))

    plt.pie(
        categories.values(),
        labels=categories.keys(),
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

# ---------------------------
# USER PROFILES
# ---------------------------

elif menu == "User Profiles":

    st.title("👤 User Profiles")

    uid = st.selectbox(
        "Select User",
        list(engine.users.keys())
    )

    user = engine.users.get(uid)

    st.subheader(user.name)

    st.write("### Ratings")
    st.json(user.ratings)

    st.write("### Search History")
    st.write(user.search_history)

    st.write("### Cart Items")
    st.write(user.cart_items)