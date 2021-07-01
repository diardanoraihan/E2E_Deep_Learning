import requests
import numpy as np

labels = [
    'dress',
    'hat',
    'longsleeve',
    'outwear',
    'pants',
    'shirt',
    'shoes',
    'short',
    'skirt',
    't-shirt'
]

data = {
    "url": "http://bit.ly/mlbookcamp-pants"
}

url ="http://localhost:8080/2015-03-31/functions/function/invocations"

results = requests.post(url, json=data).json()

print('[PREDICTION RESULT]')
print('+-------------------------------------------+')
score = []
for cat in results:
	print('+ {}: {}'.format(cat, results[cat]))
	score.append(results[cat])

best_cat = np.argmax(score)
print('+-------------------------------------------+')
print('Therefore, the model predicts the input image as {}'.format(labels[best_cat].upper()))
print()