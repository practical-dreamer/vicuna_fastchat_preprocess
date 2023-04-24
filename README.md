# FastChat Conversation Converter

This repository contains a script to convert chat conversations from a JSON file to a text file, with formatting suitable for training a language model using the FastChat framework. The script relies on the [FastChat repository](https://github.com/lm-sys/FastChat) to preprocess and tokenize the conversations before writing them to the output file.

## Dependencies

- Python 3.6 or higher
- IJSON library
- FastChat repository (specifically, the `train.py` script located under the `fastchat/train/` directory)

## Installation

### 1. Setup Conda Environment (Optional but recommended)
```
conda create -n fastchat-conversation-converter python=3.10.9
conda activate fastchat-conversation-converter
```
### 2. Clone this repo and install dependencies
```
git clone https://github.com/practicaldreamer/fastchat-conversation-converter
cd fastchat-conversation-converter
pip install ijson
```
### 3. Clone FastChat Repo and install FastChat
```
mkdir repos
cd repos
git clone https://github.com/lm-sys/FastChat
cd FastChat
pip install -e .
cd ..
cd ..
```
## Usage

``` 
process_conversations.py \
--model_path '/home/user/Documents/models/llama-7b' \
--input_json_path '/home/user/Downloads/ShareGPT_V3_unfiltered_cleaned_split_no_imsorry.json' \
--output_txt_path '/home/user/Documents/output.txt'
```
Replace the arguments with the appropriate values for your use case.

## Credits
This script is built upon the [FastChat](https://github.com/lm-sys/FastChat) project. Please refer to the original repository for more information about the framework and its usage.
