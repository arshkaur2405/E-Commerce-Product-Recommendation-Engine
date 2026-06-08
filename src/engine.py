import heapq

from src.data_structures import CustomHashMap
from src.data_structures import Trie
from src.similarity import SimilarityMetrics


class RecommendationEngine:

    def __init__(self):

        self.products = CustomHashMap()
        self.users = CustomHashMap()
        self.search_trie = Trie()

    def register_product(self, product):

        self.products.put(product.product_id, product)

        self.search_trie.insert(
            product.title,
            product.product_id
        )

        self.search_trie.insert(
            product.category,
            product.product_id
        )

    def register_user(self, user):

        self.users.put(
            user.user_id,
            user
        )

    def compute_item_similarity(
        self,
        product_a,
        product_b
    ):

        p1 = self.products.get(product_a)
        p2 = self.products.get(product_b)

        vector1 = [
            len(p1.title),
            p1.price
        ]

        vector2 = [
            len(p2.title),
            p2.price
        ]

        return SimilarityMetrics.cosine_similarity(
            vector1,
            vector2
        )

    def get_personalized_recommendations(
        self,
        user_id,
        k=5
    ):

        user = self.users.get(user_id)

        interested_categories = set()

        for pid in user.ratings.keys():

            product = self.products.get(pid)

            if product:
                interested_categories.add(
                    product.category
                )

        for pid in user.cart_items:

            product = self.products.get(pid)

            if product:
                interested_categories.add(
                    product.category
                )

        scores = {}

        for pid in self.products.keys():

            product = self.products.get(pid)

            if pid in user.ratings:
                continue

            score = 0

            if product.category in interested_categories:
                score += 50

            score += product.price / 100

            scores[pid] = score

        heap = []

        for pid, score in scores.items():

            heapq.heappush(
                heap,
                (-score, pid)
            )

        recommendations = []

        while heap and len(recommendations) < k:

            score, pid = heapq.heappop(heap)

            recommendations.append(
                (
                    -score,
                    self.products.get(pid)
                )
            )

        return recommendations