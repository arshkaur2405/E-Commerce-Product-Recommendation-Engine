import os

from src.models import Product
from src.models import User
from src.engine import RecommendationEngine


def create_products():

    return [

        Product(
            "P01",
            "Apple MacBook Pro M3",
            "Electronics",
            1999
        ),

        Product(
            "P02",
            "Dell XPS 15",
            "Electronics",
            1799
        ),

        Product(
            "P03",
            "Sony Headphones",
            "Electronics",
            399
        ),

        Product(
            "P04",
            "Logitech Mouse",
            "Electronics",
            99
        ),

        Product(
            "P05",
            "Samsung Monitor",
            "Electronics",
            299
        ),

        Product(
            "P06",
            "CLRS Algorithms",
            "Books",
            79
        ),

        Product(
            "P07",
            "Clean Code",
            "Books",
            49
        ),

        Product(
            "P08",
            "Python Crash Course",
            "Books",
            59
        ),

        Product(
            "P09",
            "Ergonomic Chair",
            "Office",
            249
        ),

        Product(
            "P10",
            "Standing Desk",
            "Office",
            399
        ),

        Product(
            "P11",
            "Hydro Flask",
            "Fitness",
            39
        ),

        Product(
            "P12",
            "Resistance Bands",
            "Fitness",
            29
        )
    ]


def seed_users(engine):

    alice = User(
        "U01",
        "Alice"
    )

    alice.add_rating(
        "P01",
        5
    )

    alice.add_rating(
        "P04",
        4
    )

    alice.add_search(
        "Electronics"
    )

    alice.add_cart(
        "P03"
    )

    engine.register_user(alice)

    bob = User(
        "U02",
        "Bob"
    )

    bob.add_rating(
        "P06",
        5
    )

    bob.add_rating(
        "P07",
        4
    )

    bob.add_search(
        "Books"
    )

    bob.add_cart(
        "P08"
    )

    engine.register_user(bob)


def export_report(engine):

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    path = (
        "outputs/"
        "recommendation_report.txt"
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        for uid in engine.users.keys():

            user = engine.users.get(uid)

            f.write(
                f"\nUser: {user.name}\n"
            )

            recommendations = (
                engine.get_personalized_recommendations(
                    uid,
                    5
                )
            )

            for score, product in recommendations:

                f.write(
                    f"{product.title}"
                    f" -> "
                    f"{score}\n"
                )

    print(
        f"\nReport saved at: {path}"
    )


def main():

    engine = RecommendationEngine()

    products = create_products()

    for product in products:
        engine.register_product(product)

    seed_users(engine)

    while True:

        print("\n")
        print("=" * 50)
        print("E-Commerce Recommendation Engine")
        print("=" * 50)

        print("1. Show Products")
        print("2. Search Product")
        print("3. Recommendations")
        print("4. Generate Report")
        print("5. Exit")

        choice = input(
            "Enter choice: "
        )

        if choice == "1":

            for pid in engine.products.keys():

                print(
                    engine.products.get(pid)
                )

        elif choice == "2":

            prefix = input(
                "Search: "
            )

            result = (
                engine.search_trie
                .get_suggestions(prefix)
            )

            print(
                "\nMatching Products"
            )

            for pid in result:

                product = (
                    engine.products
                    .get(pid)
                )

                if product:
                    print(product)

        elif choice == "3":

            uid = input(
                "Enter User ID: "
            )

            recommendations = (
                engine
                .get_personalized_recommendations(
                    uid,
                    5
                )
            )

            print(
                "\nTop Recommendations"
            )

            rank = 1

            for score, product in recommendations:

                print(
                    f"{rank}. "
                    f"{product.title} "
                    f"(Score={score:.2f})"
                )

                rank += 1

        elif choice == "4":

            export_report(
                engine
            )

        elif choice == "5":

            print(
                "Goodbye!"
            )

            break

        else:

            print(
                "Invalid Choice"
            )


if __name__ == "__main__":
    main()
    # ...