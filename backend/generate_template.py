import sys
from jinja2 import Template

from app import models

MODEL_MODULE_PATH = "app.models"

if __name__ == "__main__":
    mod_name = sys.argv[1]
    if mod_name not in dir(models):
        print("Model not found")
        sys.exit(1)

    data = {
        "model_name": mod_name,
    }

    with open("templates/crud_template.py.jinja2") as f:
        template = Template(f.read())
        print(template.render(**data))
