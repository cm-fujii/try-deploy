deploy:
	aws s3 cp openapi.yaml s3://aws-sam-cli-managed-default-samclisourcebucket-1t8vcnv9f5use/Try-Deploy-App/openapi.yaml
	sam build --use-container
	sam deploy

deploy-1st:
	sam build --use-container
	sam deploy \
		--region ap-northeast-1 \
		--stack-name Try-Deploy-App-Stack
