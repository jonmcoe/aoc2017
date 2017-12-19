import sys

import shared


def mark_all_neighbors(as_bytes, row_num, col_num):
    if as_bytes[row_num][col_num] != '1':
        return
    else:
        as_bytes[row_num][col_num] = 'x'
    if row_num > 0:
        mark_all_neighbors(as_bytes, row_num - 1, col_num)
    if col_num > 0:
        mark_all_neighbors(as_bytes, row_num, col_num - 1)
    if row_num < len(as_bytes) - 1:
        mark_all_neighbors(as_bytes, row_num + 1, col_num)
    if col_num < len(as_bytes) - 1:  # assumes square
        mark_all_neighbors(as_bytes, row_num, col_num + 1)


if __name__ == '__main__':
    hashprefix = shared.get_string(sys.argv[1]).strip()
    all_hashes_hexstring = (shared.knot_hash("{0}-{1}".format(hashprefix, i)) for i in range(128))
    as_bytes = [list(shared.convert_hex_to_bytes(h)) for h in all_hashes_hexstring]
    regions = 0
    for row_num, row in enumerate(as_bytes):
        for col_num, cell in enumerate(row):
            if cell == '1':
                regions += 1
                mark_all_neighbors(as_bytes, row_num, col_num)
    print(regions)