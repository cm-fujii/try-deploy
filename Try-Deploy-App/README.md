# 前提

- 必要なS3バケットは作成済みです
  - aws-sam-cli-managed-default-samclisourcebucket-1t8vcnv9f5use

# デプロイ手順

## OepnAPIファイルをS3バケットに格納する

```bash
aws s3 cp openapi.yaml s3://aws-sam-cli-managed-default-samclisourcebucket-1t8vcnv9f5use/Try-Deploy-App/openapi.yaml
```

## デプロイする

```bash
sam deploy
```

## APIからResponseが返ってくることを確認する

- URLは調べてください
- 正常にResponseが返ってこればOKです
  - サンプルは ../README.md を参照
