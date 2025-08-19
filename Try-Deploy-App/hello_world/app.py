import json

import boto3
import os

from PIL import Image, ImageDraw, ImageFont

s3 = boto3.client("s3")


def lambda_handler(event, context):
    image = Image.new("RGB", (200, 200), "black")
    draw = ImageDraw.Draw(image)
    draw.text((20, 20), "hello!", fill="pink")
    image.save("/tmp/hello.png")

    s3.upload_file("/tmp/hello.png", os.environ["BUCKET_NAME"], "hello.png")

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
            }
        ),
    }
