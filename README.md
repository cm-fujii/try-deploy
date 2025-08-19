# はじめに

妖精さんのいたずらで、本アプリケーションがデプロイできなくなりました。

# 目的

AWSへのデプロイを成功させてください。
作業過程における思考やふるまいなどを見せていただきます。

※インターネットで検索するなどは、問題ありません。

# 共通情報

## デプロイ先のAWSアカウント

- xxx

## デプロイ先のIAMロール（AssumeRole用）

- 事前に伝えています
- 不明な場合は教えてください

# お願い

- 画面共有して作業をしてください
- 今の作業内容や考えていることなどを、適宜、声に出して伝えてください
- AI関連ツールの利用は控えてください

# 手順

## 1. 任意のフォルダを選択し、デプロイしてください。

| フォルダ名 | IaC | Lambda |
| xxx | AWS SAM | Python |

各フォルダ内の `README.md` を参考にしてください。

## 2. APIから下記のResponseが返ってきたらOKです。

```bash
$ curl https://example.com/v1/hello

{"message": "hello world"}
```

## 3. S3からオブジェクトを取得し、「hello」を記載があればOKです。

```bash
aws s3 cp s3://aws-sam-cli-managed-default-samclisourcebucket-1t8vcnv9f5use/hello.png hello.png
```

