import cv2

# فتح الفيديو أو الكاميرا
cap = cv2.VideoCapture(0)

# تحديد إعدادات الفيديو
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # أو "XVID" أو "MJPG"
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)  # كتابة الإطارات إلى الملف
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # إنهاء بالضغط على 'q'
        break

cap.release()
out.release()
cv2.destroyAllWindows()
