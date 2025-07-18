import boto3
import json

# Inicio de sessão com perfil específico
session = boto3.Session(profile_name="BRSAO186")
rekognition = session.client('rekognition', region_name='us-east-1')
s3 = session.client('s3', region_name='us-east-1')

# Definição de parâmetros
bucket = "brsao-186-rekognition"
imagem = "s3-service.png"
resultado_json = "resultado-imagem.json"

# Detectar os rótulos (labels) da imagem
response = rekognition.detect_labels(
        Image={
        "S3Object": {
            "Bucket": bucket,
            "Name": imagem
        }
    },
    MaxLabels=10,
    MinConfidence=80
)

# Extraindo os rótulos
labels = response["Labels"]

# Salvando o resultado num json no bucket
s3.put_object(
    Bucket=bucket,
    Key=resultado_json,
    Body=json.dumps(labels, indent=2),
    ContentType='application/json'
)

print(f"O resultado foi salvo com sucesso no bucket {bucket} como {resultado_json}.")