import cv2 as cv
import argparse
import Classes


def follow_people():
    ap = argparse.ArgumentParser()
    ap.add_argument("-video", required=True, help="Path of the video.")
    args = vars(ap.parse_args())

    # we create the objects defined on "Classes"
    inout = Classes.FileInOut()
    imgtreat = Classes.ImageTreatment()
    findfollow = Classes.FindAndFollow()
    viddata = Classes.VideoData()

    file_data = inout.filecreator()
    video_input, image_past = viddata.videoin(args)

    while video_input.isOpened():
        ret, image = video_input.read()
        if not ret:
            break
        img = imgtreat.mean(image_past, image)
        img = imgtreat.clean(img)
        img, data = findfollow.detect(img,image)
        cross, no_cross = findfollow.follow(data)

        inout.printer(file_data, cross, no_cross, int(video_input.get(1)))
        cv.imshow("Frame", img)
        cv.waitKey(22)

    findfollow.finalreport(file_data, inout)
    video_input.release()
    file_data.close()
    cv.destroyAllWindows()


if __name__ == "__main__":
    follow_people()
