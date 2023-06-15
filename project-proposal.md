# 1. Introduction
Our proposed project aims to develop a deep learning model capable of playing the Dobble Game by accurately recognizing and identifying the unique symbol shared by two different cards. We intend to create a flexible codebase using PyTorch to generate our dataset that replicates the cards in a Dobble deck. This codebase will allow for parameterization of various attributes such as the number of symbols on a single card, size and color of the symbols, and the type of symbols (e.g., real-world objects, simple geometric shapes etc.). Additionally, we aim to include affine transformations in our dataset generation to mimic different viewing angles that humans would experience when actually playing the game.

# 2. Objectives
Our project objectives are as follows:
* Develop a codebase using PyTorch to generate a dataset that mirrors the cards in a Dobble deck. The codebase should allow for maximum flexibility in creating different datasets. Among other image augmentation techniques, affine transformations will be included to mimic different viewing angles.
* Preprocess and augment the dataset to enhance model performance and generalization from training to testing. This includes resizing the images to 224 x 224 pixels to ensure compatibility with many readily available architectures.
* Design and implement our own custom deep learning model architecture using PyTorch.
* Train and evaluate the model to achieve high accuracy in identifying the common symbol between two cards.
* Explore additional features to broaden the project scope, such as investigating multiple model architectures, hyperparameter tuning, etc.
* Fun idea: Look into the potential for developing an application that is able to play the Dobble game (i.e., users can take images of Dobble cards from inside the app and the app then returns the symbol common to the two cards in the picture).

# 3. Methodology
## a. Dataset Generation
We will develop a flexible codebase using PyTorch to generate a dataset representing Dobble cards. This codebase will allow for customization of various card attributes, including the number of symbols, size of symbols, color of symbols, and the type of symbols on each card. Additionally, we will incorporate affine transformations to simulate different viewing angles, ensuring the dataset captures the variations encountered during actual gameplay.

## b. Dataset Preprocessing and Augmentation
To improve model performance and generalization, we will preprocess the dataset by normalizing the images and resizing them to 224 x 224 pixels. Resizing to this standard size will enable compatibility with most deep learning architectures. Furthermore, we will apply suitable image augmentation techniques, such as rotation, flipping, and affine transformations, to augment the dataset and increase its diversity. Random cropping will most likely not be incorporated as it is crucial for our model to "see" the full card in order to learn to play the game.

## c. Model Architecture Design
Using PyTorch, we will design and implement a custom deep learning model architecture. We will experiment with various architectural choices that we have already encountered in our course, such as convolutional layers, pooling layers, and fully connected layers, to develop an effective model that can accurately identify the common symbol between two cards.

## d. Model Training and Evaluation
The model will be trained using a training set and validated using a validation set. We will implement appropriate loss functions, optimization algorithms, and regularization techniques in PyTorch. The model's performance will be evaluated on the testing set, measuring accuracy and other relevant metrics.

## e. Extending the Project
To extend the project's scope, we could consider exploring the following ideas:
* Multiple Model Architectures: We could compare and contrast different model architectures, experimenting with various combinations of layers, depths, and parameters using PyTorch. This exploration could provide insights into the performance and capabilities of different models for symbol recognition.
* Hyperparameter Tuning: Techniques like grid search, random search, or other optimization methods could be employed to tune hyperparameters such as learning rate, batch size, and regularization strength. This would potentially allow us to fine-tune our models for optimal performance.
* Image Augmentation: In addition to the mentioned techniques, we could explore additional suitable image augmentation methods, such as adding noise, to further enhance model generalization and robustness.

# 4. Milestones
The first part of our project will be divided into the following milestones:
* Milestone 1: Dataset Generation
* Milestone 2: Dataset Preprocessing and Augmentation
* Milestone 3: Model Architecture Design and Implementation
* Milestone 4: Model Training and Evaluation

Once we have achieved these milestones and have managed to build a network that is capable of playing Dobble, we will decide how best to continue.

# 5. Expected Outcomes
Upon the successful completion of this first part of the project, we anticipate the following outcomes:
* A flexible codebase using PyTorch for dataset generation, allowing customization of various card attributes such as the number of symbols, size of symbols, color of symbols, and the type of symbols.
* One or more preprocessed dataset(s) with images resized to 224 x 224 pixels, ensuring compatibility with most deep learning architectures.
* One or more custom deep learning model architecture(s) implemented in PyTorch that achieve(s) high accuracy in symbol recognition between two cards.