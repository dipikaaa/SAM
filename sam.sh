#!/bin/bash
sam package --template-file DipikaSSmOpen1Function.yml --s3-bucket dipika-bucket --output-template-file packaged.yaml
sam deploy --template-file ./packaged.yaml --stack-name DipikaSAM3 --capabilities CAPABILITY_IAM
