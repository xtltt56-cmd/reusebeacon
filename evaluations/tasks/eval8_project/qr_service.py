"""QR code generation for ticketing. Not implemented yet."""
import sys


def make_qr(payload: str, out_png: str, ecc: str = "H") -> None:
    """Render `payload` as a scannable QR code PNG at error-correction level `ecc`."""
    raise NotImplementedError("QR rendering not implemented yet")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: py -3.12 qr_service.py payload.txt out.png", file=sys.stderr)
        sys.exit(2)
    payload = open(sys.argv[1], encoding="utf-8").read()
    make_qr(payload, sys.argv[2])
    print(f"written: {sys.argv[2]}")
