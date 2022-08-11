class Morse:
    MORSE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
        '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.',
        ')': '-.--.-', ' ': '  ',
    }

    def __init__(self):
        self.active = True
        self.message = str()

    # Main loop
    def run(self):
        while self.active:

            # Ask user for an input
            self.message = input("Insert your message (type 'quit' to exit): \n").upper().lstrip(" ").rstrip(" ")

            try:

                # If the input is a plain text
                if self.message[0] not in self.MORSE_DICT['A']:
                    # Check if user wants to break the loop and quit
                    if self.message == "QUIT":
                        self.active = False
                        break

                    print(f"Your Morse message: {self.to_morse()}")

                # If the input is a morse code
                else:
                    print(f"Result text: {self.from_morse()}")

            # If the input is empty
            except IndexError:
                print("No message received. Try again...")

    # To Morse Converter
    def to_morse(self) -> str:
        separated_text = [char for char in self.message]
        return "".join([self.MORSE_DICT[char] + " " for char in separated_text])

    # From Morse Converter
    def from_morse(self) -> str:
        key_list = list(self.MORSE_DICT.keys())
        val_list = list(self.MORSE_DICT.values())

        split_message = self.message.split(" ")
        result_list = list()

        for i in range(len(split_message)):
            # Deal with multiple spaces of Morse
            if not split_message[i] == split_message[i-1] == "":
                if split_message[i] != "":
                    result_list.append(key_list[val_list.index(split_message[i])].lower())
                else:
                    result_list.append(" ")

        return "".join(result_list).capitalize()


if __name__ == "__main__":
    morse = Morse()
    morse.run()
