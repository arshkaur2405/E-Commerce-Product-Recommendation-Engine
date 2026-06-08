import math


class SimilarityMetrics:

    @staticmethod
    def cosine_similarity(v1, v2):

        dot = sum(a*b for a, b in zip(v1, v2))

        mag1 = math.sqrt(sum(x*x for x in v1))
        mag2 = math.sqrt(sum(x*x for x in v2))

        if mag1 == 0 or mag2 == 0:
            return 0

        return dot / (mag1 * mag2)

    @staticmethod
    def calculate_jaccard(set1, set2):

        union = len(set1.union(set2))

        if union == 0:
            return 0

        intersection = len(set1.intersection(set2))

        return intersection / union
    # ...