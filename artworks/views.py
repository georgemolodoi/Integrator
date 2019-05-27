from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage

from django.views.decorators.csrf import csrf_exempt

from io import BytesIO
import aiohttp, asyncio

from fastai import *
from fastai.vision import *


PATH = Path(__file__).parent
EXPORT_FILE_URL = 'https://drive.google.com/uc?authuser=0&id=1ywlgxYo2u0txYF-s3PjI3_OovZfQONWv&export=download'
EXPORT_FILE_NAME = 'arts_model.pkl'

CLASSES = ['Albrecht_Dürer',
 'Alfred_Sisley',
 'Amedeo_Modigliani',
 'Andrei_Rublev',
 'Andy_Warhol',
 'Camille_Pissarro',
 'Caravaggio',
 'Claude_Monet',
 'Diego_Rivera',
 'Diego_Velazquez',
 'Edgar_Degas',
 'Edouard_Manet',
 'Edvard_Munch',
 'El_Greco',
 'Eugene_Delacroix',
 'Francisco_Goya',
 'Frida_Kahlo',
 'Georges_Seurat',
 'Giotto_di_Bondone',
 'Gustav_Klimt',
 'Gustave_Courbet',
 'Henri_Matisse',
 'Henri_Rousseau',
 'Henri_de_Toulouse-Lautrec',
 'Hieronymus_Bosch',
 'Jackson_Pollock',
 'Jan_van_Eyck',
 'Joan_Miro',
 'Kazimir_Malevich',
 'Leonardo_da_Vinci',
 'Marc_Chagall',
 'Michelangelo',
 'Mikhail_Vrubel',
 'Pablo_Picasso',
 'Paul_Cezanne',
 'Paul_Gauguin',
 'Paul_Klee',
 'Peter_Paul_Rubens',
 'Pierre-Auguste_Renoir',
 'Piet_Mondrian',
 'Pieter_Bruegel',
 'Raphael',
 'Rembrandt',
 'Rene_Magritte',
 'Salvador_Dali',
 'Sandro_Botticelli',
 'Titian',
 'Vasiliy_Kandinskiy',
 'Vincent_van_Gogh',
 'William_Turner']

async def download_file(url, dest):
    if dest.exists(): return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(dest, 'wb') as f: f.write(data)

async def setup_learner():
    await download_file(EXPORT_FILE_URL, PATH/EXPORT_FILE_NAME)
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
loop.close()


# async def analyze(request):
#     if request.method == 'POST':
#         file_ = await request.FILES['input-file']
#         imgBytes = await file_.read()
#         img = open_image(BytesIO(imgBytes))

#         # Get the first 3 predictions 
#         _,_, losses = learn.predict(img)
#         predictions = sorted(zip(CLASSES, map(float, losses)), key=lambda p: p[1], reverse=True)[0:3]

#         # Cleaning categories names
#         names = [y for x in predictions for y in x if type(y) is str]
#         cleanedNeams = list(map(lambda s: str(s).replace("_", " "), names))

#         # Get probabilities for predictions
#         probs = [y for x in predictions for y in x if type(y) is float]

#         context = zip(cleanedNeams, probs)
#         print(context)

#         return render(request, 'artworks/result.html', context)


def index(request):
    if request.method == 'POST':
        print('Yellow')
        file_ = request.FILES['myfile']
        imgBytes =  file_.read()
        img = open_image(BytesIO(imgBytes))

        # Get the first 3 predictions 
        _,_, losses = learn.predict(img)
        predictions = sorted(zip(CLASSES, map(float, losses)), key=lambda p: p[1], reverse=True)[0:3]

        # Cleaning categories names
        names = [y for x in predictions for y in x if type(y) is str]
        cleanedNeams = list(map(lambda s: str(s).replace("_", " "), names))

        # Get probabilities for predictions
        probs = [y for x in predictions for y in x if type(y) is float]
        goodProbs = [x*100 for x in probs]
        
        results = zip(cleanedNeams, goodProbs)
        
        print(goodProbs)

        context = {'results': results}
        return render(request, 'artworks/result.html', context)
    print('No')
    return render(request, 'artworks/index.html')


