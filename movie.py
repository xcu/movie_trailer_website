NO_IMAGE = 'http://www.ekhitxanpona.org/leihatila/img/noimage.jpeg'


class Movie(object):
    def __init__(self, title,
                 trailer_youtube_url='', poster_image_url=NO_IMAGE):
        self.trailer_youtube_url = trailer_youtube_url
        self.title = title
        self.poster_image_url = poster_image_url