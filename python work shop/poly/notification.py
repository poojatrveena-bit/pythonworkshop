class Notification:

    def get_notification(self):
        pass

class Instagram(Notification):

    def get_notification(self):
        print("Notification from Instagram")
class FaceBook(Notification):
    def get_notification(self):
        print("Notification from FaceBook")

instagram=Instagram()
instagram.get_notification()

facebook=FaceBook()
facebook.get_notification()