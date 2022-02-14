

#from __future__ import absolute_import, division, print_function, unicode_literals



import os
import logging


from .extractor import extract_urls
from .backends import PDFMinerBackend
from .exceptions import FileNotFoundError, PDFInvalidError
from pdfminer.pdfparser import PDFSyntaxError

from io import BytesIO
from urllib.request import Request, urlopen

unicode = str

logger = logging.getLogger(__name__)


class PDFx(object):


    # Available after init
    uri = None  # Original URI
    fn = None  # Filename part of URI
    is_url = False  # False if file
    is_pdf = True

    stream = None  # ByteIO Stream
    reader = None  # ReaderBackend
    summary = {}

    def __init__(self, uri):
        """
        Open PDF handle and parse PDF metadata
        - `uri` can bei either a filename or an url
        """
        logger.debug("Init with uri: %s" % uri)

        self.uri = uri

        # Find out whether pdf is an URL or local file
        url = extract_urls(uri)
        self.is_url = len(url)

        # Grab content of reference
        if self.is_url:
            logger.debug("Reading url '%s'..." % uri)
            self.fn = uri.split("/")[-1]
            try:
                content = urlopen(Request(uri)).read()
                self.stream = BytesIO(content)
            except Exception as e:
                print("Pas bon ")
                #raise DownloadError("Error downloading '%s' (%s)" % (uri, unicode(e)))

        else:
            if not os.path.isfile(uri):
                raise FileNotFoundError("Invalid filename and not an url: '%s'" % uri)
            self.fn = os.path.basename(uri)
            self.stream = open(uri, "rb")

        # Create ReaderBackend instance
        try:
            self.reader = PDFMinerBackend(self.stream)
        except PDFSyntaxError as e:
            raise PDFInvalidError("Invalid PDF (%s)" % unicode(e))
        except Exception as e:
            raise
    
    def get_text(self):
        return self.reader.get_text()
