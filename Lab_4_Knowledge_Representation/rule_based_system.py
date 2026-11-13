def diagnose_plant(problem):
    if problem.get("leaf_color") == "yellow" and problem.get("leaf_spots") == "yes":
        return "Possible fungal infection. Use fungicide and remove infected leaves."
    if problem.get("stem_wilt") == "yes" and problem.get("soil_moist") == "wet":
        return "Possible root rot. Improve drainage and reduce watering."
    if problem.get("leaf_color") == "brown" and problem.get("dry_soil") == "yes":
        return "Possible water stress. Water the plant and monitor soil moisture."
    return "No clear diagnosis. Check the plant closely or consult an expert."


print("Plant Health Diagnostic System")
print("=" * 35)

sample = {
    "leaf_color": "yellow",
    "leaf_spots": "yes",
    "stem_wilt": "no",
    "soil_moist": "dry",
    "dry_soil": "no"
}

print(diagnose_plant(sample))
