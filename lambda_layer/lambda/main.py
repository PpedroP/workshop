import pandas
def handler(event, context):
    print('lista lambda con pandas', pandas.__version__)
    return 'ok'