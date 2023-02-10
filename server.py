
import glob

mp3paths = glob.glob('E:/audios/*.mp3', recursive=True)
for mp3path in mp3paths:
    textpath = mp3path.replace('audios', 'audios_text').replace('mp3', 'txt')
    with open(textpath, "r", encoding="utf-8") as fp:
        text = fp.read()
        a = 1



# import whisper

# model = whisper.load_model("base")

# # load audio and pad/trim it to fit 30 seconds
# audio = whisper.load_audio("audio.mp3")
# audio = whisper.pad_or_trim(audio)

# # make log-Mel spectrogram and move to the same device as the model
# mel = whisper.log_mel_spectrogram(audio).to(model.device)

# # detect the spoken language
# _, probs = model.detect_language(mel)
# print(f"Detected language: {max(probs, key=probs.get)}")

# # decode the audio
# options = whisper.DecodingOptions()
# result = whisper.decode(model, mel, options)

# # print the recognized text
# print(result.text)