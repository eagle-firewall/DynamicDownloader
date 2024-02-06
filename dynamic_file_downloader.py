import requests
import threading
from tqdm import tqdm
import os


def download_segment(url, start, end, segment_index, progress_bar):
    headers = {'Range': f'bytes={start}-{end}'}
    response = requests.get(url, headers=headers, stream=True)
    filename = f"segment{segment_index}.part"

    with open(filename, 'wb') as file:
        with tqdm(total=(end - start + 1), unit='B', unit_scale=True, desc=f"Segment {segment_index}") as pb:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    pb.update(len(chunk))

    print(f"Segment {segment_index} downloaded.")


def download_file(url, num_segments, output_file_name):
    response = requests.head(url)
    content_length = int(response.headers['Content-Length'])
    total_size = content_length
    segment_size = content_length // num_segments

    threads = []
    start = 0
    end = segment_size - 1

    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading")

    for i in range(num_segments):
        if i == num_segments - 1:
            end = content_length - 1

        thread = threading.Thread(target=download_segment, args=(url, start, end, i, progress_bar))
        threads.append(thread)
        thread.start()
        start = end + 1
        end += segment_size

    for thread in threads:
        thread.join()

    merge_segments(num_segments, output_file_name)

    progress_bar.close()


def merge_segments(num_segments, output_file_name):
    with open(output_file_name, 'wb') as output_file:
        for i in range(num_segments):
            filename = f"segment{i}.part"
            with open(filename, 'rb') as segment_file:
                output_file.write(segment_file.read())
            os.remove(filename)

    print("File download completed.")


# Example usage
url = input("Enter your file URL: ")
num_segments = int(input("Enter the number of segments: "))
output_file_name = input("Enter the output file name with the format[name.format]: ")
download_file(url, num_segments, output_file_name)

