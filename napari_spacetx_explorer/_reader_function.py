from ._csv_io import CSVIO


def is_compatible(file_path):
    # CSV
    csv_reader = CSVIO(file_path)
    if csv_reader.is_compatible():
        return True

    return None


def read_spots(file_path):
    print("read spots:", file_path)
    # CSV
    csv_reader = CSVIO(file_path)
    if csv_reader.is_compatible():
        csv_reader.read()
        return csv_reader.total_data

    return None

