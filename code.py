import math

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
        photos.append(Photo(position, tags, [photo]))

    return photos


def calculateScoreBetweenSlides(slideA, slideB):
    n_common_tags = 0;
    for tag in slideA.tags:
        if tag in slideB.tags:
            n_common_tags = n_common_tags + 1
    return min([n_common_tags, len(slideA.tags) - n_common_tags, len(slideB.tags) - n_common_tags])
    
def calculateScoreOfSlideshow(slide_show):
    score = 0
    for i in range(1, len(slide_show)):
        score = score + calculateScoreBetweenSlides(slide_show[i-1], slide_show[i]);
    return score

def printPhotos(photos):
    for photo in photos:
        print(photo.position)
        print(photo.tags)


def slideshow_maker(input_file):
    photos = readData(input_file)
    #print(len(photos))
    # printPhotos(photos)
    # print("-----------------------")
    # convert to slides
    slides = createSlides(photos)
    #print ('Converted to slides')
    slides = sortSlides(slides)
    slideshow = []
    tail = slides[0]
    slideshow.append(tail)    

    while (len(slides) > 1):
        # print(len(slides))
        # if (len(slides) % 1000 == 0):
        #     print(len(slides))
        slides.remove(tail)  # remove from slides
        bestScore = 0
        bestSlide = slides[0]
        for slide in slides:
            score = calculateScoreBetweenSlides(tail, slide)
            if (score > bestScore):
                bestScore = score
                bestSlide = slide
            if (score >= len(slide.tags)/2 - 0.5):
                break
        
        slideshow.append(bestSlide)
        tail = bestSlide
    
    return slideshow

def printSubmission(slideshow):
    print(len(slideshow))
    for slide in slideshow:
        for id in slide.id:
            print(id, end=' ')
        print()

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
        best_similar_tags = len(photo1.tags)
        verticals.remove(photo1)
        for photo2 in verticals:
            continue_for = False
            similar_tags = 0;
            for tag in photo1_copy.tags:
                if tag in sorted(photo2.tags):
                    similar_tags = similar_tags + 1
                    if (similar_tags == best_similar_tags):
                        continue_for = True
                        break
                if (continue_for):
                    continue

            if (similar_tags < best_similar_tags):
                best_photo = photo2
                best_similar_tags = similar_tags
            if(best_similar_tags == 0):
                break
        if(photo1_copy.id[0] != best_photo.id[0]):
            slides.append(Photo("H", list(set().union(photo1_copy.tags, best_photo.tags)), [photo1_copy.id[0], best_photo.id[0]]))
        verticals.remove(best_photo)
        #printPhotos([slides[len(slides)-1]])
        # if (len(slides) % 100 == 0):
        #     print(len(slides))
    return slides


def sortByLenTags(slide):
    return len(slide.tags)

def sortSlides(slides):
    slides.sort(key = sortByLenTags)
    return slides

def createSlides(photos):
    verticals, horizontals = separatePhotos(photos)
    vertical_slides = groupVerticals(verticals)
    slides = horizontals
    for vertical_slide in vertical_slides:
        slides.append(vertical_slide)
    return slides

#slideshow = slideshow_maker("a_example.txt")
#slideshow = slideshow_maker("b_lovely_landscapes.txt")
#slideshow = slideshow_maker("e_shiny_selfies.txt")
slideshow = slideshow_maker("d_pet_pictures.txt")
printSubmission(slideshow)
#print('-------------- Score --------------')
#print(calculateScoreOfSlideshow(slideshow))


