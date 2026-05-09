import random
import time
import sys
import threading

# Common guitar chords organized by type
MAJOR_CHORDS = ["A", "B", "C", "D", "E", "F", "G"]  # , "Bb", "Db", "Eb", "F#", "Ab"]
MINOR_CHORDS = [
    "Am",
    "Bm",
    "Cm",
    "Dm",
    "Em",
    "Fm",
    "Gm",
    "Bbm",
    "Dbm",
    "Ebm",
    "F#m",
    "Abm",
]
SEVENTH_CHORDS = ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "Bb7", "Eb7", "F#7", "Ab7"]
MINOR_SEVENTH_CHORDS = [
    "Am7",
    "Bm7",
    "Cm7",
    "Dm7",
    "Em7",
    "Fm7",
    "Gm7",
    "Bbm7",
    "Dbm7",
    "Ebm7",
    "F#m7",
    "Abm7",
]
MAJOR_SEVENTH_CHORDS = [
    "Amaj7",
    "Bmaj7",
    "Cmaj7",
    "Dmaj7",
    "Emaj7",
    "Fmaj7",
    "Gmaj7",
    "Bbmaj7",
    "Dbmaj7",
    "Ebmaj7",
    "F#maj7",
    "Abmaj7",
]
SUS_CHORDS = [
    "Asus2",
    "Asus4",
    "Csus2",
    "Csus4",
    "Dsus2",
    "Dsus4",
    "Esus2",
    "Esus4",
    "Fsus2",
    "Fsus4",
    "Gsus2",
    "Gsus4",
]

CUSTOM_CHORDS = MAJOR_CHORDS + ["Am", "Dm", "Em", "A7", "D7", "E7"]

CHORD_TYPES = {
    "major": MAJOR_CHORDS,
    "minor": MINOR_CHORDS,
    "7th": SEVENTH_CHORDS,
    "m7": MINOR_SEVENTH_CHORDS,
    "maj7": MAJOR_SEVENTH_CHORDS,
    "sus": SUS_CHORDS,
    "all": MAJOR_CHORDS
    + MINOR_CHORDS
    + SEVENTH_CHORDS
    + MINOR_SEVENTH_CHORDS
    + MAJOR_SEVENTH_CHORDS
    + SUS_CHORDS,
    "custom": CUSTOM_CHORDS,
}


def countdown_timer(seconds=5, stop_event=None):
    """Display a countdown timer for the given number of seconds. Can be stopped by stop_event."""
    if stop_event is None:
        stop_event = threading.Event()

    for i in range(seconds, 0, -1):
        if stop_event.is_set():
            sys.stdout.write("\r" + " " * 40 + "\n")
            sys.stdout.flush()
            return
        sys.stdout.write(f"\r⏱️  Time remaining: {i}s ")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r⏱️  Time's up!        \n")
    sys.stdout.flush()


class ChordBag:
    """A bag-based chord selector that cycles through all chords before repeating."""

    def __init__(self, chords):
        """Initialize the bag with chords."""
        self.original_chords = list(chords)
        self.bag = []
        self.refill()

    def refill(self):
        """Refill and shuffle the bag."""
        self.bag = self.original_chords.copy()
        random.shuffle(self.bag)

    def draw(self):
        """Draw a chord from the bag. Refills if empty."""
        if not self.bag:
            self.refill()
        return self.bag.pop()


def randomize_chord(chord_bag, seconds=5, stop_event=None):
    """Draw and display a chord from the bag with countdown."""
    if stop_event is None:
        stop_event = threading.Event()
    chord = chord_bag.draw()
    print("\n" + "=" * 40)
    print(f"🎸 Play this chord: {chord}")
    print("=" * 40)
    countdown_timer(seconds, stop_event)


def main():
    """Main loop for the chord randomizer."""
    print("Guitar Chord Randomizer")
    print("=" * 40)

    # Chord type selection menu
    print("\nChoose chord type(s):")
    print("1) All chords")
    print("2) Major chords")
    print("3) Minor chords")
    print("4) 7th chords")
    print("5) Minor 7th chords")
    print("6) Major 7th chords")
    print("7) Sus chords")
    print("8) Custom")
    print("\nYou can select multiple: e.g., '2,3,4' or '2 3 4'")

    choice = input("\nEnter choice(s) (default is 1): ").strip()
    chord_map = {
        "1": "all",
        "2": "major",
        "3": "minor",
        "4": "7th",
        "5": "m7",
        "6": "maj7",
        "7": "sus",
        "8": "custom",
    }

    # Parse multiple selections
    if not choice:
        selected_chords = CHORD_TYPES["all"]
        selected_types = ["all"]
    else:
        # Handle comma or space separated input
        choices = choice.replace(",", " ").split()
        selected_chords = []
        selected_types = []

        for c in choices:
            chord_type = chord_map.get(c)
            if chord_type:
                if chord_type == "all":
                    selected_chords = CHORD_TYPES["all"]
                    selected_types = ["all"]
                    break
                else:
                    selected_chords.extend(CHORD_TYPES[chord_type])
                    selected_types.append(chord_type)

        # Default to all if no valid selections
        if not selected_chords:
            selected_chords = CHORD_TYPES["all"]
            selected_types = ["all"]

    # Time selection
    time_input = input("\nHow many seconds per chord? (default is 5): ").strip()
    try:
        seconds = int(time_input) if time_input else 5
        if seconds < 1:
            seconds = 1
    except ValueError:
        seconds = 5

    selected_str = ", ".join(selected_types).title()
    print(f"\n✓ Selected: {selected_str}")
    print(f"✓ Time per chord: {seconds} seconds")
    print("✓ Using bag method (no repeats until all chords played)")
    print("✓ Press any key to exit\n")

    # Create the chord bag
    chord_bag = ChordBag(selected_chords)

    # Flag to stop the program
    stop_event = threading.Event()

    def listen_for_input():
        """Listen for any input and set the stop event."""
        try:
            input()
            stop_event.set()
        except EOFError:
            pass

    # Start input listener thread
    input_thread = threading.Thread(target=listen_for_input, daemon=True)
    input_thread.start()

    try:
        while not stop_event.is_set():
            randomize_chord(chord_bag, seconds, stop_event)
    except KeyboardInterrupt:
        pass

    print("\nThanks for practicing! 🎵")


if __name__ == "__main__":
    main()
