import pykakasi

def convert_and_print(text):
    kks = pykakasi.kakasi()
    result = kks.convert(text)
    #print(f'This is result for: {text}')
    for item in result:
        print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(item['orig'], item['kana'], item['hira'], item['hepburn']))

def main():
    text = "私は元気です。ありがとうございます。あなたは日本語の勉強をしていますか？"
    convert_and_print(text)

if __name__ == "__main__":
    main()
