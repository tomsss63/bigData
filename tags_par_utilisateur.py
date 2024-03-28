from mrjob.job import MRJob

class TagsParUtilisateur(MRJob):

    def mapper(self, _, line):
        # Ignorer l'en-tête
        if line.startswith('userId'):
            return
        parts = line.split(',')
        userId = parts[0]
        yield userId, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    TagsParUtilisateur.run()
