import boto3

# Inicialização do cliente Polly
session = boto3.Session(profile_name="BRSAO186")
client = session.client("polly", region_name="us-east-1")

# Definição do texto para conversão em voz
texto_voz = "Olá, Esse aqui é um exemplo de geração de voz com o Polly."

# Configuração para criação da voz
response = client.synthesize_speech(
    Text=texto_voz,
    Engine='neural',
    OutputFormat='mp3',
    VoiceId='Vitoria'
)

# Salvar o arquivo de voz localmente
nome_arquivo = "exemplo_audio.mp3"
with open(nome_arquivo,"wb") as file:
    file.write(response['AudioStream'].read())


print(f"Voz gerada e salva como {nome_arquivo}.")