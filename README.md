# rough_score

入力した文字列の誤字脱字をカウントする。

python: 3.11
openai: 1.2.0
model: gpt-3.5-turbo-1106


## 入出力例

>  個の事件は解決をみたことでもう話題にはならないだろうが、大きな反響を読んだ事は間違いなしだ。


{
  "errors": [
    {
      "original": "個",
      "corrected": "この"
    },
    {
      "original": "みた",
      "corrected": "見た"
    },
    {
      "original": "読んだ",
      "corrected": "呼んだ"
    }
  ],
  "total_errors": 3
}


この例における使用トークン数

CompletionUsage(completion_tokens=83, prompt_tokens=150, total_tokens=233)
