
try:
    import pip
except:
    import os
    import urllib

    urllib.request.urlretrieve("https://bootstrap.pypa.io/get-pip.py", "get-pip.py")
    os.system("python get-pip.py")

    import pip


def run():
    pip.main(["install", "PyQt5"])


if __name__ == "__main__":
    run()
