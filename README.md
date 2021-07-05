# E2E Deep Learning: Serverless Image Classifier
The Jovian Data Science Capstone Project: Build an end-to-end deep learning model to classify real-world images using TensorFlow, TensorFlow Lite, Docker, and AWS Lambda with API Gateway.
- __Publication__: [Towards Data Science](https://diardano.medium.com/e2e-deep-learning-serverless-image-classification-d4351372c83e)
- __Author__: Diardano Raihan 
- __Email__: diardano@gmail.com
- __Social Media__: [LinkedIn](https://www.linkedin.com/in/diardanoraihan), [Medium](https://diardano.medium.com/)

## Project Summary
Imagine we need to deal with lots of real-world clothes images and your responsibility is to create an automated image classifier for an e-commerce company. As a result, the challenge is not only to build a robust deep learning model, but also to deploy it as a __serverless app__. We can combine the __AWS Lambda__ and __API Gateway__ for hosting this serverless APIs. 

In this project, we will learn together how to:
- __train a deep learning model__ to classify images using TensorFlow.
- __convert the model into a more size-efficient__ format using TensorFlow Lite.
- __deploy the model locally__ on our machine using Docker.
- __deploy the model as a REST API__ using AWS Lambda and API Gateway.


## Datasets
The dataset contains 3781 clothes images with the top 10 most popular categories, divided into the train, test, and validation sets. We can access the data [here](https://github.com/alexeygrigorev/clothing-dataset-small).
| Label | Dataset Size | Train Size | Test Size | Validation Size | 
|:-------:|:-------:|:-------------------:|:------------:|:----------:|
| `dress`       | 288       | 241                  | 15        | 32     |
| `hat`         | 149       | 123                  | 12        | 14     |
| `longsleeve`  | 576       | 455                  | 72        | 49       |
| `outwear`     | 246       | 184                  | 38        | 24       |
| `pants`       | 559       | 468                  | 42        | 49       |
| `shirt`       | 345       | 290                  | 26        | 29       |
| `shoes`       | 297       | 198                  | 73        | 26       |
| `shorts`      | 257       | 202                  | 30        | 25       |
| `skirt`       | 136       | 112                  | 12        | 12       |
| `t-shirt`     | 928       | 795                  | 52        | 81       |
| __TOTAL__     | 3781      | 3068                 | 372       | 341      |

The image samples from each class are shown below:
<img src="https://raw.githubusercontent.com/diardanoraihan/E2E_Deep_Learning/main/Visualization/training_10_classes_images.png" width="600">

## The Proposed Deep Learning Model
We will build a deep learning model using the transfer learning method and image augmentation to achieve a good performance and prevent overfitting. The pre-trained model we use is __InceptionV3__, but feel free to experiment with another model as well.
- Download the InceptionV3 local weight [here](https://storage.googleapis.com/mledu-datasets/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5).
- The sample result of an image being augmented is shown below.
<img src="https://raw.githubusercontent.com/diardanoraihan/E2E_Deep_Learning/main/Visualization/sample_image_augmented.png" width="600">
- Model training:
<img src="https://raw.githubusercontent.com/diardanoraihan/E2E_Deep_Learning/main/Visualization/best_model.png" width="800">
  - Classification accuracy on test dataset: 90.59%
  - Gap accuracy between test and training dataset: 3.04% (test acc > training acc)
  - Test loss: 0.273
  - Avoid overvitting: YES
- Test the Model:
<img src="https://raw.githubusercontent.com/diardanoraihan/E2E_Deep_Learning/main/Visualization/best_model_predictions.png" width="600">

## Model Conversion with TensorFlow Lite



## Model Deployment



### Deploy on Local Machine with Docker



### Deploy on AWS Lambda and API Gateway
