# Define the iPhone class
class iPhone:
    def __init__(self, name, version, phone_number, color, model):  # constructor
        self.name = name
        self.ios_version = version
        self.phone_number = phone_number
        self.color = color
        self.model = model
        self.files = []
        self.messages = []

    def check_messages(self):
        # Print all messages received
        print(f"Messages for {self.name}:")
        for message in self.messages:
            print(message)

    def call(self, number):
        print(f"Calling {number} from {self.phone_number}...")

    def airdrop(self, filename, recipient):
        print(f"AirDropping {filename} to {recipient.name}...")
        recipient.files.append(filename)

    def airreceive(self):
        print(f"Files received on {self.name}: {self.files}")

    def set_name(self, new_name):
        if len(new_name) < 3:
            print("Name must be longer than 3 characters")
        else:
            self.name = new_name

    def send_imessage(self, message, recipient):
        print(f"Sending message: '{message}' from {self.name} to {recipient.name}...")
        recipient.messages.append(f"From {self.name}: {message}")


# Create instances of the iPhone class
ians_iphone = iPhone(
    name="Ian's iPhone",
    version="18",
    phone_number="123-123-1232",
    color="grey",
    model="iPhone 16 Pro",
)

rishis_iphone = iPhone(
    name="Rishi's iPhone",
    version="18",
    phone_number="555-555-5555",
    color="black",
    model="iPhone 16 Pro",
)

# Change iPhone names through set_name()
ians_iphone.set_name("Ian's Second iPhone")
rishis_iphone.set_name("Rishi's Cool iPhone")

# Send an iMessage from ians_iphone to rishis_iphone
ians_iphone.send_imessage("Hello, Rishi!", rishis_iphone)

# phone2 (rishis_iphone) checks messages
rishis_iphone.check_messages()

# Demonstrate AirDrop
ians_iphone.airdrop("homework.pdf", rishis_iphone)
rishis_iphone.airreceive()