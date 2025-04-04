# Deep Learning with Dobble <a href="https://github.com/mrvnthss/deep-learning-with-dobble"><img src="https://github.com/mrvnthss/deep-learning-with-dobble/blob/main/data/processed/classic-dobble/classic-dobble_021.png?raw=true" align="right" height="100"/></a>

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrvnthss/deep-learning-with-dobble/blob/main/deep-learning-with-dobble.ipynb)
[![Jupyter](https://img.shields.io/badge/Jupyter-Lab-F37626.svg?style=flat&logo=Jupyter)](https://jupyterlab.readthedocs.io/en/stable)
[![Python](https://img.shields.io/badge/Python-3.11_|_3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch_2.2.1-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/get-started/locally/)
[![GitHub License](https://img.shields.io/github/license/mrvnthss/deep-learning-with-dobble?color=ad2317)](https://www.gnu.org/licenses/gpl-3.0.html.en)

Welcome to **Deep Learning with Dobble**! This repository contains the results of a graded project that formed part of the **Deep Learning** seminar taught at [**Justus Liebig University Giessen**](https://www.uni-giessen.de/) in Spring 2023.

**Note**: The official project deadline was July 23, 2023. I have continued to work on this repository after the project was officially submitted. If you wish to browse the repository at the project deadline, click [here](https://github.com/mrvnthss/deep-learning-with-dobble/tree/b2d3f37fc3922c41284bc09b53fedb4b5aa2e5dd).

## Table of Contents

- [The Card Game *Dobble*](#the-card-game-dobble)
- [Generating *Dobble* Decks](#generating-dobble-decks)
- [A Deep Learning Pipeline](#a-deep-learning-pipeline)
- [Comparing ResNet Models](#comparing-resnet-models)
- [Getting Started](#getting-started)
- [Languages & Tools](#languages-and-tools)
- [References](#references)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## The Card Game Dobble

[*Dobble*](https://www.dobblegame.com) is a popular card game that challenges players to spot matching symbols between pairs of cards. While there are different modes of play, the basic idea of the game remains the same: Every two cards in a deck of playing cards have exactly one symbol in common, and players must identify that unique symbol as quickly as possible. A classic *Dobble* deck consists of 55 playing cards, with 8 different symbols placed on each card. The constraint that any two cards share one and only one symbol gives rise to a rich mathematical structure known as finite projective planes. There are several well-written articles on the web about this topic, some of which I have listed in the [References](#references) section of this README.

<div align="center">
    <img src="https://github.com/mrvnthss/deep-learning-with-dobble/blob/main/reports/other/dobble-brettspiel-empfehlungen.jpg?raw=true" alt="card-game-dobble" width="700">
    <p>A set of <em>Dobble</em> cards.  <a href="https://brettspiel-empfehlungen.de">&copy Brettspiel Empfehlungen</a>. Used with permission.</p>
</div>

The goal of this project when Nina (a fellow student) and I started working on it was twofold:

1. Implement an algorithm that can generate custom *Dobble* decks based on a set of open-source emojis that serve as symbols on the cards.
1. Set up a deep learning pipeline to train, validate, and test arbitrary model architectures with the goal of teaching those models to play *Dobble*.

In this README, I will walk you through the indidvidual steps we took to achieve these goals. If you're interested in running the Jupyter notebooks on your local machine, check out the [Getting Started](#getting-started) section.

## Generating Dobble Decks

In order to create our own *Dobble* decks, we would need to go through the following steps:

1. Find open source emojis to use as symbols on the playing cards.

1. Develop an algorithm that takes an arbitrary number of emojis and places them on a white disk on top of a transparent background to resemble a single playing card. In doing so, we need to make sure that no two emojis overlap. Ideally, the way we place the emojis on the white disk will resemble the way the symbols are arranged on actual *Dobble* playing cards.

1. Develop an algorithm that determines which emojis to place on which card to satisfy the constraint that every two playing cards have exactly one emoji in common.

The emojis used for this project are taken from [OpenMoji](https://openmoji.org) - the open-source emoji and icon project. Here are the reasons for choosing OpenMoji:

- The emojis are open source and published under the [Creative Commons Share Alike License 4.0](https://creativecommons.org/licenses/by-sa/4.0/#).

- There are over 4,000 emojis to choose from!

- All emojis follow a common [styleguide](https://openmoji.org/styleguide/#styleguide). Most importantly, all emojis use the same primary and secondary [colors](https://openmoji.org/styleguide/#color). This is crucial for resembling the original *Dobble* playing cards, as the symbols on those cards also use only a finite set of colors (i.e., a single shade of green, a single shade of yellow, and so on).

Here are the emojis we have chosen to resemble the original *Dobble* symbols as close as possible:

<div align="center">
    <img src="https://github.com/mrvnthss/deep-learning-with-dobble/blob/main/reports/figures/emojis/classic-dobble-emojis.png?raw=true" alt="classic-dobble-emojis" width="600">
    <p>The emojis from <a href="https://openmoji.org">OpenMoji</a> used to create our own deck of <em>Dobble</em> playing cards.</p>
</div>

Next, we had to implement a logic that would place the selected emojis on our virtual playing cards in such a way that ...

- the available space on each card would be utilized as much as possible,

- no two emojis would overlap,

- the arrangement of emojis on our virtual playing cards would resemble the appearance of actual *Dobble* cards.

To solve this task, we used results from the mathematical theory of *circle packing*. Circle packing involves arranging circles in a confined space so that they touch but don't overlap, aiming to fit as many circles as possible. The data we used for this project were taken from [Prof. Dr.-Ing. Eckehard Specht](https://www.ltv.ovgu.de/Mitarbeiter/Lehrstuhlinhaber/Prof_+Eckehard+Specht-p-210.html)'s website [packomania.com](http://www.packomania.com). A few selected circle packings for different numbers of circles are visualized below.

<div align="center">
    <img src="https://github.com/mrvnthss/deep-learning-with-dobble/blob/main/reports/figures/packings/packings-illustration.png?raw=true" alt="packings-illustration" width="600">
    <p>Different types of circle packings for different numbers of circles.</p>
</div>

Although all the square images of the emojis are the same size (in pixels), the emojis within them take up different amounts of space. In addition, some emojis extend far into the corners of the images, while others do not. To account for this, we have implemented a simple algorithm that automatically resizes each emoji to take up as much space as possible without extending outside the incircle of the square image. Below you can find an emoji that extended too far into the top right-hand corner, and consequently was downsized to correct for this.

<div align="center">
    <img src="https://github.com/mrvnthss/deep-learning-with-dobble/blob/main/reports/figures/emojis/downsized-emoji.png?raw=true" alt="downsized-emoji" width="400">
    <p>Emojis that extend into the corners are automatically downsized.</p>
</div>

The ice emoji, on the other hand, does not use nearly all of the space available in the square image, so it is automatically enlarged.

<div align="center">
    <img src="https://github.com/mrvnthss/deep-learning-with-dobble/blob/main/reports/figures/emojis/enlarged-emoji.png?raw=true" alt="downsized-emoji" width="400">
    <p>Emojis that are too small are automatically enlarged.</p>
</div>

Below you can see the full set of emojis, automatically resized to take up as much space as possible without extending outside the incircle of the square image.

<div align="center">
    <img src="https://github.com/mrvnthss/deep-learning-with-dobble/blob/main/reports/figures/emojis/resized-classic-dobble-emojis.png?raw=true" alt="resized-classic-dobble-emojis" width="600">
    <p>Resized emojis.</p>
</div>

With the emojis and their placement on the individual cards all figured out, we needed to implement an algorithm that would ultimately tell us which emoji to place on which card to create a valid deck of *Dobble* playing cards. Essentially, this comes down to computing the so-called *incidence matrix* of a finite projective plane of order $p^k$ for a prime number $p$. To read up on how this is done, I highly recommend [this article](https://mickydore.medium.com/the-dobble-algorithm-b9c9018afc52) by *Micky Dore*. Below is the full set of $57$ playing cards used in this project.

<div align="center">
    <img src="https://github.com/mrvnthss/deep-learning-with-dobble/blob/main/reports/figures/cards/classic-dobble-deck.png?raw=true" alt="classic-dobble-deck" width="600">
    <p>The full set of playing cards used in this project.</p>
</div>

## A Deep Learning Pipeline

At this point in the project, we were essentially able to create our own dataset to use for training purposes. The full dataset, created using our imitation of the classic *Dobble* deck, consisted of $(57 * 56) / 2 = 1596$ pairs of cards, which we divided into a training set, a validation set, and a test set (using a $70 / 15 / 15$ split). Thus, our training set essentially consisted of $1117$ pairs of images of playing cards. However, we did not feed these image pairs directly into the network. Instead, in order to increase the variability of our training set, we ...

- applied image augmentation techniques to both images of the individual playing cards,
- randomly positioned the two cards in two of the four quadrants of a randomly colored square background,
- and applied additional image augmentation techniques to this combined image of the two playing cards against a colored background.

The image augmentation techniques we chose were intended to mimic the conditions a human being would face when playing the game (e.g., varying lighting conditions, different viewing angles, etc.).

<div align="center">
    <img src="https://github.com/mrvnthss/deep-learning-with-dobble/blob/main/reports/figures/cards/image-augmentation.png?raw=true" alt="image-augmentation" width="600">
    <p>Using image augmentation to increase the variability of our dataset.</p>
</div>

All of this was implemented in our custom `DobbleDataset` dataset class. Finally, we had the data we needed to train our models. All that remained was to set up a deep learning pipeline. To do this, we coded our own training, validation, and testing routines. We made sure to regularly save checkpoints during training, and we performed a simple sanity check before starting the training routines by overfitting models on a single batch of training data. This allowed us to get rid of any major bugs in advance. Additionally, we implemented the [REX learning rate scheduler](#rex) based on the `LRScheduler` class available in `torch.optim.lr_scheduler`. The decy factor used in this schedule is illustrated below.

<div align="center">
    <img src="https://github.com/mrvnthss/deep-learning-with-dobble/blob/main/reports/figures/results/rex-schedule.png?raw=true" alt="rex-schedule" width="700">
    <p>The REX learning rate schedule.</p>
</div>

## Comparing ResNet Models

To cap things off, we compared the performance of ResNet models of different depths. In hindsight, this was not very enlightening, as the smallest ResNet model already solved the task with perfect accuracy (evaluated on a test set the network had never seen before). The results we observed are also not surprising: the larger models required more epochs of training to produce meaningful results, because more parameters had to be fine-tuned to solve the task. In fact, 300 epochs of training was not enough to achieve (near) perfect accuracy for the two largest ResNet models.

<div align="center">
    <img src="https://github.com/mrvnthss/deep-learning-with-dobble/blob/main/reports/figures/results/resnet-comparison.png?raw=true" alt="resnet-comparison" width="700">
    <p>Training results for ResNet models of different depths.</p>
</div>

## Getting Started

Follow these steps to clone the repository and run the project on your local machine.

### Prerequisites

- Python 3.11 or 3.12 installed on your machine.
- Operating system: Unix/macOS

### Clone the Repository

1. Open a terminal or command prompt on your local machine.

2. Clone the repository using `git`:

```
git clone https://github.com/mrvnthss/deep-learning-with-dobble
cd deep-learning-with-dobble
```

### Set up a Virtual Environment (Optional but Recommended)

Before you begin, make sure that `pip` is installed on your system. `pip` is a package manager for Python, and it's usually included by default when you install Python. To ensure that `pip` is installed, run the following commands:

```
python3 -m pip install --user --upgrade pip
python3 -m pip --version
```

Setting up a virtual environment helps isolate project dependencies. If you don't have `virtualenv` installed, you can install it using:

```
python3 -m pip install --user virtualenv
```

Create and activate a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

All the dependencies that are required to execute the notebooks in this repository are listed in the [requirements.txt](requirements.txt) file. Installing these is a breeze. Simply issue the following command after you have set up your virtual environment:

```
pip install -r requirements.txt
```

### Start JupyterLab

To start [JupyterLab](https://jupyter.org), simply run the following command inside your activated virtual environment:

```
juypter lab
```

That's it, you're good to go! Simply open one of the notebooks. The [deep-learning-with-dobble.ipynb](deep-learning-with-dobble.ipynb) notebook contains most of the project, so I'd recommend exploring that one first!

## Languages and Tools

<p align="left">
  <a href="https://jupyterlab.readthedocs.io/en/latest/" target="_blank" rel="noreferrer">
    <img src="https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg" alt="jupyter" width="40" height="40"/>
  </a>
  &nbsp;
  <a href="https://www.python.org" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
  </a>
  &nbsp;
  <a href="https://pytorch.org/" target="_blank" rel="noreferrer">
    <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/>
  </a>
  &nbsp;
  <a href="https://numpy.org" target="_blank" rel="noreferrer">
    <img src="https://github.com/numpy/numpy/blob/main/branding/logo/logomark/numpylogoicon.png?raw=true" alt="numpy" width="40" height="40"/>
  </a>
  &nbsp;
  <a href="https://opencv.org/" target="_blank" rel="noreferrer">
    <img src="https://www.vectorlogo.zone/logos/opencv/opencv-icon.svg" alt="opencv" width="40" height="40"/>
  </a>
  &nbsp;
  <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/>
  </a>
</p>

## References

- <a id='rex'></a> Chen, J., Wolfe, C., & Kyrillidis, A. (2022). REX: Revisiting budgeted training with an improved schedule. *Proceedings of Machine Learning and Systems, 4*, 64–76.

- Collingridge, P. (2018, September 13). *Dobble*. petercollingridge.co.uk. https://www.petercollingridge.co.uk/blog/mathematics-toys-and-games/dobble/

- Dore, M. (2021, December 30). The Dobble algorithm. *Medium*. https://mickydore.medium.com/the-dobble-algorithm-b9c9018afc52

- Dore, M. (2021, December 29). The maths behind Dobble. *Medium*. https://mickydore.medium.com/dobble-theory-and-implementation-ff21ddbb5318

- *Finite projective planes and the math of Spot It!* (2023, March 29). Puzzlewocky. https://puzzlewocky.com/games/the-math-of-spot-it/

## Acknowledgments

The emojis used in this project are designed by [**OpenMoji**](https://openmoji.org/) - the open-source emoji and icon project. License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/#)

The data on circle packings used in this project are made available by [**Prof. Dr.-Ing. Eckehard Specht**](https://www.ltv.ovgu.de/Mitarbeiter/Lehrstuhlinhaber/Prof_+Eckehard+Specht-p-210.html) on his website [**packomania.com**](http://www.packomania.com).

## License

This project is open source and available under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) (GPLv3). The GPLv3 is a copyleft license that allows for the free distribution, modification, and use of this software, ensuring that all derivatives of this work are also available under the same license. Here’s a summary of the license’s main points:

- **Freedom to Use**: You are free to use this software for any purpose, including commercial applications, in accordance with the license terms.

- **Freedom to Modify**: You can modify the source code of this software, allowing you to tailor it to your needs or improve upon it. Your modifications must also be licensed under GPLv3.

- **Freedom to Share**: You can distribute this software freely, whether in its original form or with your modifications, as long as you also make the source code available under the same license terms.

- **Share Alike**: If you distribute modified versions of this software, you must also do so under the GPLv3, ensuring that all derivatives remain free and open source under the same terms.

- **Attribution and Notices**: When distributing or modifying the project's software, you must retain all copyright notices and author attributions found in the original work, as well as provide notices that you have modified the work. This ensures transparency and respects the original creators' contributions.

- **No Additional Restrictions**: You may not impose any further restrictions on the recipients' exercise of the rights granted under the license. This includes not using legal terms or technological measures that legally restrict others from doing anything the license permits.

For more detailed information, please review the full [LICENSE](LICENSE) text. By using, distributing, or contributing to this project, you agree to abide by the terms of the GNU GPLv3.
