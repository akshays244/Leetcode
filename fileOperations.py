import urllib.request
#using the inbuilt module which doesn't require to be installed like pip or something
# URL of the log file
url = 'https://public.karat.io/content/test/test_log.txt'

# Open the URL and read the contents
response = urllib.request.urlopen(url)

# Try to split without decoding
log_list = response.read().splitlines()  # This will still work, but the content will be in byte format

# Initialize counters for Block and released IPs
block_count = 0
released_ip_count = 0

# Loop through each line and further split them into blocks
for line in log_list:
    # Since the content is still in bytes, we need to decode each line before processing
    parts = line.decode('utf-8').split()  # Decode each line here

    # Check for "Block" and count occurrences
    if 'Block' in parts:
        block_count += 1

    # Check for "released" and count occurrences
    if 'Release' in parts:
        released_ip_count += 1

# Print the results
print(f"Number of 'Block' occurrences: {block_count}")
print(f"Number of 'released IPs': {released_ip_count}")
