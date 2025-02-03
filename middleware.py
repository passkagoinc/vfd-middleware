from flask import Flask, request, jsonify
import serial

app = Flask(__name__)

# Configure the serial port (Update COM3 based on your actual port)
SERIAL_PORT = 'COM3'
BAUD_RATE = 9600

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=10)

except Exception as e:
    print(f"Error opening serial port: {e}")
    ser = None  # Prevent crash if the serial port is not found

@app.route('/display', methods=['POST'])
def display_text():
    if ser is None:
        return jsonify({'status': 'error', 'message': 'Serial port not available'})

    try:
        data = request.json
        text = data.get('text', '')

        # Clear the display
        ser.write(b'\x0C')  # Clear screen command

        # Send text to the VFD display
        ser.write(text.encode('ascii') + b'\r\n')

        return jsonify({'status': 'success', 'message': 'Text displayed on VFD.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(port=5000)
