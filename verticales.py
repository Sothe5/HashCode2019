class Photo:
    def __init__(self, position, tags, id):
        self.position = position
        self.tags = tags
        self.id = id

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




def printPhotos(photos):
    for photo in photos:
        print(photo.position)
        print(photo.tags)
        print(photo.id)



def separatePhotos(photos):
    verticals = []
    horizontals = []
    for photo in photos:
        if (photo.position == "V"):
            verticals.append(photo)
        else:
            horizontals.append(photo)
    return verticals, horizontals

def groupVerticals(verticals):
    slides = []
    for photo1 in verticals:
        photo1_copy = photo1
        best_photo = photo1
        prev_similar_tags = len(photo1.tags)
        verticals.remove(photo1)
        for photo2 in verticals:
            similar_tags = len(list(set(photo1_copy.tags).intersection(photo2.tags)))
            if (similar_tags < prev_similar_tags):
                best_photo = photo2
                prev_similar_tags = similar_tags
        if(photo1_copy.id != best_photo.id):
            slides.append(Photo("H", list(set().union(photo1_copy.tags, best_photo.tags)), [photo1_copy.id, best_photo.id]))
        verticals.remove(best_photo)
        #printPhotos([slides[len(slides)-1]])
    return slides

def createSlides(photos):
    verticals, horizontals = separatePhotos(photos)
    vertical_slides = groupVerticals(verticals)
    slides = horizontals
    for vertical_slide in vertical_slides:
        slides.append(vertical_slide)
    return slides



photos = readData("c_memorable_moments.txt")
#verticals, horizontals = separatePhotos(photos)
#slides_verticals = groupVerticals(verticals)
slides = createSlides(photos)
printPhotos(slides)
