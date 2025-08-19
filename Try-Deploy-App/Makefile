deploy:
	aws s3 cp openapi.yaml s3://aws-sam-cli-managed-default-samclisourcebucket-1t8vcnv9f5use/Try-Deploy-App/openapi.yaml
	sam build --use-container
	sam deploy
