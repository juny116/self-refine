import json

from tqdm import tqdm
from argparse import ArgumentParser

from src.code_optim.utils import call_gpt
from src.code_optim.prompts import PROMPT_CRITIQUE, PROMPT_FIX

MAX_EXAMPLE = 100
ROUNDS = 5
FILE_PATH = "/data/juny116/CoE/code_optim/python_splits/test.jsonl"


def main():
    parser = ArgumentParser()
    parser.add_argument("--file", type=str, default=FILE_PATH)
    parser.add_argument("--output", type=str, default="optim.jsonl")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        examples = [json.loads(line) for line in f.readlines()]

    with open(args.output, "w") as f:
        for example in tqdm(examples[:MAX_EXAMPLE]):
            rounds = []
            code = example["input"]
            code = code.replace("\n\n", "\n")
            for round_number in range(ROUNDS):
                prompt = PROMPT_CRITIQUE.format(code=code)
                suggestion = call_gpt(prompt, temperature=0.0)[0]
                prompt = PROMPT_FIX.format(code=code, suggestion=suggestion)
                code = call_gpt(prompt)[0].strip()
                rounds.append({"suggestion": suggestion, "updated_code": code})
            f.write(
                json.dumps({"original_code": example["input"], "updates": rounds})
                + "\n"
            )


if __name__ == "__main__":
    main()
