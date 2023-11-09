import pickle

from openai import OpenAI


def gpt(utterance):
    base_prompt = """
    次の文章について、誤字脱字の数を数えて教えてください。また、間違えていた語句を教えてください。


    """

    client = OpenAI()
    print(client.models.list())

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": "あなたはよくできた誤字脱字チェックシステムで、全てJSON形式で出力します。",
            },
            {"role": "user", "content": base_prompt + utterance},
        ],
    )

    with open("artifacts/response.pkl", "wb") as f:
        pickle.dump(response, f)
    return response.choices[0].message.content, response.usage


if __name__ == "__main__":
    res, usage = gpt(
        "個の事件は解決をみたことでもう話題にはならないだろうが、大きな反響を読んだ事は間違いなしだ。",
    )

    print(res)

    print(usage)

    with open("artifacts/message.pkl", "wb") as f:
        pickle.dump(res, f)

    with open("artifacts/usage.pkl", "wb") as f:
        pickle.dump(usage, f)
