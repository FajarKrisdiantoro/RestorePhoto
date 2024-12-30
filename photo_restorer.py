from dotenv import load_dotenv # type: ignore
load_dotenv(".env.local")
import replicate # type: ignore

model = replicate.models.get("tencentarc/gfpgan")
version = model.versions.get("0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c")

def predict_image(filename):

    inputs = {
        "img": open(filename,"rb"),

        'version': "v1.4",

        'scale': 2,
    }

      # Menggunakan replicate.run untuk melakukan prediksi
    output = replicate.run(
        "tencentarc/gfpgan:0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c", 
        input=inputs
    )

    # Menyimpan output ke file
    with open("output.png", "wb") as file:
        file.write(output.read())

    print("Output has been saved to output.png")
    return output