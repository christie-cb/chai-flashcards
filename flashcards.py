from enum import Enum, auto
from supermemo2 import SMTwo

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.review = None

    def update_review(self, quality):
        """ Take the user's input to set the flashcard 'easiness'. """
        quality = int(quality)
        if self.review is None:
            self.review = SMTwo.first_review(quality)
            return self.review
        self.review = self.review.review(quality)
        return self.review

    def __lt__(self, other):
        """ Use the magic 'less-than' method to help us sort the flashcards. """
        if self.review is None:
            return True
        if other.review is None:
            return False
        if self.review.review_date == other.review.review_date:
            return self.review.easiness < other.review.easiness
        return self.review.review_date < other.review.review_date

    def __repr__(self):
        """ Giving our Flashcard a printable output can be helpful
            in the development process. """
        return f"{self.question}, {self.answer}, {self.review}"


class MessageType(Enum):
    QUESTION = auto()
    ANSWER = auto()
    QUALITY = auto()

