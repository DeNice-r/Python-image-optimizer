from PIL import Image
from os import mkdir, listdir, getcwd


print("Image optimizer/compressor.\nCurrently supported extensions are JPEG, JPG and PNG.")


params = {"quality": 65, "folder": "optimized_pictures", "path": getcwd()}
params_hints = {"quality": "Quaility: 0-100, more is better but heavier, closer to the original.\n" "Enter for default."
                           " Default is " + str(params["quality"]) + ": ",
                "folder": "Folder for output.\nEnter for default. Default is " + params['folder'] + ": ",
                "path": "Path: path to the pictures.\nEnter for default. Default is current working dir (" + getcwd() +
                        "): "}
for param in params.keys():
    inputs, error = "a", True
    while error is True:
        try:
            inputs = input(params_hints[param])
            if inputs != '':
                params[param] = inputs
        except ValueError:
            pass
        else:
            error = False

params["quality"] = int(params["quality"])
print("The parameters are:\n", params, sep='')

image_paths = [image_path for image_path in listdir(params["path"]) if image_path.endswith((".jpg", ".jpeg", ".png"))]

try:
    mkdir(params["path"] + "\\" + params["folder"])
except FileExistsError:
    print("Looks like the folder is present already.")


print("Compressing...")
tracker = 0
for path in image_paths:
    image = Image.open(path)
    image.save(params["path"] + "\\" + params["folder"] + "\\" + path, optimize=True, quality=params["quality"])
    tracker += 1
    print(round((tracker * 100) / len(image_paths), 2), '%', sep='')

print("Done. Thanks for using me!")
