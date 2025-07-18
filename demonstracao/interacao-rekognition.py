# Importar o SDK da AWS para python
import boto3

# Fazendo com que o script tenha permissões de acesso aos serviços da AWS
session = boto3.Session(profile_name='BRSAO186')

# Criando um cliente o serviço do Rekognition numa região específica
client = session.client('rekognition', region_name='us-east-1')

# Detectar objetos numa imagem do S3
response = client.detect_labels(
    Image={
        "S3Object": {
            "Bucket": "brsao-186-rekognition",
            "Name": "imagem_01.png"
        }
    },
    MaxLabels=10
    #MinConfidence=80
)

# Exibir o resultado da deteção
for label in response["Labels"]:
    print(f"Objeto: {label['Name']}, Confiança: {label['Confidence']:.2f}%")