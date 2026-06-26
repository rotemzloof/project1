def checkWordCount():
    try:
        f = open('filePath', 'r')
        content = f.read()
        f.close()
    except FileNotFoundError:
        print("file path dont exsit")
        return 
   
    else:
        count = 0
        for word in content.split():
            count += 1 
        print("Total words:"+count)
        return count
