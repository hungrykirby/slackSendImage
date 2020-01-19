# import slackItem

import slackItem

def main():
  si = slackItem.SlackItem()
  si.test()
  si.post_with_img('test.jpg', 'title', 'init\ncomment')

if __name__ == "__main__":
  print("Hello bot")
  main()