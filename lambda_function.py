# in AWS Lambda, we need to use this import below
import tflite_runtime.interpreter as tflite
import numpy as np
from urllib.request import urlopen
from PIL import Image

# Create an interpreter interface for any model in TFLite
interpreter = tflite.Interpreter(model_path='Models/clothing_classifier.tflite')
interpreter.allocate_tensors()

# Get a list of input details from the model
input_details = interpreter.get_input_details()
input_index = input_details[0]['index']

# Get a list of output details from the model
output_details = interpreter.get_output_details()
output_index = output_details[0]['index']

def predict(X):
    # set the value of the input tensor
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()

    # Get the value of the output tensor
    preds = interpreter.get_tensor(output_index)
    
    return preds[0]

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

def decode_predictions(pred):
    result = {label: float(score) for label, score in zip(labels, pred)}
    return result

def preprocessor(img_url):
    # load the image using PIL module
    img = Image.open(urlopen(img_url))
    
    # Specify the image target size
    img = img.resize((150, 150))
    
    # Turn the image into a 4D-array
    X = np.expand_dims(img, axis =0)
    
    # Normalize the image
    X = X/255.0
    
    # Turn the image into a Numpy array with float32 data type
    X = X.astype('float32')
    
    return X

def lambda_handler(event, context):
    # Obtain the image location
    url = event['url']
    
    # Preprocess the image
    X = preprocessor(url)
    
    # Make prediction
    preds = predict(X)
    
    # Obtain the result
    results = decode_predictions(preds)
    return results