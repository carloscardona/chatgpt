"""Simple CLI application to add two numbers."""

import argparse


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for two numbers.

    Returns:
        argparse.Namespace: Parsed arguments with num1 and num2.
    """

    parser = argparse.ArgumentParser(description="Add two numbers together")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = args.num1 + args.num2
    print(f"{args.num1} + {args.num2} = {result}")


if __name__ == "__main__":
    main()
