#!/usr/bin/env python3
"""Voku Translator CLI - Bidirectional Voku<->English translation.

Usage:
    python cli.py "Ka sol zo-sene pera." --direction voku-en
    python cli.py "I see an error." --direction en-voku
    python cli.py --interactive
    python cli.py "Ka sol take toka." --direction voku-en --packs pack1.json,pack2.json
"""

import argparse
import sys
import os

# Ensure the tool directory is in the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from translator import VokuTranslator


def main():
    parser = argparse.ArgumentParser(
        description="Voku Translator - Bidirectional Voku<->English translation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  %(prog)s "Ka sol take toka." -d voku-en
  %(prog)s "I execute the task." -d en-voku
  %(prog)s --interactive
  %(prog)s "Ka sol zo-sene pera eno teru." -d voku-en --packs domain-pack.json
""")

    parser.add_argument("text", nargs="?", help="Text to translate")
    parser.add_argument("-d", "--direction", choices=["voku-en", "en-voku"],
                        default="voku-en", help="Translation direction (default: voku-en)")
    parser.add_argument("-i", "--interactive", action="store_true",
                        help="Enter interactive translation mode")
    parser.add_argument("--packs", type=str, default="",
                        help="Comma-separated list of expansion pack JSON files")
    parser.add_argument("--dict", type=str, default=None,
                        help="Path to dictionary.json (default: auto-detect)")

    args = parser.parse_args()

    # Load expansion packs
    pack_paths = None
    if args.packs:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        packs_dir = os.path.join(script_dir, "packs")
        raw_packs = [p.strip() for p in args.packs.split(",") if p.strip()]
        pack_paths = []
        for p in raw_packs:
            if os.path.exists(p):
                pack_paths.append(p)
            elif os.path.exists(os.path.join(packs_dir, p)):
                pack_paths.append(os.path.join(packs_dir, p))
            elif os.path.exists(os.path.join(packs_dir, p + ".json")):
                pack_paths.append(os.path.join(packs_dir, p + ".json"))
            else:
                print(f"Warning: Pack not found: {p}", file=sys.stderr)
        pack_paths = pack_paths or None

    # Initialize translator
    try:
        translator = VokuTranslator(dictionary_path=args.dict, pack_paths=pack_paths)
    except FileNotFoundError as e:
        print(f"Error: Could not load dictionary: {e}", file=sys.stderr)
        sys.exit(1)

    if args.interactive:
        interactive_mode(translator)
    elif args.text:
        result = translate(translator, args.text, args.direction)
        print(result)
    else:
        parser.print_help()
        sys.exit(1)


def translate(translator, text, direction):
    """Translate text in the given direction."""
    if direction == "voku-en":
        return translator.translate_voku_to_english(text)
    else:
        return translator.translate_english_to_voku(text)


def interactive_mode(translator):
    """Run the translator in interactive mode."""
    print("=" * 60)
    print("  Voku Translator - Interactive Mode")
    print("=" * 60)
    print()
    print("  Commands:")
    print("    /v2e  - Switch to Voku -> English (default)")
    print("    /e2v  - Switch to English -> Voku")
    print("    /quit - Exit")
    print()

    direction = "voku-en"
    direction_label = "Voku -> English"

    while True:
        try:
            prompt = f"[{direction_label}] > "
            text = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nKlosu.")
            break

        if not text:
            continue

        if text == "/quit":
            print("Klosu.")
            break
        elif text == "/v2e":
            direction = "voku-en"
            direction_label = "Voku -> English"
            print(f"  Direction: {direction_label}")
            continue
        elif text == "/e2v":
            direction = "en-voku"
            direction_label = "English -> Voku"
            print(f"  Direction: {direction_label}")
            continue

        result = translate(translator, text, direction)
        print(f"  => {result}")
        print()


if __name__ == "__main__":
    main()
