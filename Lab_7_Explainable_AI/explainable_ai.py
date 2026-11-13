def explain_features(feature_values, weights):
    contributions = {}
    for feature, value in feature_values.items():
        contributions[feature] = value * weights[feature]
    return dict(sorted(contributions.items(), key=lambda item: abs(item[1]), reverse=True))

feature_values = {
    'age': 35,
    'income': 68000,
    'education_years': 12,
    'credit_score': 750
}

weights = {
    'age': 0.02,
    'income': 0.0004,
    'education_years': 0.8,
    'credit_score': 0.1
}

contributions = explain_features(feature_values, weights)
print("Feature contributions to the prediction:")
for feature, contribution in contributions.items():
    print(f"- {feature}: {contribution:.3f}")

print("\nInterpretation:")
print("The most important feature in this toy model is the one with the largest absolute contribution.")
print("This is a simple example of explainability using model weights.")
