import whisper
import os


def get_audio_sub(input_file: str, model_type='small', language=None):
    """
        Input an audio or video and specify the output language, return subtitle data in SRT format.
    """
    if isinstance(input_file, str):
        model = whisper.load_model(model_type)
        result = model.transcribe(input_file)
        '''result = {'text': '...', 
                    'segments': [{'id': 0, 'seek': 0, 'start': 0.0, 'end': 10.200000000000001, 'text': '...', 'tokens': [50364, 44537,...], 'temperature': 0.0, 'avg_logprob': -0.23897131895407653, 'compression_ratio': 1.0934579439252337, 'no_speech_prob': 0.3848685920238495}], 
                    'language': 'ja'}
        '''
        return generate_srt_dict(result, language)
    raise TypeError("Invalid input type. Expected a string.")


def get_audio_subs(input_files: list[str], model_type='small', language=None):
    """
            Input a list of audio or video files and specify the output language, return a list of subtitle data in SRT format.
    """
    if isinstance(input_files, list):
        for file in input_files:
            if not isinstance(file, str):
                raise TypeError("Invalid input type. Expected a string.")
        model = whisper.load_model(model_type)
        subs = [generate_srt_dict(model.transcribe(file), language) for file in input_files]
        return subs
    raise TypeError("Invalid input type. Expected a string or a list of strings.")


def save_audio_sub(input_file: str, model_type='small', language=None):
    """
        Save the SRT file in the same directory as the input file.
    """
    sub = get_audio_sub(input_file, model_type, language)
    file_name, _ = os.path.splitext(input_file)
    file_name += '.srt'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(generate_str_str(sub))


def save_audio_subs(input_files: list[str], model_type='small', language=None):
    """
        Save the SRT files in the same directory as the input files.
    """
    subs = get_audio_subs(input_files, model_type, language)
    for i in range(len(input_files)):
        file_name, _ = os.path.splitext(input_files[i])
        file_name += '.srt'
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(generate_str_str(subs[i]))


def generate_srt_dict(input, language=None):
    if not language or language == input['language']:
        subtitles = [to_srt_format(text) for text in input['segments']]
        return subtitles
    # if texts need translate
    # to be implemented
    # subtitles = []


def generate_str_str(input):
    srt_content = ''
    for subtitle in input:
        srt_content += f"{subtitle['index']}" + os.linesep
        srt_content += f"{subtitle['start']} --> {subtitle['end']}" + os.linesep
        srt_content += f"{subtitle['text']}" + os.linesep + os.linesep
    """
        1
        00:00:01,000 --> 00:00:03,000
        Hello, this is the first subtitle.
    """
    return srt_content


def to_srt_format(raw):
    result = {'index': int(raw['id']), 'start': seconds_to_srt_time(raw['start']),
              'end': seconds_to_srt_time(raw['end']), 'text': raw['text']}
    """
    {
        'index': 1,
        'start': '00:00:01,000',
        'end': '00:00:03,000',
        'text': 'Hello, this is the first subtitle.'
    }
    """
    return result


def seconds_to_srt_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    remaining_seconds = seconds % 60
    srt_seconds, milliseconds = divmod(remaining_seconds, 1)
    srt_seconds = int(srt_seconds)
    milliseconds = int(milliseconds * 1000)

    srt_time = f"{hours:02d}:{minutes:02d}:{srt_seconds:02d},{milliseconds:03d}"
    return srt_time
