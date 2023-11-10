import pickle

from openai import OpenAI


def gpt(client, utterance):
    base_prompt = """次の文章について、誤字脱字の数を数えて教えてください。

    """

    print(base_prompt + utterance)

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
    client = OpenAI()

    res, usage = gpt(
        client,
        "個の事件は解決をみたことでもう話題にはならないだろうが、大きな反響を読んだ事は間違いなしだ。",
    )

    print(res)

    print(usage)

    print("#######")
    with open("artifacts/message.pkl", "wb") as f:
        pickle.dump(res, f)

    with open("artifacts/usage.pkl", "wb") as f:
        pickle.dump(usage, f)

    res, usage = gpt(
        client,
        "直樹は来月からの生活に胸を踊らせていた。大都会、一人暮らし、電車通勤と、すべからく人生初の挑戦だ。あのまま父親の経営する会社にいれば、順調に出世して、いずれは社長を継ぐことになっただろう。しかし、自分に経営者としての才能がないのは、よく自負している。新しい勤め先は、親の力を借りずに探した。都会ではそんなに知名度のある会社ではないので、資産家の息子だとばれることはないだろうが、人の口に戸は立てられない。どこで知られないともかぎらないから、そこは注意するに越したことはない。",
    )

    print(res)

    print(usage)

    print("#######")
    res, usage = gpt(
        client,
        "小子化の進む中、あえて学習塾を起業してはや5年。授業料は高いが、それに違わない高品質の個別指導を売り物にしたのだが、これほど流行るとはゆめゆめ思わなかった。妻も心配してくれていたから、きょうは慰労の旅行に来ている。海を望むレストランで、先ほどディナーをしたところだ。バルコニーで満天の星を見上げながら、ふと笑みがこぼれる。",
    )

    print(res)

    print(usage)

    print("#######")
    res, usage = gpt(
        client,
        "NHKのニュースが、誰でも知っている二枚目俳優が飲酒運転で逮捕された、と報じていた。アルコール依存症で長年苦しんでいたらしい。真一郎はそんな馬鹿な、と思ったが、国営放送が億測で報道するはずがない。才色兼備の彼が、何でそんなふうになってしまったのだろう。",
    )

    print(res)

    print(usage)
