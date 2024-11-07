import cv2
from deepface import DeepFace
import threading

cam = cv2.VideoCapture(0)
counter = 0
face_match = False
ref_image = cv2.imread(r'C:\moughit.jpg')

if ref_image is None:
    print("خطأ: لم يتم تحميل الصورة المرجعية.")
    cam.release()
    cv2.destroyAllWindows()
    exit()

ref_image_rgb = cv2.cvtColor(ref_image, cv2.COLOR_BGR2RGB)

lock = threading.Lock()

def check(frame):
    global face_match
    try:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = DeepFace.verify(frame_rgb, ref_image_rgb)
        
        with lock:
            face_match = result['verified']
        print("مطابقة:", face_match)
    except Exception as e:
        print(f"حدث خطأ أثناء التحقق: {e}")
        with lock:
            face_match = False

while True:
    ret, frame = cam.read()
    if not ret or frame is None:
        print("الإطار غير صالح")
        break

    if counter % 30 == 0:
        threading.Thread(target=check, args=(frame.copy(),), daemon=True).start()

    counter += 1

    text = "MATCH" if face_match else "NO MATCH"
    color = (0, 255, 0) if face_match else (0, 0, 255)
    cv2.putText(frame, text, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 3)

    cv2.imshow("video", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
