def main():
    try:
        open("/path/to/mars.jpg")
    except OSError as error:
        if error.errno == 2:
            print("Couldn´t find the image file!")
        elif error.errno == 13:
            print("Found config.txt but couldn´t read it")

if __name__ == '__main__':
    main()