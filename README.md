# Deep Learning with Dobble

Welcome to **Deep Learning with Dobble**! This README aims to provide the bare minimum of documentation necessary to successfully execute the notebook *deep-learning-with-dobble.ipynb* on your local machine.

## Getting Started

Follow these steps to clone the repository and run the project on your local machine.

### Prerequisites

- Python 3.11 or higher installed on your machine.
- Operating system: Unix/macOS

### Clone the Repository

1. Open a terminal or command prompt on your local machine.

2. Clone the repository using `git`:

```
git clone https://github.com/mrvnthss/deep-learning-with-dobble
cd deep-learning-with-dobble
```

### Setting up a Virtual Environment (Optional but Recommended)

Before you begin, make sure that `pip` is installed on your system. `pip` is a package manager for Python, and it's usually included by default when you install Python. To ensure that `pip` is installed, run the following command:

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
python3 -m venv env
source env/bin/activate
```

The second argument of the first command (`env`) is the location to create the virtual environment. You can change this to something you prefer.

### Install dependencies

Install the required Python packages specified in the `requirements.txt` file by running:

```
python3 -m pip install -r requirements.txt
```

## Starting JupyterLab

To start **JupyterLab**, simply run the following command inside your activated virtual environment:

```
juypter lab
```

All you have to do now is navigate to the `notebooks/` directory and open the `deep-learning-with-dobble.ipynb` notebook. The notebook can be run from top to bottom in a single go. All paths are set relative to the notebook's directory and all of the necessary data is already included in the repository that you cloned. The only thing that's not included in the repository right away is PyTorch checkpoints since these files are too large to be hosted on GitHub. Instead, these files are downloaded at the very beginning of the notebook and moved into the appropriate subdirectories. All of this happens automatically, without you having to do anything.

At the end of the notebook, we have commented out the commands to train the different models so that the notebook executes quickly. Of course, these commands can be executed by you at any time by simply uncommenting them and re-running the respective cells of the notebook.

## License

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) (GPLv3) - see the [LICENSE](LICENSE) file for details.

You are free to:

- **Share**: Copy and redistribute the material in any medium or format.
- **Adapt**: Remix, transform, and build upon the material for any purpose, even commercially.

Under the following terms:

- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **ShareAlike**: If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
- **No additional restrictions**: You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.
