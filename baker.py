


# Set variables
user_name = "Pushpinder Sharma"
user_url = "https://www.drpushpindersharma.in/"
file_name = f"pages/{user_name.lower().replace(' ', '_')}.html"

# Replace text
def replaceTemp(body, user_name, user_url, file_name):
    body = body.replace("__temp_name__", user_name)
    body = body.replace("__temp_url__", user_url)
    return body


# Save file
def saveFile(body,file_name):
    with open(file_name, 'x') as f:
        f.write(body)

def main():
    # Read the template file
    with open('index.html', 'r') as f:
        body = f.read()

    body = replaceTemp(body, user_name, user_url, file_name)
    saveFile(body,file_name)

main()
