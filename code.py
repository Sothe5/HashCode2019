class Photo:
    def __init__(self, position, tags, id):
        self.position = position
        self.tags = tags
        self.id = id;

class Slide:
    def __init__(self, tags, id):
        self.position = position
        self.tags = tags
        self.id = id


def readData(input_file):   
    input = open(input_file, "r")
    photos = []
    n_photos = int(input.readline())
    for photo in range(0, n_photos):
        photo_data = input.readline().rstrip().split(" ")
        position = photo_data[0]
        n_tags = int(photo_data[1])
        tags = []
        for tag in range(2, n_tags + 2):
            tags.append(photo_data[tag])
        photos.append(Photo(position, tags, photo))

    return photos


def calculateScoreBetweenPhotos(photoA, photoB):
    n_common_tags = 0;
    for tag in photoA.tags:
        if tag in photoB.tags:
            n_common_tags = n_common_tags + 1
    return min([n_common_tags, len(photoA.tags) - n_common_tags, len(photoB.tags) - n_common_tags])
    

def printPhotos(photos):
    for photo in photos:
        print(photo.position)
        print(photo.tags)


photos = readData("a_example.txt")
# print(photos)
