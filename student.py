class Student :
    def __init__(self, hometown, age, height, fav_icecream):
        self.hometown= hometown
        self.age= age
        self.height= height
        self.fav_icecream= fav_icecream
    def print_summary(self):
        print("Hometown: "+self.hometown+" age: "+str(self.age)+" height: "+str(self.height)+" favorite ice cream flavor: "+self.fav_icecream)

    def get_giraffe_gap(self):
        return(500-self.height)
