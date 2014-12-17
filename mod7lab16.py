#Module 7 Lab 16
#Team 3
#Christopher Rendall
#Sevren Gail

#makePage writes content to a user-supplied html page.
def makePage(content):
  printNow("Choose an HTML file to write to.")
  file = pickAFile()
  file = open(file, "wt")
  data = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transition//EN" "http://www.w3.org/TR/html4/loose.dtd\"><html><head><title>Lab 16 - URLs and HTML</title></head><body>" + content + "</body></html>"
  file.write(data)
  file.close()

#createRedditCats pulls information from Reddit, creates a list of post titles and links, then creates
#content from those titles and links. It then calls makePage(content) to write the content to an HTML file.
def createRedditCats():
  import urllib
  handle = urllib.urlopen("https://www.reddit.com/r/catpictures/")
  data = handle.read()
  posts = []
  blocks = data.split("<a class=\"title may-blank \"")
  for i in range(2, len(blocks)):
    block = blocks[i]
    title = block.split(">")[1].split("<")[0]
    url = block.split("href=\"")[1].split("\"")[0]
    commentsUrl = "https://www.reddit.com/r/catpictures/comments" + block.split("https://www.reddit.com/r/catpictures/comments")[1].split("\"")[0]
    numberOfComments = block.split("<a href=\"https://www.reddit.com/r/catpictures/comments")[1].split(">")[1].split("<")[0]
    if numberOfComments.find(" ") != -1:
      numberOfComments = str(numberOfComments.split(" ")[0])
    else:
      numberOfComments = "0"
    if ".jpg" in url:
      posts.append(title + "|||" + url + "|||" + numberOfComments + "|||" + commentsUrl)
  content = "<H1>Front Page of <a href=\"https://www.reddit.com/r/catpictures\">/r/catpictures</a></H1>"
  for i in range(0, len(posts)):
    content += "<h2>" + posts[i].split("|||")[0] + "</h2>"
    content += "<img src=\"" + posts[i].split("|||")[1] + "\" style=\"width:500px; height:500px;\"> <br />"
    content += "<b>Number of Comments: <a href=\"" + posts[i].split("|||")[3] + "\">" + posts[i].split("|||")[2] + "</a> <br /></b>"
  makePage(content)
createRedditCats()