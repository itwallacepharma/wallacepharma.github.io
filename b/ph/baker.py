import pandas as pd
    


# Replace text
def replaceTemp(body, user_name, user_url):
    body = body.replace("__user_name__", user_name)
    body = body.replace("__user_url__", user_url)
    return body


# Save file
def saveFile(body,file_name):
    with open(file_name, 'x') as f:
        f.write(body)


def main():
    # Read the template file
    # userBaseUrlList = []
    df = pd.read_csv('../../../data/ph_dr_websites_nov_v2.csv')
    for i, j in zip(df.user_name, df.user_url):
        with open('template.html', 'r') as f:
            body = f.read()
        file_name = f"{i.lower().replace(' ', '_').replace('.', '_')}.html"
        j = str(j.replace(" ", ""))
        body = replaceTemp(body, i, j)
        saveFile(body,file_name)
        # userBaseUrl = f"https://itwallacepharma.github.io/web/b/ph/{file_name}"
        # userBaseUrlList.append(userBaseUrl)
    # pd.DataFrame(userBaseUrlList).to_csv('userBaseUrlList.csv')
main()



