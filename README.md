# FastChat Conversation Converter

This repository contains a script to convert chat conversations from a JSON file to a text file, with formatting suitable for training a language model using the FastChat framework. The script relies on the [FastChat repository](https://github.com/lm-sys/FastChat) to preprocess and tokenize the conversations before writing them to the output file.

## Dependencies

- Python 3.6 or higher
- Transformers library
- IJSON library
- FastChat repository (specifically, the `train.py` script located under the `fastchat/train/` directory)

## Installation

1. Clone this repository: `git clone https://github.com/practicaldreamer/fastchat-conversation-converter.git`
2. Install the required Python libraries: `pip install transformers ijson`
3. Clone the FastChat repository (if you haven't already): `git clone https://github.com/lm-sys/FastChat.git`

## Usage

1. Modify the script `conversation_converter.py` to include the correct paths for the FastChat `train.py` file and the input/output files.
2. Run the script:
`python conversation_converter.py \
  --model_path '/home/user/Documents/models/llama-7b' \
  --input_json_path '/path/to/input.json' \
  --output_txt_path '/path/to/output.txt'`
Replace the arguments with the appropriate values for your use case.

## Credits
This script is built upon the [FastChat](https://github.com/lm-sys/FastChat) project. Please refer to the original repository for more information about the framework and its usage.
