import cv2
import numpy as np
import requests

url = "http://192.168.2.215:8080/shot.jpg"
output_file = "kayit.mp4"  # Kaydedilecek video dosyası adı
output_width = 640
output_height = 480
fps = 30  # Video FPS (kare hızı)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter(output_file, fourcc, fps, (output_width, output_height))

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (output_width, output_height))

    cv2.imshow("a", img)
    video_writer.write(img)

    if cv2.waitKey(1) == 27:
        break

video_writer.release()
cv2.destroyAllWindows()
