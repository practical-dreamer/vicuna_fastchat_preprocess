import ijson
import json
import argparse
from fastchat.train.train import make_supervised_data_module, DataArguments, preprocess
from transformers import AutoTokenizer
from tqdm import tqdm

def roles_are_alternating(conversations, human_name, ai_name, strict_format):
    if strict_format and (not conversations or conversations[0]["from"] != human_name):
        return False

    for i in range(1, len(conversations)):
        if strict_format and (
            conversations[i]["from"] == conversations[i - 1]["from"] or \
            conversations[i]["from"] not in [human_name, ai_name] or \
            conversations[i - 1]["from"] not in [human_name, ai_name]
        ):
            return False
    return True

def main(args):
    tokenizer = AutoTokenizer.from_pretrained(
        args.model_path,
        model_max_length=args.model_max_length,
        padding_side='right',
        use_fast=False
    )
    tokenizer.pad_token = tokenizer.unk_token

    with open(args.input_json_path, 'r') as f, open(args.output_txt_path, 'w') as out_f:
        conversations_generator = ijson.items(f, 'item.conversations')

        # Get the total number of conversations
        total_conversations = sum(1 for _ in ijson.items(open(args.input_json_path, 'r'), 'item.conversations'))

        buffer = []
        for conversations in tqdm(conversations_generator, total=total_conversations, desc="Processing conversations"):
            # Filter out empty conversations, conversations with a "system" role, and conversations where roles aren't alternating
            if conversations and roles_are_alternating(conversations, args.human_name, args.ai_name, args.strict_format):
                buffer.append({"conversations": conversations})

            if len(buffer) >= 2:
                # Write buffered conversations to a temporary JSON file
                with open(args.temp_json_path, 'w') as temp_f:
                    json.dump(buffer, temp_f)

                # Process the temporary JSON file
                data_args = DataArguments(data_path=args.temp_json_path, lazy_preprocess=False)
                data_module = make_supervised_data_module(tokenizer=tokenizer, data_args=data_args)

                for conversation in buffer:
                    data_dict = preprocess([conversation["conversations"]], tokenizer)
                    input_ids = data_dict["input_ids"]
                    decoded_text = tokenizer.decode(input_ids[0], skip_special_tokens=True)

                    # Append the decoded text to the output file
                    out_f.write(decoded_text + '\n')

                buffer = []

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process Conversations')
    parser.add_argument('--human_name', default='human', help='Name to use for human role')
    parser.add_argument('--ai_name', default='gpt', help='Name to use for AI role')
    parser.add_argument('--model_max_length', type=int, default=2048, help='Maximum sequence length for the model')
    parser.add_argument('--model_path', required=True, help='Path to the model')
    parser.add_argument('--input_json_path', required=True, help='Path to the input JSON file')
    parser.add_argument('--output_txt_path', required=True, help='Path to the output TXT file')
    parser.add_argument('--temp_json_path', default='buffer.json', help='Path to the temporary JSON file for buffering')
    parser.add_argument('--strict_format', action='store_false', default=True, help='Disable strict formatting filters')

    args = parser.parse_args()
    main(args)
