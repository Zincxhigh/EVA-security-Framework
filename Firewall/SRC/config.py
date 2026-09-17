from pathlib import Path
import yaml

def load_yaml(filename="config.yaml"):
  path = Path(__file__).resolve().parent / filename

  if not path.exists():
    raise FileNotFoundError(f"Configuration file not found: {path}")

  with path.open("r", encoding="utf-8") as file:
    return yaml.safe_load(file)
