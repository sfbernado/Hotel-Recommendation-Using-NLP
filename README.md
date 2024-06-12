# Hotel-Recommendation-Using-NLP

## Overview

This project is a hotel recommendation system that uses Natural Language Processing (NLP) to analyze hotel locations and amenities and recommend hotels based on customer preferences. The system uses a dataset of hotel features and scores to predict the best hotel rating based on customer preferences.

## Features

- Data Acquisition: The dataset is acquired from the [Hotel Recommendation System](https://www.kaggle.com/datasets/jiashenliu/515k-hotel-reviews-data-in-europe) dataset on Kaggle.
- Data Preprocessing: The dataset is cleaned and preprocessed to remove irrelevant data, missing values, duplicated data, several string operations, and implement several NLP techniques such as tokenization, stop word removal, and lemmatization to clean and prepare the text data.
- Recommendation System: The recommendation system is based on collaborative filtering and NLP. It calculates the similarity between user preferences and hotel amenities to generates hotel recommendations.

## Prerequisites

- Python 3.x
- Jupyter Notebook
- Pandas
- NumPy
- NLTK
- Kaggle API (optional)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sfbernado/Hotel-Recommendation-Using-NLP.git
cd Hotel-Recommendation-Using-NLP
```

2. Install the required packages:
```bash
pip install numpy pandas nltk
```

or

```bash
pip install -r requirements.txt
```

3. Setup Kaggle API (optional):
```bash
pip install kaggle
export KAGGLE_CONFIG_DIR=/path/to/kaggle.json
```

4. Run the Jupyter Notebook:
```bash
jupyter notebook Hotel-Recommendation-Using-NLP.ipynb
```

5. Run the notebook cells sequentially

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Hotel Recommendation System](https://www.kaggle.com/datasets/jiashenliu/515k-hotel-reviews-data-in-europe) dataset on Kaggle
- [Pandas](https://pandas.pydata.org/) library
- [NumPy](https://numpy.org/) library
- [Natural Language Toolkit (NLTK)](https://www.nltk.org/) library

## Author

Stanislaus Frans Bernado

[![Gmail Badge](https://img.shields.io/badge/-stanislausfb@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:stanislausfb@gmail.com "Connect via Email")
[![Linkedin Badge](https://img.shields.io/badge/-Stanislaus%20Frans%20Bernado-0072b1?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/stanislausfb/ "Connect on LinkedIn")
