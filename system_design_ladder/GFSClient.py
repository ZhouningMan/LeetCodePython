'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''

class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        pass

    def writeChunk(self, filename, chunkIndex, content):
        pass

class GFSClient(BaseGFSClient):
    def __init__(self, chunkSize):
        super().__init__()
        self.file_to_chunk = {}
        self.chunk_size = chunkSize

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    def read(self, filename):
        if filename not in self.file_to_chunk:
            return
        content= ''
        for i in range(self.file_to_chunk[filename]):
            content += self.readChunk(filename, i)
        return content

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    def write(self, filename, content):
        length = len(content)
        chunks = (length - 1) // self.chunk_size + 1
        self.file_to_chunk[filename] = chunks
        for i in range(chunks):
            self.writeChunk(filename, i, content[i * self.chunk_size: (i + 1) * self.chunk_size])
