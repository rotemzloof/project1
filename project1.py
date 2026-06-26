def checkWordCount(filePath):
    try:
        with open(filePath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("file path dont exsit")
        return 
   
    else:
        count = 0
        for word in content.split():
            clean_word = word.strip(",.!?;:\"'") 
            if clean_word:
                    count += 1 
        print("Total words:"+ str(count))
        return count
