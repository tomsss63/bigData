from mrjob.job import MRJob

class TagsParFilm(MRJob):

    def mapper(self, _, line):
        # Ignorer l'en-tête
        if line.startswith('userId'):
            return
        parts = line.split(',')
        movieId = parts[1]
        yield movieId, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    TagsParFilm.run()
