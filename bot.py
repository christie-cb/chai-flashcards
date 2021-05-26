from chai_py import ChaiBot, Update
from flashcards import Flashcard, MessageType
from flashcards_list import FLASHCARDS

class Bot(ChaiBot):
    def setup(self):
        self.logger.info("Setting up...")
        self.flashcards = FLASHCARDS
        self.previous_messagetype = None

    async def on_message(self, update: Update) -> str:
        if self.previous_messagetype is MessageType.QUESTION:
            self.previous_messagetype = MessageType.QUALITY
            return f"Answer: {self.flashcards[0].answer}\n\nHow easy was this? (1-5)"
        if self.previous_messagetype is MessageType.QUALITY:
            self.flashcards[0].update_review(update.latest_message.text)
            print(self.flashcards[0].review)
            self.flashcards.sort()
        self.previous_messagetype = MessageType.QUESTION
        return self.flashcards[0].question

if __name__=="__main__":
    from chai_py import TRoom
    troom = TRoom([Bot()])
    troom.chat()
