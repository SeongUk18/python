class FeatureA:
    def feature_a(self):
        print("Feature A")


class FeatureB:
    def feature_b(self):
        print("Feature B")


class CombinedClass(FeatureA, FeatureB):
    pass


combined = CombinedClass()
combined.feature_a()  # "Feature A" 출력
combined.feature_b()  # "Feature B" 출력
