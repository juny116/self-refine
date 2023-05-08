PROMPT_SINGLE = (
    """
I have some code. Can you optimize the code. 

{code}
""".strip()
    + "\n"
)

PROMPT_CRITIQUE = (
    """
I have some code. Can you give one suggestion to optimize the code. Don't fix the code, just give a suggestion.

{code}
""".strip()
    + "\n"
)

PROMPT_FIX = (
    """
I have some code. Can you give one suggestion to optimize the code. Don't fix the code, just give a suggestion.

{code}

{suggestion}

Now fix the code.
""".strip()
    + "\n"
)
