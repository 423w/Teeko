
from pydub import AudioSegment
from pydub.playback import play
import threading

def storm_sound():
    """ this plays the fortnite storm sound """
    play(AudioSegment.from_wav("Fortnite (storm eye incoming) sfx.wav"))


def win_sound():
    """this plays Dr. O saying you win in a goofy voice"""
    sound = AudioSegment.from_wav('Texas A&M University.wav')
    t = threading.Thread(target=play, args=(sound,))
    t.start()

def cam_beat():
    """this plays cams beat"""
    sound = AudioSegment.from_wav('cams_beat.wav')[:10000]
    t = threading.Thread(target=play, args=(sound,))
    t.start()


def explosion():
    """ this play a funny explosion sound """
    sound = AudioSegment.from_wav('new explosion (with sound).wav')[:1500]
    t = threading.Thread(target=play, args=(sound,))
    t.start()

def jazz():
    """ this plays jazz"""
    sound = AudioSegment.from_wav('5 Minutes Jazz Music for Relaxing.wav')
    t = threading.Thread(target=play, args=(sound,))
    t.start()

def place():
    """this plays a thud like you're placing a piece down"""
    sound = AudioSegment.from_wav("place_sound.wav")
    t = threading.Thread(target=play, args=(sound,))
    t.start()

