import boto3
import requests
import time

# Inicialização dos clientes
cliente = boto3.Session(profile_name="BRSAO186")
s3 = cliente.client("s3", region_name="us-east-1")
transcribe = cliente.client("transcribe", region_name="us-east-1")

# Definição dos nomes
bucket_name = "brsao-186-polly"
audio_key = "audios/exemplo_audio_2.mp3"
transcribe_jobname = "job-audio-exem"

# URL para o transcribe
media_uri = f"s3://{bucket_name}/{audio_key}"

# Inicio do job do Transcribe
transcribe.start_transcription_job(
    TranscriptionJobName=transcribe_jobname,
    Media={'MediaFileUri': media_uri},
    MediaFormat="mp3",
    LanguageCode= "pt-BR"
)

print("O Job do Transcribe foi iniciado...")

while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=transcribe_jobname)
    job_status = status['TranscriptionJob']['TranscriptionJobStatus']
    if job_status in ["COMPLETED", "FAILED"]:
        break
    print("Transcrição em andamento...")
    time.sleep(5)

if job_status == "COMPLETED":
    transcribe_url = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
    response = requests.get(transcribe_url)
    transcript_text = response.json()['results']['transcripts'][0]['transcript']    
    
    nome_local = "transcricao_resultado.txt"
    with open(nome_local, "w", encoding="utf=8") as file:
        file.write(transcript_text)
    print("O texto foi transcrito com sucesso!")    

    nome_s3 = "transcricoes/transcricao_resultado.txt"
    s3.upload_file(nome_local, bucket_name, nome_s3)
    print(f"A transcrição foi salva no bucket {bucket_name} no caminho {nome_s3}.")

else:
    print("Houve algum erro na transcrição.")

    




