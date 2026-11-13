import math


def entropy(labels):
    total = len(labels)
    if total == 0:
        return 0
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    value = 0.0
    for count in counts.values():
        probability = count / total
        value -= probability * math.log2(probability)
    return value


def information_gain(data, feature_index, target_index):
    total_entropy = entropy([row[target_index] for row in data])
    values = {}
    for row in data:
        feature_value = row[feature_index]
        values.setdefault(feature_value, []).append(row)

    weighted_entropy = 0.0
    for feature_value, subset in values.items():
        subset_entropy = entropy([row[target_index] for row in subset])
        weighted_entropy += (len(subset) / len(data)) * subset_entropy

    return total_entropy - weighted_entropy


def choose_best_feature(data, features):
    target_index = len(features)
    best_feature = None
    best_gain = -1
    for index, feature in enumerate(features):
        gain = information_gain(data, index, target_index)
        if gain > best_gain:
            best_gain = gain
            best_feature = feature
    return best_feature


dataset = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rainy", "Mild", "High", "Weak", "Yes"],
    ["Rainy", "Cool", "Normal", "Weak", "Yes"],
    ["Rainy", "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny", "Mild", "High", "Weak", "No"],
    ["Sunny", "Cool", "Normal", "Weak", "Yes"],
    ["Rainy", "Mild", "Normal", "Weak", "Yes"],
    ["Sunny", "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High", "Strong", "Yes"],
    ["Overcast", "Hot", "Normal", "Weak", "Yes"],
    ["Rainy", "Mild", "High", "Strong", "No"],
]

feature_names = ["Outlook", "Temperature", "Humidity", "Wind", "Play Tennis"]
print("Feature names:", feature_names)
print("Best feature for split:", choose_best_feature(dataset, feature_names[:-1]))
print("Entropy of labels:", entropy([row[-1] for row in dataset]))
