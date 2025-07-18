import boto3

# Definir cliente
session = boto3.Session(profile_name="BRSAO186")
polly_client = session.client("polly", region_name="us-east-1")
s3_client = session.client("s3", region_name="us-east-1")

# Definir texto para conversão em voz
texto_voz = "Da escrita a voz, da voz a escrita: um ciclo completo."

# Gerar a voz
response = polly_client.synthesize_speech(
    Text=texto_voz,
    Engine='neural',
    OutputFormat='mp3',
    VoiceId='Thiago'
)

# Definir nome dos arquivos
nome_bucket = "brsao-186-polly"
nome_arquivo_local = "exemplo_audio_2.mp3"
nome_arquivo_s3 = "audios/exemplo_audio_2.mp3"

# Salvar localmente
with open(nome_arquivo_local, "wb") as file:
    file.write(response['AudioStream'].read())

# Salvar no S3
s3_client.upload_file(nome_arquivo_local, nome_bucket, nome_arquivo_s3)

print(f"Voz gerada e enviada para o bucket {nome_bucket} no caminho {nome_arquivo_s3}.")
