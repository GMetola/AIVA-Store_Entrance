import cv2 as cv
import argparse
import Classes


def follow_people():
    ap = argparse.ArgumentParser()
    ap.add_argument("-video", required=True, help="Path of the video.")
    args = vars(ap.parse_args())

    # we create the objects defined on "Classes"
    io = Classes.FileInOut()
    it = Classes.ImageTreatment()
    ff = Classes.FindAndFollow()
    vd = Classes.VideoData()

    file_data = io.filecreator()
    video_input, image_past = vd.videoin(args)

    while video_input.isOpened():
        ret, image = video_input.read()
        if not ret:
            break
        img = it.mean(image_past, image)
        img = it.clean(img)
        img, data = ff.detect(img)
        cross, no_cross = ff.follow(data)

        io.printer(file_data, cross, no_cross, int(video_input.get(1)))
        cv.imshow("Frame", img)
        cv.waitKey(22)

    video_input.release()
    file_data.close()
    cv.destroyAllWindows()


if __name__ == "__main__":
    follow_people()
