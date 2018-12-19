"""
Mopidy amazon music backend
"""
import pykka
from mopidy import core


class AmazonMusicBackend(pykka.ThreadingActor, backend.Backend):
    """
    Amazon music backend
    """

    def __init__(self, config, audio):
        """
        constrcutor

        :param config: configuration
        :param audio: audio actor
        """
        super(AmazonMusicBackend, self).__init__()
        self._audio = audio
        self._config = config
