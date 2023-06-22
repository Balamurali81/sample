import sys
def handler(event, context):
    return 'Hello from AWS AWS Lambda using Python and container images from ECR' + sys.version + '!' 
