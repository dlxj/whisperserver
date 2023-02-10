
import whisper
model = whisper.load_model("medium")
import glob

mp3paths = glob.glob('./audios/*.mp3', recursive=True)
for mp3path in mp3paths:
    textpath = mp3path.replace('audios', 'audios_text').replace('mp3', 'txt')
    with open(textpath, "r", encoding="utf-8") as fp:
        text = fp.read()

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(mp3path)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    # _, probs = model.detect_language(mel)
    # print(f"Detected language: {max(probs, key=probs.get)}")

    #prompt='以下是普通话的句子'
    #result = model.transcribe(audioFile, task='translate',language='zh',verbose=True,initial_prompt=prompt)

    # decode the audio
    options = whisper.DecodingOptions(language="Japanese")
    #options['language'] = 'Japanese'


    #decode_options = dict(language="Japanese", **options)
    # transcribe_options = dict(task="transcribe", **decode_options)

    # transcription = model.transcribe("kittens_30secs.mp3", **transcribe_options)
    # print(transcription["text"])


    result = whisper.decode(model, mel, options)

    # print the recognized text
    print(f'predict: {result.text}')
    print(f'origin : {text}')


