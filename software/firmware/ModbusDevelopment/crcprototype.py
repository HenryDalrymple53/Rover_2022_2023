knownPackets = [
    [0x01, 0x03, 0x00, 0x03, 0x00, 0x03],
    [0x01, 0x10, 0x00, 0x00, 0x00, 0x03],
    [0x01, 0x10, 0x01, 0x00, 0x01, 0x01, 0x04, 0x40, 0x48, 0xf5, 0xc3],
    [0x01, 0x10, 0x00, 0x00, 0x00, 0x01, 0x02, 0x42, 0x42],
    [0x01, 0x10, 0x01, 0x00, 0x01, 0x01, 0x04, 0x40, 0x48, 0xf5, 0xc3],
    [0x01, 0x10, 0x02, 0x00, 0x02, 0x01, 0x01, 0x42],
    [0x01, 0x10, 0x03, 0x00, 0x03, 0x01, 0x01, 0x01],
    [0x00, 0x10, 0x00, 0x00, 0x00, 0x01]]
#knownCRCs   = [0xf5cb,0x8008]

"""
in c

UInt16 ModRTU_CRC(byte[] buf, int len)
{
  UInt16 crc = 0xFFFF;

  for (int pos = 0; pos < len; pos++) {
    crc ^= (UInt16)buf[pos];          // XOR byte into least sig. byte of crc

    for (int i = 8; i != 0; i--) {    // Loop over each bit
      if ((crc & 0x0001) != 0) {      // If the LSB is set
        crc >>= 1;                    // Shift right and XOR 0xA001
        crc ^= 0xA001;
      }
      else                            // Else LSB is not set
        crc >>= 1;                    // Just shift right
    }
  }
  // Note, this number has low and high bytes swapped, so use it accordingly (or swap bytes)
  return crc;
}

"""

def modRTU_CRC(packet,len):
    crc = 0xffff
    for i in range(len):
        crc ^= packet[i]

        for j in range(8,0,-1):
            if((crc & 0x001) != 0):
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    crcbytes = crc.to_bytes(2,'big')
    crcar = bytearray(crcbytes)
    crcar.reverse()
    return crcar



for i in knownPackets:
    print("Packet: ")
    print(i)
    print("crc:")
    print(modRTU_CRC(i,len(i)))
    print("")
