"""
The idea is to provide an interface for translate
a MIDI stream into JSON, and then to do it the other way.

"""

from struct import unpack, pack


def read_varlen(data):
    NEXTBYTE = 1
    value = 0
    while NEXTBYTE:
        chr = ord(data.next())
        if not (chr & 0x80):
            NEXTBYTE = 0
        chr = chr & 0x7f
        value = value << 7
        value += chr
    return value


def parse_midi_header(binfile):
    header = binfile.read(4)
    assert header == 'MThd'
    length, format, tracks, res = unpack(">LHHH", binfile.read(10))
    if length > 14:
        binfile.read(length - 14)
    return length, format, tracks, res


def parse_track_header(binfile):
    header = binfile.read(4)
    assert header == 'MTrk'
    return unpack(">L", binfile.read(4))[0]


def parse_track(binfile, length):
    data = iter(binfile.read(length))
    while True:
        try:
            tick = read_varlen(data)
            stsmsg = ord(data.next())
            print tick
            print stsmsg
        except StopIteration:
            break


def midi_to_json(path):
    if isinstance(path, basestring):
        binfile = open(path, 'rb')
    elif isinstance(path, file):
        if not path.mode == 'rb':
            raise ValueError('File must be opened in Read-Binary mode')
        binfile = path
    else:
        raise ValueError
    length, format, tracks, res = parse_midi_header(binfile)
    tracklength = parse_track_header(binfile)
    parse_track(binfile, tracklength)


if __name__ == "__main__":
    midi_to_json('arp.mid')
