import importlib.util
import platform
import sys


def is_installed(package_name: str) -> bool:
    return importlib.util.find_spec(package_name) is not None


print("AI Environment Check")
print("=" * 30)
print(f"Operating System: {platform.system()} {platform.release()}")
print(f"Python Version: {sys.version}")
print(f"Python Executable: {sys.executable}")

packages = ["numpy", "pandas", "matplotlib", "sklearn", "torch", "tensorflow"]
print("\nLibrary Status:")
for package in packages:
    status = "Installed" if is_installed(package) else "Not Installed"
    print(f"- {package}: {status}")

print("\nEnvironment is ready for AI/ML experiments.")
