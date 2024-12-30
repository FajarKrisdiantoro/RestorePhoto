from dotenv import load_dotenv  # type: ignore
import replicate  # type: ignore
import os

load_dotenv(".env.local")

model = replicate.models.get("tencentarc/gfpgan")
version = model.versions.get("0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c")

def predict_image(filename):
    with open(filename, "rb") as img_file:
        inputs = {
            "img": img_file,
            "version": "v1.4",
            "scale": 2,
        }

        output = replicate.run(
            "tencentarc/gfpgan:0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c",
            input=inputs
        )

    return output  # URL hasil dari Replicate API
