class ReviewSystem:
    def __init__(self):
        self.reviews = {}

    def add_review(self, tutor, review):
        self.reviews.setdefault(tutor, []).append(review)
        print(f"Review agregada para {tutor}: {review}")

    def edit_review(self, tutor, index, new_review):
        if tutor in self.reviews and 0 <= index < len(self.reviews[tutor]):
            old = self.reviews[tutor][index]
            self.reviews[tutor][index] = new_review
            print(f"Review editada para {tutor}: '{old}' -> '{new_review}'")
        else:
            print("No se pudo editar la review.")

    def delete_review(self, tutor, index):
        if tutor in self.reviews and 0 <= index < len(self.reviews[tutor]):
            deleted = self.reviews[tutor].pop(index)
            print(f"Review eliminada para {tutor}: '{deleted}'")
        else:
            print("No se pudo eliminar la review.")
