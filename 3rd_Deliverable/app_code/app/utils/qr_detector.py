import cv2
from pyzbar.pyzbar import decode

def decode_qr():
  # Start webcam capture
  cap = cv2.VideoCapture(0)

  decoded_string = None

  while True:
      ret, frame = cap.read()
      if not ret:
          break

      # Detect and decode QR codes
      for qr in decode(frame):
          decoded_string = qr.data.decode('utf-8')
          print("✅ QR Code Detected:", decoded_string)

          # Draw bounding box around QR code
          pts = qr.polygon
          if len(pts) > 4: pts = pts[:4]
          for i in range(len(pts)):
              pt1 = pts[i]
              pt2 = pts[(i + 1) % len(pts)]
              cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

          # Stop scanning after first QR code
          cap.release()
          cv2.destroyAllWindows()
          break

      # Display the video frame
      cv2.imshow("QR Scanner - Press 'q' to Quit", frame)
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break

  # Cleanup
  cap.release()
  cv2.destroyAllWindows()

  # Print result if one was found
  if decoded_string:
      print("\n🎉 Final Decoded String:", decoded_string)
      return int(decoded_string.strip().split()[-1])
  print("\n❌ No QR code was detected.")
  return -1
      
  