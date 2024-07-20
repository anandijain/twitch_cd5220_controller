# %% 
import serial
import time

def main():
    # Configure the serial port
    port = serial.Serial(
        port='COM4',       # Update this to the correct COM port
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

    # Open the serial port
    if not port.is_open:
        port.open()

    try:
        while True:
            # Read input from the user
            message = input("Enter message to send to display: ")

            # Prepare the message for the display, ensuring it does not exceed the display's width.
            # Each line can hold 20 characters, so we truncate to 40 characters (2 lines).
            display_message = message[:40]
            command_to_send = f"\x1B\x51\x41{display_message}\r"  # ESC Q A...CR, to write to the upper line

            # Send the prepared message to the display
            port.write(command_to_send.encode('utf-8'))
            print('Message sent to display')
    except KeyboardInterrupt:
        print("Program interrupted by user")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the serial port
        port.close()
        print("Serial port closed")

if __name__ == "__main__":
    main()

# %%
