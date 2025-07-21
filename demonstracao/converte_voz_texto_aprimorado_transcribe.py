import boto3 
import time
import requests
from botocore.exceptions import BotoCoreError, ClientError


try:
    session = boto3.Session(profile_name='BRSAO186')
    s3 = session.client('s3', region_name='us-east-1')
    transcribe = session.client('transcribe', region_name='us-east-1')

    bucket_name = 'brsao-186-polly'
    audio_s3_audio = 'audios/exemplo_audio_2.mp3'

    # Gerou um nome único utilizando timestamp
    transcription_job_name = f"job-audio-{int(time.time())}"
    media_uri = f"s3://{bucket_name}/{audio_s3_audio}"

    transcribe.start_transcription_job(
        TranscriptionJobName=transcription_job_name,
        Media={'MediaFileUri': media_uri},
        LanguageCode="pt-BR"
    )

    print(f"O Job '{transcription_job_name}' de transcrição foi iniciado... ")

    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=transcription_job_name)
        job_status = status['TranscriptionJob']['TranscriptionJobStatus']

        if job_status in ['COMPLETED','FAILED']:
            break

        print(f"A transcrição está em andamento... ")
        time.sleep(5)

    if job_status == 'COMPLETED':
        transcript_url = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
        response = requests.get(transcript_url)
        transcribe_text = response.json()['results']['transcripts'][0]['transcript']


        local_text = 'transcricao_resultado.txt'  
        with open(local_text, 'w', encoding='utf-8') as file:
            file.write(transcribe_text) 
        print(f"O texto foi transcrito e salvo como {local_text}.")    

        s3_text = f'transcricoes/{local_text}'
        s3.upload_file(local_text, bucket_name, s3_text)
        print(f"A transcrição foi salva no S3 como {s3_text}")

    else:
        print("Ocorreu um erro na transcrição")

except (BotoCoreError, ClientError) as e:
    print(f"Erro com AWS: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição HTTP: {e}")