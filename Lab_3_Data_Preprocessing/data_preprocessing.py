rows = [
    {"age": 25, "income": 50000, "gender": "Male", "label": "Yes"},
    {"age": 30, "income": 60000, "gender": "Female", "label": "Yes"},
    {"age": None, "income": 55000, "gender": "Male", "label": "No"},
    {"age": 40, "income": 80000, "gender": "Female", "label": "Yes"},
    {"age": 35, "income": None, "gender": "Male", "label": "No"},
    {"age": 25, "income": 50000, "gender": "Male", "label": "Yes"},
]


def fill_missing(rows, column, default_value):
    for row in rows:
        if row.get(column) is None:
            row[column] = default_value
    return rows


def remove_duplicates(rows):
    seen = set()
    unique_rows = []
    for row in rows:
        normalized_row = tuple(sorted((key, str(value)) for key, value in row.items()))
        if normalized_row not in seen:
            seen.add(normalized_row)
            unique_rows.append(row)
    return unique_rows


def normalize_numeric(rows, column):
    values = [row[column] for row in rows if row.get(column) is not None]
    if not values:
        return rows

    min_value = min(values)
    max_value = max(values)
    if max_value == min_value:
        return rows

    for row in rows:
        if row.get(column) is not None:
            row[column] = (row[column] - min_value) / (max_value - min_value)
    return rows


def one_hot_encode(rows, column):
    categories = sorted({row[column] for row in rows if row.get(column) is not None})
    encoded_rows = []
    for row in rows:
        encoded = dict(row)
        for category in categories:
            encoded[f"{column}_{category}"] = 1 if row.get(column) == category else 0
        encoded.pop(column, None)
        encoded_rows.append(encoded)
    return encoded_rows


if __name__ == "__main__":
    print("Original data:")
    for row in rows:
        print(row)

    rows = fill_missing(rows, "age", 30)
    rows = fill_missing(rows, "income", 60000)
    rows = remove_duplicates(rows)
    rows = normalize_numeric(rows, "age")
    rows = normalize_numeric(rows, "income")
    rows = one_hot_encode(rows, "gender")

    print("\nProcessed data:")
    for row in rows:
        print(row)
