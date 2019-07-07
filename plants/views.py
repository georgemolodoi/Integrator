from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage

from django.views.decorators.csrf import csrf_exempt

from io import BytesIO
import aiohttp, asyncio

from fastai import *
from fastai.vision import *


PATH = Path(__file__).parent
EXPORT_FILE_URL = 'https://drive.google.com/uc?export=download&id=1bw0sCVQSSeROfB02yHYLimsd6VdX5UNI'
EXPORT_FILE_NAME = 'plants_model.pkl'

CLASSES = ['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Blueberry___healthy',
 'Cherry_(including_sour)___Powdery_mildew',
 'Cherry_(including_sour)___healthy',
 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn_(maize)___Common_rust_',
 'Corn_(maize)___Northern_Leaf_Blight',
 'Corn_(maize)___healthy',
 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)',
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange___Haunglongbing_(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,_bell___Bacterial_spot',
 'Pepper,_bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']

async def download_file(url, dest):
    if dest.exists(): return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(dest, 'wb') as f: f.write(data)

async def setup_learner():
    download_file(EXPORT_FILE_URL, PATH/EXPORT_FILE_NAME)
    try:
        learn = load_learner(PATH, EXPORT_FILE_NAME)
        return learn
    except RuntimeError as e:
        if len(e.args) > 0 and 'CPU-only machine' in e.args[0]:
            print(e)
            message = "\n\n This model was trained using an old version of fastai and will not work in a CPU environment. Please update the fastai library.\n\n"
            raise RuntimeError(message)
        else:
            raise


try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

tasks = [asyncio.ensure_future(setup_learner())]
learn = loop.run_until_complete(asyncio.gather(*tasks))[0]
# loop.close()


def analyze(request):
    if request.method == 'POST':
        file_ = request.FILES['myfile']
        imgBytes =  file_.read()
        img = open_image(BytesIO(imgBytes))

        # Get the first 3 predictions 
        _,_, losses = learn.predict(img)
        predictions = sorted(zip(CLASSES, map(float, losses)), key=lambda p: p[1], reverse=True)[0:3]

        # Cleaning categories names
        names = [y for x in predictions for y in x if type(y) is str]
        cleanedNames = list(map(lambda s: str(s).replace("_", " "), names))

        # Get probabilities for predictions
        probs = [y for x in predictions for y in x if type(y) is float]
        goodProbs = [x*100 for x in probs]

        results = zip(cleanedNames, goodProbs)

        context = {'results': results}
        return render(request, 'plants/result.html', context)

    return render(request, 'plants/index.html')

